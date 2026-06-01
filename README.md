# Chatbot Bancario: Reglas vs LLM

Este proyecto implementa y compara dos versiones de un chatbot bancario:

## Tecnologías utilizadas

- Python 3.11
- Ollama
- Llama 3.2
- Requests
- Jupyter Notebook
- IPython Kernel

## Estructura del proyecto

```text
Bot/
├── llm_bot/
│   ├── chatbot.py
│   ├── context_manager.py
│   └── prompt_builder.py
│
├── rule_bot/
│   ├── chatbot.py
│   ├── entities.py
│   ├── intents.py
│   └── responses.py
│
├── tests/
│   ├── pruebas_rule_bot.py
│   ├── pruebas_llm_bot.py
│   └── comparacion_bots.py
│
├── notebooks/
│   └── actividad3_chatbot.ipynb
│
├── requirements.txt
└── README.md 


Requisitos previos
- Python 3.11
- Ollama 

Verificar Python:
python --version

Verificar Ollama:
ollama --version 


Instalar modelo LLM
ollama run llama3.2 


Crear entorno virtual
python -m venv .venv 

Activar entorno:
.venv\Scripts\activate 


Instalar dependencias
pip install -r requirements.txt


Registrar kernel para Jupyter
python -m ipykernel install --user --name bot-venv --display-name "Python (Bot)"

Verificar kernels disponibles:
jupyter kernelspec list 

Ejecutar chatbot basado en reglas
python -m tests.pruebas_rule_bot

Ejecutar chatbot con LLM
python -m tests.pruebas_llm_bot

Ejecutar comparación entre ambos sistemas
python -m tests.comparacion_bots 


Ejecutar notebook

Abrir el notebook:
notebooks/actividad3_chatbot.ipynb 

Seleccionar el kernel:
Python (Bot)


