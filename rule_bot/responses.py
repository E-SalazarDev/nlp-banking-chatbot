FIXED_RESPONSES = {
    "saludo": (
        "Hola. Soy el asistente virtual bancario. "
        "Puedo ayudarte a consultar saldo, solicitar tu estado de cuenta, "
        "resolver problemas de acceso o responder dudas generales."
    ),

    "consulta_saldo": (
        "Para consultar tu saldo bancario, ingresa a la sección 'Mis cuentas' "
        "de la aplicación bancaria. Por seguridad, primero deberás verificar tu identidad. "
        "¿Deseas consultar el saldo de una cuenta de ahorro, nómina o crédito?"
    ),

    "estado_cuenta": (
        "Puedes consultar tu estado de cuenta desde la sección 'Estados de cuenta' "
        "en la aplicación o banca en línea. También puedes seleccionar el periodo "
        "que deseas revisar, por ejemplo, el último mes o una fecha específica."
    ),

    "soporte": (
        "Entiendo que necesitas ayuda. Si tienes problemas para acceder a tu cuenta, "
        "te recomiendo verificar tu conexión, confirmar que tus datos sean correctos "
        "y utilizar la opción 'Recuperar contraseña'. Si el problema continúa, "
        "puedo orientarte con opciones de soporte técnico."
    ),

    "consulta_general": (
        "Puedo brindarte información general sobre cuentas, tarjetas, comisiones, "
        "horarios de atención y servicios bancarios disponibles. "
        "¿Sobre qué servicio deseas más información?"
    ),
}


FALLBACK_RESPONSE = (
    "Lo siento, no pude identificar con claridad tu solicitud.\n\n"
    "Puedes reformular tu consulta o elegir una de estas opciones:\n"
    "1. Consultar saldo\n"
    "2. Estado de cuenta\n"
    "3. Soporte técnico\n"
    "4. Consulta general\n\n"
    "¿Cómo puedo ayudarte?"
)