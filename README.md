# Instalación y configuración

## Requisitos previos

Antes de ejecutar el proyecto es necesario tener instalado:

* Python 3.11 o superior
* Ollama
* Modelo Llama 3.2 descargado localmente

Verificar instalación de Python:

```bash
python --version
```

Verificar instalación de Ollama:

```bash
ollama --version
```

---

## Instalación de Ollama

Descargar e instalar Ollama desde:

https://ollama.com/download

Una vez instalado, descargar el modelo utilizado por el chatbot:

```bash
ollama run llama3.2
```

---

## Clonar el repositorio

```bash
git clone https://github.com/E-SalazarDev/nlp-banking-chatbot.git
cd nlp-banking-chatbot
```

---

## Crear entorno virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configurar Jupyter Notebook (opcional)

Registrar el kernel del entorno virtual:

```bash
python -m ipykernel install --user --name bot-venv --display-name "Python (Bot)"
```

Verificar kernels disponibles:

```bash
jupyter kernelspec list
```

Abrir Jupyter:

```bash
jupyter notebook
```

Seleccionar el kernel:

```text
Python (Bot)
```

---

# Ejecución del proyecto

## 1. Ejecutar chatbot basado en reglas

```bash
python -m tests.pruebas_rule_bot
```

Este script ejecuta múltiples consultas de prueba para validar:

* Detección de intenciones
* Extracción de entidades
* Respuestas predefinidas
* Manejo de fallback

---

## 2. Ejecutar chatbot basado en LLM

```bash
python -m tests.pruebas_llm_bot
```

Este script demuestra:

* Gestión de contexto conversacional
* Preguntas de seguimiento
* Recuperación de entidades entre turnos
* Manejo de cierre de conversación
* Recuperación después de fallback

---

## 3. Ejecutar comparación entre ambos sistemas

```bash
python -m tests.comparacion_bots
```

La salida compara:

* Intención detectada
* Respuesta generada
* Comportamiento del chatbot basado en reglas
* Comportamiento del chatbot basado en LLM

---

# Notebook de la actividad

El notebook utilizado para la documentación y evidencia experimental se encuentra en:

```text
notebooks/actividad3_chatbot.ipynb
```

Este notebook incluye:

* Definición del problema conversacional
* Diseño del flujo conversacional
* Implementación del chatbot basado en reglas
* Implementación del chatbot con LLM
* Pruebas experimentales
* Comparación de resultados
* Análisis técnico
* Conclusiones

```
```
