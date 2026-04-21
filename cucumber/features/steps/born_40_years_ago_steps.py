from behave import when

from pages.name_search_results_page import NameSearchResultsPage


def _name_search_results_page(context) -> NameSearchResultsPage:
    if context.name_search_results_page is None:
        context.name_search_results_page = NameSearchResultsPage(context.page)
    return context.name_search_results_page


@when("I remove default birthday chip if present")
def step_remove_default_birthday_chip(context):
    _name_search_results_page(context).remove_default_birthday_filter_if_present()


@when("I expand the Birth Date section if needed")
def step_expand_birth_date_section(context):
    _name_search_results_page(context).expand_birth_date_if_needed()


@when("I set From and To birth dates to 40 years ago")
def step_set_birth_dates_to_40_years_ago(context):
    _name_search_results_page(context).set_birth_date_40_years_ago()


@when("I open the first link in the first result description when available")
def step_open_first_link_in_first_result_description(context):
    _name_search_results_page(context).click_first_link_in_first_result_description_if_any()
