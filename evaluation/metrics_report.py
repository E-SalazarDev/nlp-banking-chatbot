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
    reports_dir = PROJECT_ROOT / "evaluation" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    with open(test_cases_path, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    correct = 0
    results = []

    for case in test_cases:
        user_input = case["text"]
        expected_intent = case["expected_intent"]

        result = bot.get_response(user_input)
        predicted_intent = result["intent"]
        success = predicted_intent == expected_intent

        if success:
            correct += 1

        results.append({
            "input": user_input,
            "expected_intent": expected_intent,
            "predicted_intent": predicted_intent,
            "success": success,
            "entities": result["entities"],
        })

    total = len(test_cases)
    accuracy = correct / total if total > 0 else 0

    report = {
        "model_type": "rule_based_chatbot",
        "total_cases": total,
        "correct_predictions": correct,
        "intent_accuracy": accuracy,
        "results": results,
    }

    output_path = reports_dir / "metrics.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"Metrics report generated: {output_path}")


if __name__ == "__main__":
    main()