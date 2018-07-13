from route import generate_header


def index(request):
    r = request
    header = generate_header()
    body = f'<h1>Welcome!</h1>\n' \
           f'<h2>path: {r.path}</h2>' \
           f'<h2>args: {r.args}</h2>' \
           f'<h2>form: {r.form}</h2>'

    response = header + '\r\n\r\n' + body
    return response


def error(request):
    r = request
    header = generate_header(404)
    body = f'<h1>404 NOT FOUND</h1>\n' \
           f'<h2>the path [{r.path}] you required is not found</h2>'
    response = header + '\r\n\r\n' + body
    return response


def route_public(path):
    route_dict = {
        '/': index,
    }
    return route_dict.get(path, error)
