# -*- coding: utf-8 -*-
from pychargifysimple.base import Chargify


class ChargifySubscription(Chargify):
    """To interacting with chargify API subscription.

    The class to manage the API chargify and manage the API call.
    """
    base = 'subscriptions'

    def get_subscription(self, subscription):
        """To read a subscription.

        @param subscription: The subscription id
        @type subscription: int

        @return: The subscription detail
        @rtype : dict
        """
        return self._call_api('{base}/{subscription}.json'.format(
            base=self.base, subscription=subscription), method='get').json()

    def change_next_billing_at(self, subscription, next_billing_at):
        """To change the next billing date of a subscription.

        @param subscription: The subscription id
        @type subscription: int

        @param next_billing_at: The date of the next billing
        @type next_billing_at: `datetime.datetime`

        @return: The subscription detail
        @rtype : dict
        """
        url = '{base}/{subscription}.json'.format(
            base=self.base, subscription=subscription)
        data = {
            'subscription': {
                'next_billing_at': next_billing_at.isoformat()
            }
        }

        return self._call_api(url, 'put', data=data).json()

    def change_expires_at(self, subscription, expires_at):
        """To change the expiration date of a subscription.

        @param subscription: The subscription id
        @type subscription: int

        @param expires_at: The date of the expiration date
        @type expires_at: `datetime.datetime`

        @return: The subscription detail
        @rtype : dict
        """
        url = '{base}/{subscription}.json'.format(
            base=self.base, subscription=subscription)
        data = {
            'subscription': {
                'expires_at': expires_at.isoformat()
            }
        }

        return self._call_api(url, 'put', data=data).json()

    def delete_subscription(self, subscription, customer):
        """To delete a subscription.

        @param subscription: The subscription id
        @type subscription: int

        @param customer: The customer id
        @type customer: int

        @return: The subscription detail
        @rtype : dict
        """
        url = '{base}/{subscription}/purge.json'.format(
            base=self.base, subscription=subscription, customer=customer)
        data = {'ack': customer}

        return self._call_api(url, 'post', params=data).json()
