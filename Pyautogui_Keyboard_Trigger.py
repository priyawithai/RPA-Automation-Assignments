import pyautogui
import time

# Wait time between actions (in seconds)
interval = 240  # 4 minutes

print("Auto activity simulation started. Press Ctrl+C to stop.")

try:
    while True:
        # Press Windows key
        pyautogui.press('win')
        time.sleep(1)  # Small delay between key presses

        # Press Esc to close Start menu
        pyautogui.press('esc')
        print("Simulated activity at:", time.strftime("%H:%M:%S"))

        # Wait for 4 minutes
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nStopped by user.")
