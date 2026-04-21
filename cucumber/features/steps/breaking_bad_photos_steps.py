from behave import then, when

from pages.photos_page import PhotosPage
from pages.title_page import TitlePage


def _title_page(context) -> TitlePage:
    if context.title_page is None:
        context.title_page = TitlePage(context.page)
    return context.title_page


def _photos_page(context) -> PhotosPage:
    if context.photos_page is None:
        context.photos_page = PhotosPage(context.page)
    return context.photos_page


@then("I should be on the Top TV page")
def step_verify_top_tv_page(context):
    assert "toptv" in context.page.url, "Top TV page URL does not contain 'toptv'."


@when("I open the Breaking Bad title page")
def step_open_breaking_bad_title_page(context):
    context.page.get_by_role("link", name="Breaking Bad").first.click()


@when("I open the Photos section")
def step_open_photos_section(context):
    _title_page(context).open_photos()


@when("I open the gallery")
def step_open_gallery(context):
    _photos_page(context).open_gallery()


@when("I open the photo filter prompt")
def step_open_photo_filter_prompt(context):
    _photos_page(context).open_filter_prompt()


@when('I apply person filter "{name}"')
def step_apply_person_filter(context, name):
    _photos_page(context).select_person_filter(name)


@when("I close the photo filter prompt")
def step_close_photo_filter_prompt(context):
    _photos_page(context).close_filter_prompt()


@then('I should see person filter "{name}" applied')
def step_verify_person_filter_applied(context, name):
    assert _photos_page(context).is_person_filter_applied(name)


@when("I open the second filtered image")
def step_open_second_filtered_image(context):
    _photos_page(context).click_second_filtered_image()


@then("I should be on a media viewer page")
def step_verify_media_viewer_page(context):
    assert "/mediaviewer/" in context.page.url, "Did not navigate to media viewer page."
