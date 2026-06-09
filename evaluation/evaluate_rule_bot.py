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
results = []

for case in cases:

    prediction = bot.get_response(
        case["text"]
    )["intent"]

    expected = case["expected_intent"]

    success = prediction == expected

    if success:
        correct += 1

    results.append({
        "input": case["text"],
        "expected": expected,
        "predicted": prediction,
        "success": success
    })

accuracy = correct / len(cases)

print("=" * 80)
print(f"Accuracy: {accuracy:.2%}")
print("=" * 80)

for r in results:
    print(r)