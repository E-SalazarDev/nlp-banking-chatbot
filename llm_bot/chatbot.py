import requests

from rule_bot.chatbot import RuleBasedChatbot
from rule_bot.responses import FALLBACK_RESPONSE
from llm_bot.context_manager import ContextManager
from llm_bot.prompt_builder import build_banking_prompt


class LLMChatbot:
    def __init__(self, model="llama3.2"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"
        self.rule_bot = RuleBasedChatbot()
        self.context_manager = ContextManager(max_turns=5)

    def is_closing_message(self, entities):
        return entities.get("tipo_solicitud") == "cierre"

    def infer_intent_from_context(self, detected_intent, entities, text):
        text = text.lower()

        if detected_intent != "fallback":
            return detected_intent

        if self.context_manager.active_intent:
            return self.context_manager.active_intent

        if entities.get("tipo_cuenta"):
            return "consulta_saldo"

        if entities.get("tipo_solicitud") == "descarga_pdf":
            return "estado_cuenta"

        if entities.get("fecha") and self.context_manager.active_intent == "estado_cuenta":
            return "estado_cuenta"

        if entities.get("tipo_solicitud") in [
            "ubicacion_app",
            "acceso_app",
            "recuperar_contrasena",
            "bloqueo",
            "movimientos",
        ]:
            return "soporte"

        if "pdf" in text or "descargar" in text:
            return "estado_cuenta"

        if "primero" in text or "error" in text:
            return "soporte"

        return detected_intent

    def needs_follow_up(self, intent):
        entities = self.context_manager.collected_entities

        if intent == "consulta_saldo" and not entities.get("tipo_cuenta"):
            return "¿De qué tipo de cuenta deseas consultar el saldo: ahorro, nómina o crédito?"

        if intent == "estado_cuenta" and not entities.get("fecha"):
            return "¿De qué periodo necesitas tu estado de cuenta?"

        if intent == "soporte" and not entities.get("tipo_solicitud"):
            return "¿Qué problema específico tienes: acceso a la app, contraseña, bloqueo o movimientos no reconocidos?"

        return None

    def generate_with_ollama(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1
            }
        }

        response = requests.post(
            self.ollama_url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()
        return response.json()["response"].strip()

    def get_response(self, user_text):
        rule_result = self.rule_bot.get_response(user_text)

        detected_intent = rule_result["intent"]
        detected_entities = rule_result["entities"]

        if self.is_closing_message(detected_entities):
            response = (
                "Con gusto. Me alegra haberte ayudado. "
                "Si necesitas otra consulta bancaria, estaré disponible."
            )

            self.context_manager.add_turn(
                user_text=user_text,
                intent="cierre",
                entities=detected_entities,
                response=response,
            )

            self.context_manager.clear_flow()

            return {
                "intent": "cierre",
                "entities": detected_entities,
                "response": response,
                "context": self.context_manager.get_context(),
            }

        intent = self.infer_intent_from_context(
            detected_intent=detected_intent,
            entities=detected_entities,
            text=user_text,
        )

        if intent == "fallback":
            response = FALLBACK_RESPONSE

            self.context_manager.add_turn(
                user_text=user_text,
                intent=intent,
                entities=detected_entities,
                response=response,
            )

            return {
                "intent": intent,
                "entities": detected_entities,
                "response": response,
                "context": self.context_manager.get_context(),
            }

        self.context_manager.update_entities(detected_entities)
        self.context_manager.set_active_intent(intent)

        follow_up = self.needs_follow_up(intent)

        if follow_up:
            response = follow_up
            self.context_manager.set_pending_question(follow_up)
        else:
            prompt = build_banking_prompt(
                user_text=user_text,
                intent=intent,
                entities=self.context_manager.collected_entities,
                context=self.context_manager.get_context(),
            )

            response = self.generate_with_ollama(prompt)
            self.context_manager.clear_pending_question()

        self.context_manager.add_turn(
            user_text=user_text,
            intent=intent,
            entities=self.context_manager.collected_entities.copy(),
            response=response,
        )

        return {
            "intent": intent,
            "entities": self.context_manager.collected_entities.copy(),
            "response": response,
            "context": self.context_manager.get_context(),
        }