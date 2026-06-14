import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
import time
import pyautogui
import pyperclip
import ollama
import subprocess
import pathlib
import sys

# 🔊 Voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

# 🎤 Better voice input (LIVE mic)
def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            command = recognizer.recognize_google(audio, language="en-IN")
            command = command.lower()
            print("🗣️ You said:", command)
            return command

        except sr.UnknownValueError:
            print("❌ Could not understand")
            return ""

        except sr.WaitTimeoutError:
            print("⌛ Timeout")
            return ""

# 🧠 Ollama LLM
def get_smart_response(prompt):
    try:
        system_prompt = """
You are Nexa AI Assistant.

Convert user requests into these commands:

open_google
open_youtube
open_chatgpt
open_whatsapp
open_calculator
open_notepad
open_vscode
open_spotify
open_camera

play_song:<song>

search_google:<query>
search_youtube:<query>

# =========================
# CODING COMMANDS
# =========================

If user says:
write code for <requirement>

Return ONLY:

generate_code:<requirement>

Examples:

User: write code for calculator
Assistant: generate_code:calculator

User: write code for snake game
Assistant: generate_code:snake game

User: create a flask website
Assistant: generate_code:flask website

User: make a python chatbot
Assistant: generate_code:python chatbot


If user says:
write and run code for <requirement>

Return ONLY:

run_code:<requirement>

Examples:

User: write and run calculator code
Assistant: run_code:calculator

User: write and run a tic tac toe game
Assistant: run_code:tic tac toe game


If user says:

write code for anything

Return:

generate_code:<requirement>

If user says:

write and run code for anything

Return:

run_code:<requirement>

Return only one command.

run_code:<requirement>

Never return multiple commands.
Never return explanations.
Never return more than one line.


# =========================
# INTERNET SEARCH
# =========================

For any request involving:
- search
- find
- look up
- tell me about
- who is
- what is
- latest news
- information about

Return:

search_google:<query>

Examples:

search_google:python tutorial
search_google:latest ai news
search_google:who is elon musk


# =========================
# WHATSAPP
# =========================

send_whatsapp:<name>:<message>

Example:

send_whatsapp:vinay:how are you


# =========================
# NORMAL CHAT
# =========================

Otherwise reply normally in a short helpful way.

IMPORTANT:
- Return ONLY the command.
- Never explain.
- Never give steps.
- Never use markdown.
- Never use ```python.
- Never add examples in output.
- Never add extra text.
"""

        response = ollama.chat(
            model="mistral",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response['message']['content'].strip()

    except Exception as e:
        print("❌ Ollama Error:", e)
        return "Something went wrong"

# 📲 WhatsApp automation
def send_whatsapp(contact, message):
    try:
        os.system("start whatsapp://")
        speak("Opening WhatsApp")
        time.sleep(5)

        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)

        pyperclip.copy(contact)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        time.sleep(1)

        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        speak("Message sent")

    except Exception as e:
        print("❌ WhatsApp Error:", e)
        speak("Failed to send message")

# Save Generated code
def save_generated_code(response):
    try:
        lines = response.split("\n")

        filename = lines[0].replace("write_code:", "").strip()

        code = "\n".join(lines[1:])

        os.makedirs("generated_projects", exist_ok=True)

        filepath = os.path.join("generated_projects", filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)

        speak(f"Code saved successfully in {filename}")

        print(f"✅ Saved: {filepath}")

    except Exception as e:
        print("❌ Save Error:", e)

# Open VS code
def open_vscode_project(filepath):
    try:
        os.system(f'code "{filepath}"')
        print("✅ VS Code Opened")
    except Exception as e:
        print("❌ VS Code Error:", e)

# Run Pyhton Code
def run_python_file(filepath):
    try:
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True
        )

        return result.stdout, result.stderr

    except Exception as e:
        return "", str(e)

