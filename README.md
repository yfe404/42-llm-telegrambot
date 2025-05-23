# 42 LLM Telegram Bot

This project integrates a Telegram bot with a Flask-based API wrapper to interact with the 42 Intra API, enhanced by LLMs and LangGraph for structured agent behavior.

---

## Project Structure

```text
.
├── compose.yml       # Docker Compose setup
├── .env                     # Environment variables file
├── telegram-bot/            # Telegram bot implementation
├── 42-api-wrapper/          # Flask API wrapper for 42 Intra
├── env_example              # Template for .env configuration
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yfe404/42-llm-telegrambot.git
cd 42-llm-telegrambot
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory or copy from `env_example`:
(See https://api.intra.42.fr/apidoc/guides/getting_started to get your client ID and client SECRET).

```env
# Telegram & OpenAI 
TELEGRAM_TOKEN=your-telegram-bot-token
OPENAI_API_KEY=sk-your-openai-key

# Flask API
FLASK_ENV=production
CLIENT_ID=your-42-client-id
CLIENT_SECRET=your-42-client-secret
TOK_URL=https://api.intra.42.fr/v2/oauth/token
API_URL=https://api.intra.42.fr/v2
SCOPES=public
```

### 3. Build and Run with Docker Compose

```bash
docker compose up --build
```

The services will be built and started. The Telegram bot will be able to access the Flask API and respond using OpenAI's LLM capabilities.

---

## Component Overview

### Telegram Bot (`telegram-bot/`)

* Uses LangChain and LangGraph for managing conversational agents.
* Integrates with OpenAI's GPT model (GPT-4o by default).
* Fetches user information and connected user data from the 42 API wrapper.

### API Wrapper (`42-api-wrapper/`)

* Lightweight Flask API that handles authentication and data fetching from 42 Intra.
* Exposes endpoints used by the Telegram bot.

---

## Future Enhancements

* Add persistent memory or storage for user sessions.
* Support for multiple Telegram users and roles.
* Expand 42 API coverage and functionality.
* Support alternative models

---

## Acknowledgements

Thanks to hivehelsinki/42api-lib for providing the foundation for the 42 API integration.

## License and Disclaimer

This project is intended for educational and experimental purposes. Please ensure that you are compliant with 42 Intra's API usage guidelines and handle all credentials securely.

For any issues or contributions, please open a pull request or issue on the repository.

