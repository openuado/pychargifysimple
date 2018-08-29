# -*- coding: utf-8 -*-
import json

import pytest

from pychargifysimple.subscription import ChargifySubscription


@pytest.fixture
def chargify_subscription():
    """To load the chargify subscription object"""
    chargify_subscription = ChargifySubscription(
        api_key='CH7pFcThu8Mgo9cxos61LOgznzY8haDYKREpXY4o',
        subdomain='example')
    return chargify_subscription


@pytest.fixture
def chargify_subscription_response():
    """Response of a subscription"""
    return json.dumps({
        'subscription': {
            'coupon_uses_allowed': None,
            'reason_code': None,
            'cancellation_method': None,
            'updated_at': u'2018-08-26T13:47:24+02:00',
            'previous_state': u'canceled',
            'referral_code': None,
            'balance_in_cents': 0,
            'current_period_ends_at': u'2019-08-26T13:47:24+02:00',
            'id': 42,
            'payment_collection_method': u'automatic',
            'snap_day': None,
            'product_price_in_cents': 4200,
            'automatically_resume_at': None,
            'total_revenue_in_cents': 4200,
            'signup_payment_id': 42190,
            'state': u'active',
            'current_billing_amount_in_cents': 4200,
            'coupon_use_count': None,
            'cancel_at_end_of_period': False,
            'payment_type': u'credit_card',
        }
    })
