#!/usr/bin/env python3
"""
Simple Mouse Coordinates Script
Prints mouse coordinates to terminal as you move the mouse
"""

import pyautogui
import time

def main():
    """Main function to display mouse coordinates"""
    print("Mouse Coordinates Display")
    print("Move your mouse around to see coordinates")
    print("Press Ctrl+C to stop")
    print("-" * 30)
    
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            
            # Clear the line and print coordinates
            print(f"\rMouse Position: X: {x:4d}, Y: {y:4d}", end="", flush=True)
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\nScript stopped by user")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 