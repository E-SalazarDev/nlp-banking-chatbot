from rule_bot.chatbot import RuleBasedChatbot
from llm_bot.chatbot import LLMChatbot


entradas = [
    "Hola",
    "Dame mi saldo bancario",
    "Quiero mi estado de cuenta",
    "Necesito ayuda con mi cuenta",
    "No puedo entrar a la aplicación",
]

rule_bot = RuleBasedChatbot()
llm_bot = LLMChatbot()

print("\n" + "#" * 120)
print("COMPARACIÓN ENTRE CHATBOT BASADO EN REGLAS Y CHATBOT CON LLM")
print("#" * 120)

resultados = []

for entrada in entradas:
    regla = rule_bot.get_response(entrada)
    llm = llm_bot.get_response(entrada)

    resultados.append({
        "entrada": entrada,
        "intent_reglas": regla["intent"],
        "entidades_reglas": regla["entities"],
        "respuesta_reglas": regla["response"],
        "intent_llm": llm["intent"],
        "entidades_llm": llm["entities"],
        "respuesta_llm": llm["response"],
    })


for i, item in enumerate(resultados, start=1):
    print("\n" + "=" * 120)
    print(f"PRUEBA {i}")
    print(f"ENTRADA: {item['entrada']}")
    print("-" * 120)

    print("BOT BASADO EN REGLAS")
    print(f"Intención  : {item['intent_reglas']}")
    print(f"Entidades  : {item['entidades_reglas']}")
    print(f"Respuesta  : {item['respuesta_reglas']}")

    print("-" * 120)

    print("BOT CON LLM")
    print(f"Intención  : {item['intent_llm']}")
    print(f"Entidades  : {item['entidades_llm']}")
    print(f"Respuesta  : {item['respuesta_llm']}")

    print("=" * 120)


print("\n" + "#" * 120)
print("TABLA RESUMIDA")
print("#" * 120)

print(
    f"{'Entrada':35} | "
    f"{'Intent reglas':18} | "
    f"{'Intent LLM':18} | "
    f"{'Observación'}"
)
print("-" * 120)

for item in resultados:
    observacion = "Ambos detectan la misma intención"

    if item["intent_reglas"] != item["intent_llm"]:
        observacion = "Diferencia en intención detectada"

    print(
        f"{item['entrada'][:35]:35} | "
        f"{item['intent_reglas'][:18]:18} | "
        f"{item['intent_llm'][:18]:18} | "
        f"{observacion}"
    )