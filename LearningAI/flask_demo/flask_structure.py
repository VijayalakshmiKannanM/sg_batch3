from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)

def fetch_match_updates():
    """Scrape match updates using Playwright."""
    headlines_list = []
    with sync_playwright() as p:
        # Launch browser (headless=False shows the browser; set True to hide)
        browser = p.chromium.launch(headless=True, args=["--start-maximized"])
        page = browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ))

        try:
            page.goto("https://www.espncricinfo.com/search/results?q=South+Africa+vs+Australia", timeout=90000)
            page.wait_for_load_state("load", timeout=90000)
            time.sleep(3)
        except Exception as e:
            browser.close()
            return {"error": f"Failed to load page: {e}"}

        try:
            # Extract headlines
            headlines = page.locator("a:has-text('South Africa')").all_text_contents()
            if not headlines:
                headlines = page.locator("h3, h2").all_text_contents()

            if headlines:
                for h in headlines[:5]:
                    if "South Africa" in h or "Australia" in h:
                        headlines_list.append(h.strip())
        except Exception as e:
            browser.close()
            return {"error": f"Failed to extract data: {e}"}

        browser.close()

    if not headlines_list:
        return {"message": "No relevant headlines found"}
    return {"headlines": headlines_list}


@app.route("/match", methods=["GET"])
def get_match():
    """Flask route to trigger Playwright scraping."""
    print("🔍 Fetching South Africa vs Australia updates...")
    result = fetch_match_updates()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
