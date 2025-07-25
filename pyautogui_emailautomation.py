import pyautogui
import pyperclip
import time

# Step 1: Open Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Step 2: Type the Gmail URL
pyperclip.copy("https://mail.google.com")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(10)  # Wait for Gmail to load

# Step 3: Click "Compose" (adjust based on your screen)
pyautogui.moveTo(100, 240)  # Update this based on your screen
pyautogui.click()
time.sleep(3)

# Step 4: Type recipient
pyperclip.copy("prem.170896@gmail.com")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')  # Move to subject
time.sleep(1)

# Step 5: Type subject
pyperclip.copy("Test Email from PyAutoGUI")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')  # Move to body
time.sleep(1)

# Step 6: Type message
pyperclip.copy("Hi Prem,\n\nThis is an automated email sent using PyAutoGUI.\n\nThanks,\nPriya")
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 7: Send email
pyautogui.hotkey('ctrl', 'enter')

print("✅ Email sent!")
