from django.urls import reverse
from playwright.sync_api import Page, expect

def test_display_empty_list_on_first_load(live_server, page: Page):
    url = reverse_url(live_server, "index")

    page.goto(url)
    page.wait_for_selector("text=Nothing to see")


def reverse_url(
    live_server, viewname, urlconf=None, args=None, kwargs=None, current_app=None
):
    end = reverse(viewname, urlconf, args, kwargs, current_app)
    return f"{live_server.url}{end}"

def test_create_todo_item_removes_nothing_to_see(live_server, page: Page):
    url = reverse_url(live_server, "index")

    page.goto(url)
    page.wait_for_selector("text=Nothing to see")
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("a random task")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("Nothing to see...")).to_be_hidden()

def test_create_todo_item_adds_item_to_list(live_server, page: Page):
    url = reverse_url(live_server, "index")

    page.goto(url)
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("Learn Django")
    page.get_by_role("button", name="Add").click()
    page.wait_for_selector("text=Learn Django")

def test_create_todo_item_clear_form_after_submission(live_server, page: Page):
    url = reverse_url(live_server, "index")

    page.goto(url)
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("debug")
    page.get_by_role("button", name="Add").click()

    expect(page.get_by_label("Title:")).to_be_empty()

def test_display_one_item_on_first_load(live_server, page: Page):
    TodoItem.objects.create(title="Foo")
    page.goto(reverse_url(live_server, "index"))
    page.wait_for_selector("text=Foo")  
    expect(page.get_by_text("Nothing to see here...")).to_be_hidden()