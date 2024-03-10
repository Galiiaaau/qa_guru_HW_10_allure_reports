import allure


def test_all_labels():
    allure.dynamic.title("Тестирование отсутствия issues в Github")
    allure.dynamic.suite("#777")
    allure.dynamic.sub_suite("#77")
    allure.dynamic.link("https://github.com")
    allure.dynamic.epic("qaguru")
    allure.dynamic.severity("major")
    allure.dynamic.parent_suite("parent-suite")
    allure.dynamic.tag("web")
    allure.dynamic.description("Тестирование issues")
    allure.dynamic.description_html("<h1>Тестирование issues</h1>")
    allure.dynamic.feature("feature")
    allure.dynamic.id(777)
    allure.dynamic.issue("#7")
    allure.dynamic.label("owner", "Galiiaaau")