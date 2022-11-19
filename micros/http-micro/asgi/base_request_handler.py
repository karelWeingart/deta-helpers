""" BaseRequestHandler class """
from functools import wraps


class BaseRequestHandler:
    """Base request handler contains only decorator methods
    so far and mapping of mapped implemented methods."""

    def __init__(self):
        self._app_methods = {'GET': {}, 'POST': {}, 'PUT': {}, 'DELETE': {}}

    def get(self, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            self._app_methods['GET'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def post(self, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            self._app_methods['POST'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def put(self, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            self._app_methods['PUT'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def delete(self, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args, **kwargs):
                return func(*args, **kwargs)

            self._app_methods['DELETE'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner
