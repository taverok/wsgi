from simple.router import Router
from simple import controller, router


def application(env, start_response):
    router.add('/test', controller.test)

    content, headers, code = response(env, router)

    start_response(Router.code_message(code), list(headers.items()))
    return [content.encode()]


def response(env, router: Router):
    headers = {
        'Content-Type': 'text/html'
    }

    uri = env.get('REQUEST_URI')
    _controller = router.invoke(uri, env.get('REQUEST_METHOD'))

    if not _controller:
        return "Page not found", headers, 404

    _response = _controller(env)
    content, h, code = _response
    headers.update(h)

    return content, headers, code

