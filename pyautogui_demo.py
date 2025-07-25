import pyautogui
import time

#mouse operation
'''
pyautogui.click(100,100)
time.sleep(2)
pyautogui.rightClick(100,100)
time.sleep(2)
pyautogui.leftClick(839,975)
time.sleep(2)
pyautogui.doubleClick(100,100)
time.sleep(2)
pyautogui.drag(100,100,200,200)
time.sleep(2)
pyautogui.scrollDown(500)
'''

#Keyboard Opeartion

time.sleep(2)

pyautogui.click(674,288)

time.sleep(3)

pyautogui.typewrite("priya")

pyautogui.write(" python rpa_demo.py")

pyautogui.press('enter')



pyautogui.click(674,288)
time.sleep(2)
pyautogui.hotkey("ctrl","a")            #(tab,altkey,ctrl+c,shift+ etc..)


#image operation
#location = pyautogui.locateOnScreen("C:\\Users\\priya\\OneDrive\\Desktop\\pyautogui\\copilot.png", confidence=0.8)
location = pyautogui.locateOnScreen("priya.png",confidence=0.4)
#location = pyautogui.locateOnScreen(r"C:\Users\priya\OneDrive\Desktop\pyautogui\copilot.png",confidence=0.8)
print(location)


pyautogui.click(pyautogui.center(location))

print(pyautogui.size())
ss = pyautogui.screenshot()
ss.save("demo.png")