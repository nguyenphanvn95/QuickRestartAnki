import os
import sys
import json
from aqt import mw
from aqt.qt import QAction, QKeySequence
from aqt.gui_hooks import main_window_did_init

addon_path = os.path.dirname(__file__)
config_path = os.path.join(addon_path, "config.json")
default_config = {
    "shortcut": "Alt+Shift+F4"
}

def load_config():
    if not os.path.exists(config_path):
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default_config

def restart_anki():
    mw.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def setup_restart_menu():
    config = load_config()
    shortcut = config.get("shortcut", "Alt+Shift+F4")

    # Xóa menu cũ nếu tồn tại
    for action in mw.form.menuTools.actions():
        if action.text() == "Restart Anki":
            mw.form.menuTools.removeAction(action)

    action = QAction("🔄Restart Anki", mw)
    action.setShortcut(QKeySequence(shortcut))
    action.triggered.connect(restart_anki)

    mw.form.menuTools.addAction(action)
    mw.addAction(action)  # <-- Đăng ký vào hệ thống global shortcut của Anki

main_window_did_init.append(setup_restart_menu)
