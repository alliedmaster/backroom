# Scripts Directory

This directory contains useful Python scripts.

## Mouse Coordinates Display

**File:** `mouse_coordinates.py`

A real-time mouse coordinate display tool that shows the current X and Y position of your mouse cursor on screen.

### Features:
- Real-time coordinate updates (10 times per second)
- Always-on-top window
- Shows current mouse position (X, Y)
- Displays screen resolution
- Clean, modern interface

### Requirements:
- Python 3.6+
- pyautogui library

### Installation:
```bash
pip install -r requirements.txt
```

### Usage:
```bash
python mouse_coordinates.py
```

### How it works:
The script creates a small window that stays on top of other applications and continuously updates to show your current mouse coordinates. Move your mouse around the screen to see the coordinates change in real-time.

### Exit:
Close the window or press Ctrl+C in the terminal to stop the script. 