import re


ACCOUNT_TYPES = {
    "ahorro": ["ahorro", "cuenta de ahorro"],
    "nomina": ["nomina", "nómina", "cuenta de nomina", "cuenta de nómina"],
    "credito": [
        "credito", "crédito",
        "tarjeta de credito", "tarjeta de crédito",
        "cuenta de credito", "cuenta de crédito",
    ],
}

REQUEST_TYPES = {
    "descarga_pdf": ["pdf", "descargar", "descarga", "bajar", "guardar"],
    "ubicacion_app": ["donde", "dónde", "seccion", "sección", "encuentro", "ubico", "app"],
    "acceso_app": ["no puedo entrar", "iniciar sesión", "iniciar sesion", "acceder", "error al iniciar"],
    "recuperar_contrasena": ["contraseña", "contrasena", "recuperar", "olvide", "olvidé"],
    "bloqueo": ["bloqueo", "bloqueada", "bloqueado", "desbloquear"],
    "movimientos": ["movimientos", "transacciones", "cargos", "compras"],
    "cierre": ["gracias", "muchas gracias", "ok gracias", "listo", "eso es todo"],
}

MONTHS = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def extract_entities(text: str) -> dict:
    text = text.lower()

    entities = {
        "tipo_cuenta": None,
        "monto": None,
        "fecha": None,
        "tipo_solicitud": None,
    }

    for account, patterns in ACCOUNT_TYPES.items():
        if any(pattern in text for pattern in patterns):
            entities["tipo_cuenta"] = account
            break

    amount_match = re.search(r"\$?\d+(?:,\d{3})*(?:\.\d+)?", text)
    if amount_match:
        entities["monto"] = amount_match.group()

    for month in MONTHS:
        if month in text:
            entities["fecha"] = month
            break

    if not entities["fecha"]:
        date_match = re.search(
            r"\b(hoy|ayer|mañana|manana|semana pasada|mes pasado|último mes|ultimo mes)\b",
            text,
        )
        if date_match:
            entities["fecha"] = date_match.group()

    for request_type, patterns in REQUEST_TYPES.items():
        if any(pattern in text for pattern in patterns):
            entities["tipo_solicitud"] = request_type
            break

    return entities