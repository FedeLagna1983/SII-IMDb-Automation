from behave import then, when

from pages.title_page import TitlePage
from pages.top_box_office_page import TopBoxOfficePage


def _top_box_office_page(context) -> TopBoxOfficePage:
    if context.top_box_office_page is None:
        context.top_box_office_page = TopBoxOfficePage(context.page)
    return context.top_box_office_page


def _title_page(context) -> TitlePage:
    if context.title_page is None:
        context.title_page = TitlePage(context.page)
    return context.title_page


@then("I should be on the Top Box Office page")
def step_verify_top_box_office_page(context):
    assert _top_box_office_page(context).is_open(), "Top Box Office page is not open."


@when("I open the second title from Top Box Office")
def step_open_second_top_box_office_title(context):
    _top_box_office_page(context).open_second_title()


@when("I open the user rating modal")
def step_open_user_rating_modal(context):
    _title_page(context).open_your_rating_modal()


@when("I rate the title with five stars and confirm")
def step_rate_five_stars_and_confirm(context):
    _title_page(context).rate_five_stars_and_confirm()


@then("I should either be asked to sign in or see the rating modal closed")
def step_verify_sign_in_or_closed_modal(context):
    title_page = _title_page(context)
    assert title_page.is_sign_in_required() or title_page.is_rating_modal_closed()
