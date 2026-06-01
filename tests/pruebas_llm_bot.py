from llm_bot.chatbot import LLMChatbot


def print_context_result(text, result):
    print("\n" + "=" * 90)
    print(f"USUARIO    : {text}")
    print(f"INTENCIÓN  : {result['intent']}")
    print(f"ENTIDADES  : {result['entities']}")

    print("\nRESPUESTA:")
    print(result["response"])

    print("\nCONTEXTO:")
    context = result["context"]
    print(f"  Intención activa    : {context['intencion_activa']}")
    print(f"  Pregunta pendiente  : {context['pregunta_pendiente']}")
    print(f"  Entidades acumuladas: {context['entidades_acumuladas']}")

    print("=" * 90)


print("\n" + "#" * 90)
print("FLUJO 1: CONSULTA DE SALDO")
print("#" * 90)

bot_saldo = LLMChatbot()

flujo_saldo = [
    "Hola",
    "Quiero consultar mi saldo",
    "De mi cuenta de ahorro",
    "Gracias",
]

for text in flujo_saldo:
    result = bot_saldo.get_response(text)
    print_context_result(text, result)


print("\n" + "#" * 90)
print("FLUJO 2: ESTADO DE CUENTA")
print("#" * 90)

bot_estado = LLMChatbot()

flujo_estado = [
    "Quiero mi estado de cuenta",
    "De enero",
    "¿Lo puedo descargar en PDF?",
    "Gracias",
]

for text in flujo_estado:
    result = bot_estado.get_response(text)
    print_context_result(text, result)


print("\n" + "#" * 90)
print("FLUJO 3: SOPORTE")
print("#" * 90)

bot_soporte = LLMChatbot()

flujo_soporte = [
    "No puedo entrar a la aplicación",
    "Me aparece error al iniciar sesión",
    "¿Qué puedo hacer primero?",
    "Gracias",
]

for text in flujo_soporte:
    result = bot_soporte.get_response(text)
    print_context_result(text, result)


print("\n" + "#" * 90)
print("PRUEBA DE FALLBACK Y RECUPERACIÓN")
print("#" * 90)

bot_fallback = LLMChatbot()

flujo_fallback = [
    "Me gusta comer pizza los viernes",
    "Quiero consultar saldo",
    "De mi cuenta de nómina",
]

for text in flujo_fallback:
    result = bot_fallback.get_response(text)
    print_context_result(text, result)


print("\n" + "#" * 90)
print("PRUEBA DE EXTRACCIÓN DE ENTIDADES ADICIONALES")
print("#" * 90)

bot_entidades = LLMChatbot()

flujo_entidades = [
    "Quiero transferir $5000 mañana",
]

for text in flujo_entidades:
    result = bot_entidades.get_response(text)
    print_context_result(text, result)