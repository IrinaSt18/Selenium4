from testpage import OperationHelper
import logging
import yaml
import time



with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    name = data["login"]
    paswd = data["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == "401", "Test_1 FAIL"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(paswd)
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_profile_name() == f"Hello, {name}", "Test_2 FAIL"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.click_new_post_btn()
    testpage.create_post_title("Sea")
    testpage.create_post_description("Mountains")
    testpage.create_post_content("The mountains are wonderful")
    testpage.click_create_post_button()
    time.sleep(5)
    assert testpage.get_created_post_title() == "Sea", "Test_3 FAIL"




def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationHelper(browser)
    testpage.contact_us_btn()
    testpage.contact_us_name("Irina")
    testpage.contact_us_email("Irina@gmail.com")
    testpage.contact_us_content("Cats are funny")
    testpage.click_contact_us_btn()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"