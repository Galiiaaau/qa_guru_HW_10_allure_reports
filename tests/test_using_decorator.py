import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(by.text("Search or jump to...")).click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем отсутствие issue {text}")
def should_not_see_any_issues(text):
    s(by.partial_text(text)).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("Galiiaaau/qa_guru_HW_8_oop")
    go_to_repository("Galiiaaau/qa_guru_HW_8_oop")
    open_issue_tab()
    should_not_see_any_issues("Welcome to issues!")
