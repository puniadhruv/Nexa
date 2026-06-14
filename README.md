# Nexa AI Voice Assistant

## Overview

Nexa is a Python-based AI Voice Assistant designed to perform voice-controlled tasks, answer questions using Large Language Models (LLMs), automate desktop actions, and assist users through natural language conversations.

The project integrates speech recognition, text-to-speech, AI-powered responses, web automation, and application control into a single intelligent assistant.

---

## Features

### Voice Interaction

* Real-time voice command recognition
* Speech-to-text processing
* Text-to-speech responses
* Hands-free interaction

### AI-Powered Responses

* Integration with Ollama Local LLMs
* Natural language conversations
* Intelligent command understanding
* Context-aware responses

### Web Automation

* Open Google
* Open YouTube
* Open ChatGPT
* Google Search
* YouTube Search

### Application Control

* Open VS Code
* Open Notepad
* Open Calculator
* Open WhatsApp
* Open Spotify
* Open Camera

### Entertainment

* Play songs directly from YouTube
* Search music using voice commands

### WhatsApp Automation

* Open WhatsApp Desktop
* Search contacts automatically
* Send messages using voice commands

### AI Coding Assistant

* Generate Python code using Ollama
* Save generated code automatically
* Open generated files in VS Code
* Run generated code
* Auto-debug generated code using LLM

---

## Tech Stack

### Programming Language

* Python

### AI & LLM

* Ollama
* Mistral / Llama Models

### Speech Processing

* SpeechRecognition
* Whisper

### Text To Speech

* pyttsx3

### Automation

* PyAutoGUI
* Pyperclip

### Web Integration

* PyWhatKit
* WebBrowser

### Audio Processing

* SoundDevice
* SciPy

---

## Project Structure

```text
Nexa-AI-Assistant/
│
├── assistant.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── generated_projects/
│   ├── calculator.py
│   └── ...
│
└── assets/
```

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama:

https://ollama.com

Pull a model:

```bash
ollama pull mistral
```

or

```bash
ollama pull llama3
```

---

## Running Nexa

Start Ollama first:

```bash
ollama serve
```

Then run Nexa:

```bash
python assistant.py
```

---

## Example Commands

### Web Commands

* Open Google
* Open YouTube
* Search Python tutorials
* Search AI projects

### Application Commands

* Open VS Code
* Open Calculator
* Open Notepad
* Open WhatsApp

### Entertainment

* Play Believer
* Play Punjabi songs

### Coding Commands

* Write Python calculator code
* Write and run a calculator program
* Generate a Python chatbot
* Create a to-do app in Python

### General AI Queries

* Explain Machine Learning
* What is Deep Learning?
* Tell me about Python

---

## Future Enhancements

* Wake Word Detection (Nexa)
* Memory System
* Personal Knowledge Base
* Smart File Management
* Email Automation
* AI Agent Capabilities
* Multi-Agent System
* Jarvis-Style GUI
* Autonomous Task Execution
* Local Vector Database
* RAG Integration

---

## Author

Dhruv

Machine Learning Engineer | AI Developer | Google Student Ambassador

GitHub:
https://github.com/puniadhruv

---

## License

This project is open-source and available under the MIT License.
