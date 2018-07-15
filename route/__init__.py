def generate_header(state_code=200):
    sc = str(state_code)
    state_dict = {
        '200': 'OK',
        '404': 'Not Found'
    }
    header = f'HTTP/1.1 {sc} {state_dict[sc]}\r\n' \
             f'Content-Type:text/html\r\n'
    return header
