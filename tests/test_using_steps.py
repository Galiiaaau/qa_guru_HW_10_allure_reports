import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(by.text("Search or jump to...")).click()
        s("#query-builder-test").send_keys("Galiiaaau/qa_guru_HW_8_oop").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("Galiiaaau/qa_guru_HW_8_oop")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем отсутствие issue"):
        s(by.partial_text("Welcome to issues!")).should(be.visible)
