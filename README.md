# 🛡️ Monitor de Uptime con Alertas por Telegram

Este script monitorea el estado de un sitio web y te envía una alerta por Telegram si la página se cae.

## 🚀 Requisitos

- Python 3.8+
- `requests`
- `python-dotenv`

Instala los requisitos con:


pip install -r requirements.txt




⚙️ Configuración

    Crea un archivo .env basado en el config.example.env:

TELEGRAM_TOKEN=tu_token_de_bot
TELEGRAM_CHAT_ID=tu_chat_id
URL_TO_MONITOR=https://tusitio.com
CHECK_INTERVAL_SECONDS=60


 correr el el script:

python3 main.py


🧠 ¿Cómo funciona?

    Envía una petición a la URL cada N segundos.

    Si no recibe respuesta 200, te manda una alerta por Telegram.

    Silencioso si todo está bien (opcionalmente puedes cambiarlo para notificar siempre).

    🛠️ Estructura del proyecto

monitor-web-telegram/
├── main.py
├── .env
├── utils/
│   ├── checker.py
│   ├── notifier.py
│   ├── logger.py
│   └── __init__.py
├── requirements.txt
└── README.md
