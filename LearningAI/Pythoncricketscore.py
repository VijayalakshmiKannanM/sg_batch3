# open_and_click_search.py
import webbrowser
import pyautogui
import time
import os

# Config
QUERY = "southafrica vs australia score"
FIRST_LINK_IMAGE = "first_link.png"   # put your captured image here (optional but recommended)
SEARCH_TIMEOUT = 15                   # seconds to wait for page to load
FIND_RETRIES = 10                     # how many times to try image matching
RETRY_DELAY = 1.0                     # seconds between attempts
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True             # move mouse to top-left to abort

def open_search(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)   # opens default browser to the search URL

def click_by_image(image_path, retries=FIND_RETRIES, delay=RETRY_DELAY, confidence=0.8):
    """Try to locate image on screen and click its center."""
    for i in range(retries):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            x, y = pyautogui.center(location)
            pyautogui.moveTo(x, y, duration=0.4)
            pyautogui.click()
            return True
        time.sleep(delay)
    return False

def fallback_keyboard_open_first_result():
    """
    Fallback method using keyboard navigation.
    This sequence may need adjusting depending on browser and extensions.
    """
    # Give the browser focus and let it settle
    time.sleep(0.5)
    # Focus the page and start tabbing — number of tabs may vary by browser/region
    # We'll try a few different safe sequences:
    # 1) Press 'tab' repeatedly then 'enter' (may focus first result)
    for tries in (5, 7, 9):
        pyautogui.press('home')  # ensure top of page, not strictly needed but safe
        time.sleep(0.3)
        pyautogui.press('tab', presses=tries, interval=0.15)
        time.sleep(0.3)
        pyautogui.press('enter')
        # Wait a moment to see if navigation happened; check for URL change by small pause
        time.sleep(2)
        # If page changed (title bar or new UI) user can observe; we return True assuming success
        # There's no reliable cross-platform check without browser automation (Selenium).
        return True
    return False

def main():
    print("Opening browser and searching for:", QUERY)
    open_search(QUERY)
    print("Waiting for search results to load...")
    time.sleep(SEARCH_TIMEOUT)

    # Try image-click method if image exists
    if os.path.exists(FIRST_LINK_IMAGE):
        print("Trying to find and click the first link using image:", FIRST_LINK_IMAGE)
        found = click_by_image(FIRST_LINK_IMAGE)
        if found:
            print("Clicked the first link (image match).")
            return
        else:
            print("Image not found on screen. Falling back to keyboard method.")
    else:
        print("No image file found. Using keyboard fallback to open the first link.")

    # Fallback to keyboard-based attempt
    success = fallback_keyboard_open_first_result()
    if success:
        print("Fallback keyboard sequence executed. Verify a page opened.")
    else:
        print("Fallback failed. Consider creating a better reference image or using Selenium for robust automation.")

if __name__ == "__main__":
    main()