# Fix Code Using Ollama
def fix_code_with_ollama(code, error):
    prompt = f"""
You are an expert Python developer.

Fix this code.

ERROR:
{error}

CODE:
{code}

Return ONLY corrected Python code.
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]

# Generate and Run Updated code
def generate_and_run(requirement):

    speak(f"Generating {requirement}")

    prompt = f"""
Write complete Python code for:
{requirement}

Return only code.
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    code = response["message"]["content"]

    os.makedirs("generated_projects", exist_ok=True)

    filename = f"generated_projects/{requirement.replace(' ','_')}.py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    open_vscode_project(filename)

    speak("Running code")

    output, error = run_python_file(filename)

    if error:

        speak("Error detected. Fixing.")

        fixed_code = fix_code_with_ollama(code, error)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        output, error = run_python_file(filename)

        if error:
            speak("Still getting errors")
            print(error)
        else:
            speak("Code fixed and running")

    else:
        speak("Code executed successfully")

    print(output)

# Helper to generate python code (used by run_code handler)
def generate_python_code(requirement):

    prompt = f"""
Write complete Python code for:

{requirement}

Return only code.
No markdown.
No explanation.
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response["message"]["content"]
                
# ⚙️ Action handler
def respond_and_act(command):
    result = get_smart_response(command)
    print("🧠:", result)

    if result == "open_google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif result == "open_youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif result.startswith("play_song:"):
        song = result.split(":")[1]
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        
    elif result == "open_chatgpt":
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")    

    elif result == "open_vscode":
        speak("Opening VS Code")
        os.system("code")
    
    elif result.startswith("search_google:"):
        query = result.split(":", 1)[1]
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif result.startswith("send_whatsapp:"):
        parts = result.split(":")
        if len(parts) >= 3:
            send_whatsapp(parts[1], parts[2])
        else:
            speak("Invalid command")

    elif result.startswith("generate_code:"):

        requirement = result.split(":")[1].split("\n")[0].strip()

        speak(f"Generating {requirement} code")

        code_prompt = f"""
Write complete Python code for:
{requirement}

Return only code.
No explanation.
"""

        code_response = ollama.chat(
         model="mistral",
            messages=[
                {"role": "user", "content": code_prompt}
            ]
        )

        code = code_response["message"]["content"]

        os.makedirs("generated_projects", exist_ok=True)

        filename = f"generated_projects/{requirement.replace(' ','_')}.py"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        speak("Code generated successfully")

        print(f"Saved: {filename}")
    
    elif result.startswith("run_code:"):

        requirement = result.split(":")[1].strip()

        code = generate_python_code(requirement)

        os.makedirs("generated_projects", exist_ok=True)

        filename = f"generated_projects/{requirement}.py"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"✅ Saved: {filename}")

        os.system(f'code "{filename}"')

        speak("Running code")

        for attempt in range(3):

            execution = subprocess.run(
                [sys.executable, filename],
                capture_output=True,
                text=True
            )

            if execution.returncode == 0:

                print("✅ Success")
                print(execution.stdout)

                speak("Code executed successfully")

                break

            error = execution.stderr

            print(error)

            fix_prompt = f"""
Fix this Python code.

CODE:
{code}

ERROR:
{error}

Return only corrected Python code.
"""

            response = ollama.chat(
                model="mistral",
                messages=[
                    {"role": "user", "content": fix_prompt}
                ]
            )

            code = response["message"]["content"]

            with open(filename, "w", encoding="utf-8") as f:
                f.write(code)

        print("🏁 Finished")
    
    elif result.startswith("run_code:"):

        requirement = result.replace(
        "run_code:",
        ""
        ).strip()

        generate_and_run(requirement) 
    else:
        speak(result)

# 🚀 MAIN LOOP
def main():
    speak("Hello, I am Nexo. How can I help you?")

    while True:
        command = listen_command()
        if command:
            respond_and_act(command)

if __name__ == "__main__":
    main()