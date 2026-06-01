from rule_bot.intents import INTENT_PATTERNS
from rule_bot.responses import FIXED_RESPONSES, FALLBACK_RESPONSE
from rule_bot.entities import extract_entities


class RuleBasedChatbot:

    def __init__(self):
        self.last_intent = None

    def detect_intent(self, text: str):
        text = text.lower()

        for intent, patterns in INTENT_PATTERNS.items():
            for pattern in patterns:
                if pattern in text:
                    return intent

        return None

    def get_response(self, text: str):
        intent = self.detect_intent(text)
        entities = extract_entities(text)

        if intent is None:
            return {
                "intent": "fallback",
                "entities": entities,
                "response": FALLBACK_RESPONSE,
            }

        self.last_intent = intent

        return {
            "intent": intent,
            "entities": entities,
            "response": FIXED_RESPONSES[intent],
        }