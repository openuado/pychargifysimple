# -*- coding: utf-8 -*-
import datetime
import json

import httpretty


@httpretty.activate
def test_get_subscription(
        chargify_subscription, chargify_subscription_response):
    httpretty.register_uri(
        httpretty.GET, 'https://example.chargify.com/subscriptions/42.json',
        body=json.dumps(chargify_subscription_response),
        content_type='application/json')
    assert chargify_subscription.get_subscription(
        42) == chargify_subscription_response


@httpretty.activate
def test_next_billing_at(
        chargify_subscription, chargify_subscription_response):
    httpretty.register_uri(
        httpretty.PUT, 'https://example.chargify.com/subscriptions/42.json',
        body=json.dumps(chargify_subscription_response),
        content_type='application/json')
    assert chargify_subscription.change_next_billing_at(
        42, datetime.datetime.now()) == chargify_subscription_response


@httpretty.activate
def test_expires_at(
        chargify_subscription, chargify_subscription_response):
    httpretty.register_uri(
        httpretty.PUT, 'https://example.chargify.com/subscriptions/42.json',
        body=json.dumps(chargify_subscription_response),
        content_type='application/json')
    assert chargify_subscription.change_expires_at(
        42, datetime.datetime.now()) == chargify_subscription_response


@httpretty.activate
def test_delete_subscription(
        chargify_subscription, chargify_subscription_response):
    httpretty.register_uri(
        httpretty.POST,
        'https://example.chargify.com/subscriptions/42/purge.json?ack=42',
        body=json.dumps(chargify_subscription_response),
        content_type='application/json')
    assert chargify_subscription.delete_subscription(
        42, 42) == chargify_subscription_response
