# reminder.py
"""
Simple JSON-backed reminders. Not a push-notification system — shows reminders in-app.
"""

import json
import os
from datetime import datetime
from typing import List, Dict

REM_FILE = "reminders.json"

def load_reminders() -> List[Dict]:
    if not os.path.exists(REM_FILE):
        return []
    try:
        with open(REM_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_reminders(reminders: List[Dict]):
    with open(REM_FILE, "w") as f:
        json.dump(reminders, f, indent=2)

def add_reminder(text: str, time_str: str):
    reminders = load_reminders()
    reminders.append({"task": text, "time": time_str, "created_at": datetime.now().isoformat()})
    save_reminders(reminders)

def remove_reminder(index: int):
    reminders = load_reminders()
    if 0 <= index < len(reminders):
        reminders.pop(index)
        save_reminders(reminders)
