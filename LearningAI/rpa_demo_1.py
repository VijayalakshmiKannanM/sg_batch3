import pyautogui
import time


# mouse action
pyautogui.click(100,100)
time.sleep(2)
pyautogui.rightClick(100,100)
time.sleep(4)
pyautogui.click(2324,889)
time.sleep(4)

x,y=pyautogui.position()
print(f'x:{x},Y:{y}')

pyautogui.scroll(500)
pyautogui.rightClick(100,100)

time.sleep(2)
#location=pyautogui.locateOnScreen("pic.png",confidence=0.8)

try:
    location = pyautogui.locateOnScreen("pic.png", confidence=0.8)
    if location:
        print("Found image at:", location)
        pyautogui.click(location)
    else:
        print("Image not found on screen.")
except pyautogui.ImageNotFoundException:
    print("Image not found! Check visibility, scaling, and file path.")

pyautogui.doubleClick(2324,889)

pyautogui.scroll(500)

print(pyautogui.size())

ss=pyautogui.screenshot()
ss.save("demo.png")
print("image saved")

print("Screenshot test starting...")
img = pyautogui.screenshot()
img.save("testshot.png")
print("Screenshot saved successfully.")