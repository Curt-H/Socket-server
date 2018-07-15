def generate_header(length, state_code=200):
    sc = str(state_code)
    state_dict = {
        '200': 'OK',
        '404': 'Not Found'
    }
    header = f'HTTP/1.1 {sc} {state_dict[sc]}\r\n' \
             f'Content-Length: {length}\r\n' \
             f'Content-Type: text/html\r\n' \
             f'\r\n'
    return header


if __name__ == '__main__':
    pass
