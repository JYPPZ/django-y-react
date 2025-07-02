from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            'status_code': response.status_code,
            'error': {
                'message': 'Se ha producido un error.',
                'details': response.data
            }
        }
        if 'detail' in response.data:
            custom_response['error']['message'] = response.data['detail']
            del custom_response['error']['details']['detail']

        response.data = custom_response

    return response