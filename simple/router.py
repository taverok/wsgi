import http.client


class Router:
    def __init__(self):
        self.routes = {}

    def add(self, uri, func):
        self.routes.update({uri: func})

    def invoke(self, uri, method):
        route = self.routes.get(uri)

        return route.get('func') if route and method in route.get('methods', []) else None

    def route(self, url, **kwargs):
        def wrapper(func):
            method = kwargs.get('method', ["GET"])
            self.add(url, {'methods': method, 'func': func})

        return wrapper

    @staticmethod
    def code_message(code):
        return "{} {}".format(code, http.client.responses[code])
