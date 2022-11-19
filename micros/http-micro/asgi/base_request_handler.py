from functools import wraps


class BaseRequestHandler:

    def __init__(self):
        self._app_methods = dict()
        self._app_methods['GET'] = dict()
        self._app_methods['POST'] = dict()
        self._app_methods['PUT'] = dict()
        self._app_methods['DELETE'] = dict()


    def get(*args, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            args[0]._app_methods['GET'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def post(*args, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            args[0]._app_methods['POST'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def put(*args, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args):
                return func(*args)

            args[0]._app_methods['PUT'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner

    def delete(*args, **kwargs):
        """decorator method"""

        def inner(func):
            @wraps(func)
            def wrapped_f(*args, **kwargs):
                return func(*args, **kwargs)

            args[0]._app_methods['DELETE'][kwargs['path']] = wrapped_f
            return wrapped_f

        return inner
