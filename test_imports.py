import sys
print("Python version:", sys.version)

try:
    import PySide6
    print("PySide6 version:", PySide6.__version__)
except ImportError as e:
    print("PySide6 import failed:", e)

try:
    import darkdetect
    print("darkdetect import successful")
except ImportError as e:
    print("darkdetect import failed:", e)

try:
    import pyperclip
    print("pyperclip import successful")
except ImportError as e:
    print("pyperclip import failed:", e)

try:
    from pynput import keyboard
    print("pynput import successful")
except ImportError as e:
    print("pynput import failed:", e)

try:
    import markdown2
    print("markdown2 import successful")
except ImportError as e:
    print("markdown2 import failed:", e)

try:
    import ollama
    print("ollama import successful")
except ImportError as e:
    print("ollama import failed:", e)

try:
    import openai
    print("openai import successful")
except ImportError as e:
    print("openai import failed:", e)

try:
    import requests
    print("requests import successful")
except ImportError as e:
    print("requests import failed:", e) 