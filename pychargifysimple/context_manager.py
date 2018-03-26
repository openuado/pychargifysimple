# -*- coding: utf-8 -*-
from contextlib import contextmanager

import mechanicalsoup
from fake_useragent import UserAgent


@contextmanager
def login(user, password):
    """To manage the login."""
    ua = UserAgent()
    browser = mechanicalsoup.StatefulBrowser(user_agent=ua.chrome)

    browser.open('https://app.chargify.com/login.html')
    browser.select_form('#new_user_session')

    browser['user_session[login]'] = user
    browser['user_session[password]'] = password

    browser.submit_selected()
    yield browser
    browser.close()
