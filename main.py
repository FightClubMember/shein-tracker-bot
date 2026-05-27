from playwright.sync_api import sync_playwright

url = "https://www.sheinindia.in/api/category/sverse-5939-37961?currentPage=1&pageSize=5&format=json"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    response = page.goto(url)

    print("STATUS:", response.status)

    content = page.content()

    print(content[:1000])

    browser.close()
