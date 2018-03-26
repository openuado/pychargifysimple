# -*- coding: utf-8 -*-
"""A module to manage the web part of chargify like delete subscription."""
import mechanicalsoup
from fake_useragent import UserAgent


class ChargifyWeb(object):
    """To interacting with chargify.

    Give the possibility to make few actions the API doesn't provide like the
    subscription delete.
    """

    def __init__(self, user, password, url):
        """To initalize the chargify web class.

        @param user: The id to login
        @type user: str

        @param password: The password
        @type user: str

        @param url: The chargify url
        @type url: str
        """
        self.user = user
        self.password = password
        self.url = url

    def delete_subscription(self, subscription):
        """To delete a subscription.

        @param subscription: The subscription id
        @type param: int
        """
        ua = UserAgent()
        browser = mechanicalsoup.StatefulBrowser(user_agent=ua.chrome)

        browser.open('https://app.chargify.com/login.html')
        browser.select_form('#new_user_session')

        browser['user_session[login]'] = self.user
        browser['user_session[password]'] = self.password
        browser.submit_selected()

        browser.open(
            '{url}/subscriptions/{subscription}/delete'.format(
                url=self.url, subscription=subscription))
        browser.select_form('#delete_subscription_form')
        browser.submit_selected()

        browser.close()
