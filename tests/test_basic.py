from playwright.sync_api import expect

def test_open_imdb(page):
    page.goto("https://www.imdb.com/", wait_until="domcontentloaded")
    expect(page.locator("body")).to_contain_text("IMDb")