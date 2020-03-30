# Flask-WebPush

A clean interface to `pywebpush` from Flask. Basically, a very thin wrapper.

## Quickstart

### Instantiation

Instantiate this extension like any other Flask extension:

```python
from flask_pywebpush import WebPush
app = Flask()
push = WebPush(app)
```

Or you may initialize the extension with the Flask instance later:

```python
from flask_pywebpush import WebPush
app = Flask()
push = WebPush()
push.init_app(app)
```


### VAPID keys and sender info

WebPush sender requires a private key and an identification URL to operate. For more information on those values, see [this article on Google Developers](https://developers.google.com/web/fundamentals/push-notifications/subscribing-a-user#how_to_create_application_server_keys).

You may specify these values to the extension by setting the following configuration variables of the Flask instance:

* `WEBPUSH_VAPID_PRIVATE_KEY`
  The application server private key. As with `pywebpush`, it may either be the literal key value (DER representation) or a path to a VAPID EC2 private key PEM file;
* `WEBPUSH_SENDER_INFO`: a URL containing information to contact the notification sender. Commonly a mailto: URL.

Alternatively, you can pass these values on creation of the `WebPush` extension instance or to the `init_app` method later on:

```python
from flask_pywebpush import WebPush
push = WebPush(private_key='some_value',
               sender_info='mailto:admin@server.com')
```

### Notification sending

Assuming you've got the subscription storage done, you may send a notification to a given subscription object like so:

```python
from flask_pywebpush import WebPushException

subscription = {
    'endpoint': '---some-value---',
    'keys': { ... }
}
notification = {
    'title': 'Test',
    'body': 'notification body',
}

try:
    push.send(subscription, notification)
except WebPushException as exc:
    print(exc)
```

You can also pass keyword arguments like `verbose=True` to `.send()`, which will be directly passed to `pywebpush.webpush()`


## Extended Usage

Since this is a wrapper over `pywebpush`, it exposes the main objects of the underlying library, namely, `webpush`, `WebPushException`, `WebPusher`.  
All of them may be directly imported from `flask_pywebpush`.

The `WebPush` extension instance also has a `get_webpusher(subscription)` method, allowing you to get a `pywebpush.WebPusher` instance for a given subscription.

If your usage requires more VAPID claims than simply `{"sub": "sender_info"}`, then you may override the passed claims using the `set_claims` method:

```python
from flask_pywebpush import WebPush
push = WebPush()
push.set_claims({})  # whatever VAPID claims you might need
```

## License

[MIT](https://github.com/illright/flask-webpush/blob/master/LICENSE)
