import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rule_bot.chatbot import RuleBasedChatbot


def main():
    bot = RuleBasedChatbot()

    test_cases_path = PROJECT_ROOT / "evaluation" / "test_cases.json"

    with open(test_cases_path, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    correct = 0
    total = len(test_cases)

    print("=" * 80)
    print("RULE BOT EVALUATION")
    print("=" * 80)

    for case in test_cases:
        user_input = case["text"]
        expected_intent = case["expected_intent"]

        result = bot.get_response(user_input)
        predicted_intent = result["intent"]

        success = predicted_intent == expected_intent

        if success:
            correct += 1

        print(f"Input     : {user_input}")
        print(f"Expected  : {expected_intent}")
        print(f"Predicted : {predicted_intent}")
        print(f"Success   : {success}")
        print("-" * 80)

    accuracy = correct / total if total > 0 else 0

    print("=" * 80)
    print(f"Total cases          : {total}")
    print(f"Correct predictions  : {correct}")
    print(f"Intent accuracy      : {accuracy:.2%}")
    print("=" * 80)


if __name__ == "__main__":
    main()