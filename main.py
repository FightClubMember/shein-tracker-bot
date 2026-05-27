from playwright.sync_api import sync_playwright

API_URL = "https://www.sheinindia.in/api/category/sverse-5939-37961?currentPage=1&pageSize=5&format=json"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    # Open SHEIN homepage first
    page.goto("https://www.sheinindia.in/")

    page.wait_for_timeout(5000)

    # Fetch API inside browser session
    response = page.evaluate(f"""
        async () => {{
            const res = await fetch("{API_URL}");

            return await res.text();
        }}
    """)

    print(response[:2000])

    browser.close()
