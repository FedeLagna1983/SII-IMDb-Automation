from behave import then, when

from pages.born_today_page import BornTodayPage


def _born_today_page(context) -> BornTodayPage:
    if context.born_today_page is None:
        context.born_today_page = BornTodayPage(context.page)
    return context.born_today_page


@then("the Born Today date in URL should match today")
def step_verify_born_today_date_matches_today(context):
    _born_today_page(context).validate_born_today_url_matches_today()


@when("I expand the Birthday filter if needed")
def step_expand_birthday_filter(context):
    _born_today_page(context).expand_birthday_if_needed()


@when("I set Birthday filter to yesterday")
def step_set_birthday_filter_to_yesterday(context):
    _born_today_page(context).set_birthday_to_previous_day_from_input()


@when("I open the third person in results")
def step_open_third_person_in_results(context):
    _born_today_page(context).click_third_person()
