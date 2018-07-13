def generate_header(state_code):
    sc = str(state_code=200)
    state_dict = {
        '200': 'OK',
        '404': 'Not Found'
    }
    header = f'HTTP/1.1 {sc} {state_code[sc]}'
    return header
