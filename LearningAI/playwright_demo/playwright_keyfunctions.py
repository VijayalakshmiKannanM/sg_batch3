# sa_vs_aus_update_fixed.py

from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        page = browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ))

        print("Opening ESPNcricinfo...")
        try:
            page.goto("https://www.espncricinfo.com/search/results?q=South+Africa+vs+Australia", timeout=90000)
            page.wait_for_load_state("load", timeout=90000)
            time.sleep(3)
        except Exception as e:
            print("⚠️ Could not fully load page:", e)

        print("\nFetching match updates...\n")

        try:
            headlines = page.locator("a:has-text('South Africa')").all_text_contents()
            if not headlines:
                headlines = page.locator("h3, h2").all_text_contents()
            
            if headlines:
                print("Top Updates / Headlines:\n")
                for h in headlines[:5]:
                    if "South Africa" in h or "Australia" in h:
                        print("-", h.strip())
            else:
                print("⚠️ No match headlines found. Try scrolling in the open browser window.")
        except Exception as e:
            print("❌ Error while reading page:", e)

        try:
            print("\n✅ Done. You can scroll in the browser to see full updates.")
            time.sleep(10)  # wait before closing
        finally:
            if browser.is_connected():
                browser.close()

if __name__ == "__main__":
    main()
