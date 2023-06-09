import os
import time

import pytest


def test_landing(app):
    app.landing.go_to_site()
    app.landing.all_drop_down_xpath.click_btn_by_xpath()
    expected_result = app.allSection.all_menu
    assert expected_result


def testForSearchingForAProduct(app):
    app.landing.go_to_site()
    app.landing.search_for_an_item('VolleyBall')
    expected = app.landing.find_element_by_xpath(app.landing.SEARCH_RESULTS)
    assert expected


def testThatUserIsRedirectedToSignInPage(app):
    app.landing.go_to_site()
    app.landing.sign_in_dropdown_menu_xpath.click_btn_by_xpath()
    expected = app.find_element_by_xpath(app.signIn_up.SIGN_IN_PAGE)
    assert expected


def testSignInOfUser(app):
    phone = os.getenv('PHONE')
    password = os.getenv('PASSWORD')
    app.landing.go_to_site()
    app.signIn_up.sign_in(phone, password)
    assert app.navigationAdmin.get_userName()
