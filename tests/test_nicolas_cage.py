from pages.home_page import HomePage


def test_nicolas_cage_upcoming_completed(page):
    home = HomePage(page)

    home.open()

    # Search Nicolas Cage
    page.locator('input[data-testid="suggestion-search"]').fill("Nicolas Cage")
    page.keyboard.press("Enter")

    # Open Nicolas Cage profile
    page.locator('a[href*="/name/nm0000115"]').first.click()

    # Go to Credits section
    page.locator("#credits").scroll_into_view_if_needed()

    # Expand Upcoming only if collapsed
    upcoming_expand = page.locator('label[aria-label="Expand Upcoming"]')
    if upcoming_expand.count() > 0 and upcoming_expand.first.is_visible():
        upcoming_expand.first.click()

    # Find first item with Completed tag and click its title
    items = page.locator("li.ipc-metadata-list-summary-item")
    total_items = items.count()

    clicked = False

    for index in range(total_items):
        item = items.nth(index)

        completed_tag = item.locator("a", has_text="Completed")
        if completed_tag.count() > 0:
            item.locator('a[href*="/title/"]').first.click()
            clicked = True
            break

    assert clicked, "No upcoming title with Completed tag was found."
    assert "/title/" in page.url, "Did not navigate to a title page."