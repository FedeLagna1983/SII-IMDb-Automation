from behave import then, when


@when('I search for "{query}"')
def step_search_query(context, query):
    context.page.locator('input[data-testid="suggestion-search"]').fill(query)
    context.page.keyboard.press("Enter")


@when("I open the Nicolas Cage profile")
def step_open_nicolas_cage_profile(context):
    context.page.locator('a[href*="/name/nm0000115"]').first.click()


@when("I scroll to the Credits section")
def step_scroll_to_credits_section(context):
    context.page.locator("#credits").scroll_into_view_if_needed()


@when("I expand the Upcoming section if needed")
def step_expand_upcoming_if_needed(context):
    upcoming_expand = context.page.locator('label[aria-label="Expand Upcoming"]')
    if upcoming_expand.count() > 0 and upcoming_expand.first.is_visible():
        upcoming_expand.first.click()


@when('I open the first upcoming title with status "{status}"')
def step_open_first_upcoming_title_by_status(context, status):
    items = context.page.locator("li.ipc-metadata-list-summary-item")
    total_items = items.count()

    clicked = False
    for index in range(total_items):
        item = items.nth(index)
        status_tag = item.locator("a", has_text=status)
        if status_tag.count() > 0:
            item.locator('a[href*="/title/"]').first.click()
            clicked = True
            break

    assert clicked, f'No upcoming title with status "{status}" was found.'


@then("I should be navigated to a title page")
def step_verify_title_navigation(context):
    assert "/title/" in context.page.url, "Did not navigate to a title page."
