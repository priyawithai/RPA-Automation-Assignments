import pyautogui
import pyperclip
import time

# Step 1: Prepare
print("Starting in 3 seconds...")
time.sleep(3)

# Step 2: Press Windows key to open Start
pyautogui.press('win')
time.sleep(1)

# Step 3: Type search query
search_query = "South Africa vs Australia score"
pyperclip.copy(search_query)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 4: Press Enter to open default browser with Google search
pyautogui.press('enter')
time.sleep(4)  # Wait for the page to load

# Step 5: (Optional) Move mouse to where the score box appears
# This is just to simulate or highlight the score area
pyautogui.moveTo(600, 400)  # Adjust as needed
# Do not click, because the score is visible right on the Google page

print("Score should now be visible on screen.")
