from pathlib import Path
import sys

from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _is_truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def before_all(context):
    context.playwright = sync_playwright().start()


def before_scenario(context, scenario):
    browser_name = context.config.userdata.get("browser", "chromium")
    # Mirror the current pytest setup defaults for better consistency on IMDb.
    headless = _is_truthy(context.config.userdata.get("headless", "false"))
    slow_mo = int(context.config.userdata.get("slow_mo", "300"))

    browser_type = getattr(context.playwright, browser_name)
    context.browser = browser_type.launch(headless=headless, slow_mo=slow_mo)
    context.browser_context = context.browser.new_context(
        viewport={"width": 1440, "height": 900},
        locale="en-US",
    )
    context.page = context.browser_context.new_page()
    context.page.set_default_timeout(10000)
    context.page.set_default_navigation_timeout(20000)
    context.current_scenario = scenario

    context.home_page = None
    context.menu_page = None
    context.title_page = None
    context.photos_page = None
    context.top_box_office_page = None
    context.born_today_page = None
    context.name_search_results_page = None


def after_scenario(context, scenario):
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser_context", None):
        context.browser_context.close()
    if getattr(context, "browser", None):
        context.browser.close()


def after_all(context):
    if getattr(context, "playwright", None):
        context.playwright.stop()
