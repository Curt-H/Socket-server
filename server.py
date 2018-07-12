from util import log
from socket import socket


def recieve_request(connection):
    request = b''
    buffer_size = 1024
    # start to read the request
    log('Recieving request...')
    while True:
        r = connection.recv(buffer_size)
        request += r
        if len(r) < buffer_size:
            log('All recieved')
            return request.decode(encoding='utf-8')


def app(host, port):
    with socket() as s:
        # bind host and port and listen
        s.bind((host, port))
        s.listen()
        log(f'Start listening @ http://{host}:{port}')
        log(f'You can access it at http://localhost')

        while True:
            # Accept the client connection
            client, address = s.accept()
            log(f'Connected by ({address})')

            with client:
                request = recieve_request(client)
                log(request)


if __name__ == '__main__':
    config = {
        'host': '0.0.0.0',
        'port': 80,
    }

    app(**config)
