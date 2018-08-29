# -*- coding: utf-8 -*-
import requests


class Chargify(object):
    """To interacting with API chargify.

    The class to manage the API chargify and manage the API call.
    """
    host = 'chargify.com'

    def __init__(self, api_key, subdomain):
        """To initalize the chargify class.

        @param api_key: The chargify api key
        @type api_key: str

        @param subdomain: The chargify subdomain
        @type subdomain: str
        """
        self.api_key = api_key
        self.subdomain = subdomain
        self.url = '{subdomain}.{host}'.format(
            subdomain=self.subdomain, host=self.host)

    def _call_api(self, path, method, params=None, data=None):
        request = getattr(requests, method)
        url = 'https://{url}/{path}'.format(url=self.url, path=path)
        extra_parameters = {
            'auth': (self.api_key, 'x')
        }

        if data:
            extra_parameters['json'] = data

        if params:
            extra_parameters['params'] = params

        call = request(url, **extra_parameters)

        call.raise_for_status

        return call
