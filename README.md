# Gemini AI Chatbot

A simple command-line AI chatbot built using Python and the Google Gemini API. The chatbot uses the **Gemini 3.5 Flash** model to generate intelligent conversational responses.

## Features

- Interactive command-line chatbot
- Powered by Google Gemini 3.5 Flash
- Maintains conversation context during the session
- Easy to set up and run
- Beginner-friendly project for learning Generative AI APIs

---

## Tech Stack

- Python
- Google Gemini API (Gemini 3.5 Flash)
- Google Gen AI Python SDK

---

## Prerequisites

- Python 3.10 or later
- A Google AI Studio API Key

---

## Step 1: Install the Google Gen AI SDK

Open your terminal and run:

```bash
pip install -U google-genai
```

### Why is this required?

`google-genai` is Google's official Python SDK that allows your Python application to communicate with the Gemini API. It handles authentication, sending requests, and receiving AI-generated responses, so you don't have to manually make HTTP requests.

---

## Step 2: Create a Gemini API Key

1. Visit **Google AI Studio**:
   https://ai.dev

2. Create a new API key.

3. Copy your generated API key.

---

## Step 3: Set the API Key

### Windows (Git Bash)

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

### Windows (Command Prompt)

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### macOS / Linux

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

---

## Step 4: Run the Chatbot

Navigate to the project directory and execute:

```bash
python File_name.py
```

---
