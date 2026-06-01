from rule_bot.chatbot import RuleBasedChatbot


bot = RuleBasedChatbot()

queries = [
    "Hola",
    "Dame mi saldo bancario",
    "Quiero mi estado de cuenta",
    "Necesito ayuda con mi cuenta",
    "No puedo entrar a la aplicación",
    "Quiero consultar el saldo de mi cuenta de ahorro",
    "Necesito mi estado de cuenta de enero",
    "Quiero transferir $5000 mañana",
    "Me gusta comer pizza los viernes",
]

print("\n" + "#" * 90)
print("PRUEBAS DEL CHATBOT BASADO EN REGLAS")
print("#" * 90)

for query in queries:
    result = bot.get_response(query)

    print("\n" + "=" * 90)
    print(f"USUARIO    : {query}")
    print(f"INTENCIÓN  : {result['intent']}")
    print(f"ENTIDADES  : {result['entities']}")
    print("-" * 90)
    print("RESPUESTA:")
    print(result["response"])
    print("=" * 90)