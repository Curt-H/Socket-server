from route import generate_header
from template import Template


def index(request):
    r = request
    body = Template.render('index.html', r=r)
    header = generate_header(len(body))

    response = header + body
    return response


def error(request):
    r = request
    body = Template.render('error.html', r=r)
    header = generate_header(len(body), 404)

    response = header + body
    return response


def route_public(path):
    route_dict = {
        '/': index,
    }
    return route_dict.get(path, error)
