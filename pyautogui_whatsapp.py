# Give yourself time to open WhatsApp Desktop manually
import pyautogui
import time 

print("You have 5 seconds to switch to WhatsApp window...")
time.sleep(5)

# Step 1: Click on the Search bar (adjust coordinates if needed)
pyautogui.click(x=357, y=1059)  # Replace with your search bar position
time.sleep(2)
pyautogui.write("whatsapp") # Replace with your search bar position
time.sleep(2)
pyautogui.click(x=457, y=273)
time.sleep(2)



# Step 1: Click on the Search bar (adjust coordinates if needed)
pyautogui.click(x=144, y=152)
time.sleep(2)

# Step 2: Type the contact name
contact_name = "Pooja"
pyautogui.write(contact_name)
time.sleep(2)

pyautogui.click(x=355, y=210)  # Replace with your search bar position
time.sleep(2)





# Step 4: Type a personalized message
message = "I love you d chellakutty pooja, thank you for being with me forever and whatever"
for i in range(1):
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(1)

# Step 5: Press Enter to send
pyautogui.press('enter')

print("Message sent successfully.") 