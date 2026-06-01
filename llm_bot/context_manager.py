class ContextManager:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []
        self.active_intent = None
        self.pending_question = None
        self.collected_entities = {
            "tipo_cuenta": None,
            "monto": None,
            "fecha": None,
            "tipo_solicitud": None,
        }

    def add_turn(self, user_text, intent, entities, response):
        self.history.append({
            "usuario": user_text,
            "intencion": intent,
            "entidades": entities,
            "respuesta": response,
        })

        if len(self.history) > self.max_turns:
            self.history = self.history[-self.max_turns:]

    def update_entities(self, entities):
        for key, value in entities.items():
            if value:
                self.collected_entities[key] = value

    def set_active_intent(self, intent):
        if intent not in ["fallback", "cierre"]:
            self.active_intent = intent

    def set_pending_question(self, question):
        self.pending_question = question

    def clear_pending_question(self):
        self.pending_question = None

    def clear_flow(self):
        self.active_intent = None
        self.pending_question = None
        self.collected_entities = {
            "tipo_cuenta": None,
            "monto": None,
            "fecha": None,
            "tipo_solicitud": None,
        }

    def get_context(self):
        return {
            "historial": self.history,
            "intencion_activa": self.active_intent,
            "pregunta_pendiente": self.pending_question,
            "entidades_acumuladas": self.collected_entities,
        }