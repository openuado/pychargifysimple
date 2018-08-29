# -*- coding: utf-8 -*-
"""A module to manage the web part of chargify like delete subscription."""
import logging

from mechanicalsoup.browser import LinkNotFoundError

from pychargifysimple.context_manager import login


logger = logging.getLogger(__name__)


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
        @type password: str

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
        with login(self.user, self.password) as browser:
            browser.open(
                '{url}/subscriptions/{subscription}/delete'.format(
                    url=self.url, subscription=subscription))

            try:
                browser.select_form('#delete_subscription_form')
            except LinkNotFoundError:
                logger.error(
                    'The subscription {subscription} not found'.format(
                        subscription=subscription))
                return

            browser.submit_selected()
