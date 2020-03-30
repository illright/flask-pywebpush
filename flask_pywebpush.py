'''flask_pywebpush – A clean interface to pywebpush from Flask.'''

import json
import typing as t

from flask import Flask, current_app
from pywebpush import webpush, WebPusher, WebPushException

__all__ = ['WebPush', 'WebPushException', 'webpush', 'WebPusher']


JSONType = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]


class WebPush:
    '''The extension class. Has a method for sending notifications.'''
    def __init__(self,
                 app: Flask = None,
                 private_key: str = None,
                 sender_info: str = None):
        if app is not None:
            self.init_app(app, private_key, sender_info)

    @staticmethod
    def init_app(app: Flask, private_key: str = None, sender_info: str = None):
        '''Initialize from the application object after creation.'''
        app.config.setdefault('WEBPUSH_VAPID_PRIVATE_KEY', private_key)
        app.config.setdefault('WEBPUSH_SENDER_INFO', sender_info)
        app.config.setdefault('WEBPUSH_VAPID_CLAIMS', {'sub': app.config['WEBPUSH_SENDER_INFO']})

    @staticmethod
    def set_claims(claims):
        '''Override the default VAPID claims.'''
        current_app.config['WEBPUSH_VAPID_CLAIMS'] = claims

    @staticmethod
    def send(subscription: dict, notification: JSONType, **kwargs):
        '''Send a notification payload to a given subscription.'''
        webpush(subscription,
                json.dumps(notification),
                vapid_private_key=current_app.config['WEBPUSH_VAPID_PRIVATE_KEY'],
                vapid_claims=current_app.config['WEBPUSH_VAPID_CLAIMS'],
                **kwargs)

    @staticmethod
    def get_webpusher(subscription):
        '''Return a WebPusher instance for a given subscription.'''
        return WebPusher(subscription)
