import os
import subprocess
import webbrowser

apps = {
    "brave": "C:/Users/lenovo/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe",
    "opera": "C:/Users/lenovo/AppData/Local/Programs/Opera/launcher.exe",
    "canva": "C:/Users/lenovo/AppData/Local/Programs/Canva/Canva.exe",

    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "vscode": "C:/Users/lenovo/AppData/Local/Programs/Microsoft VS Code/Code.exe",

    "notepad": "notepad.exe",
    "calculator": "calc.exe",

    # 🔥 store apps
    "spotify": "store:spotify",
    "whatsapp": "store:whatsapp",

    # optional fallback
    "chatgpt": "https://chat.openai.com"
}

def open_app(app_name):
    app_name = app_name.lower()

    for key in apps:
        if key in app_name:
            path = apps[key]

            try:
                if path.startswith("http"):
                    webbrowser.open(path)

                elif path.startswith("store:"):
                    app = path.split(":")[1]
                    subprocess.Popen(f"start {app}", shell=True)

                else:
                    subprocess.Popen(f'"{path}"')

                return f"Opening {key}"

            except Exception as e:
                print(e)
                return "Failed to open app"

    return "App not found"

def open_file(file_name):
    search_paths = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents")
    ]

    for path in search_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file_name.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    os.startfile(full_path)
                    return f"Opening {file}"

    return "File not found"