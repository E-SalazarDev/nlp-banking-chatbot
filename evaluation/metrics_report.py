import json
from rule_bot.chatbot import RuleBasedChatbot

bot = RuleBasedChatbot()

with open(
    "evaluation/test_cases.json",
    "r",
    encoding="utf-8"
) as f:
    cases = json.load(f)

correct = 0

for case in cases:

    predicted = bot.get_response(
        case["text"]
    )["intent"]

    if predicted == case["expected_intent"]:
        correct += 1

accuracy = correct / len(cases)

report = {
    "total_cases": len(cases),
    "correct_predictions": correct,
    "accuracy": accuracy
}

with open(
    "evaluation/reports/metrics.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=4
    )