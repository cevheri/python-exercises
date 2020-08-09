import requests


def recaptcha_check(recaptcha_response):
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    value = {
        'secret': '6LdBO6cZAAAAAKqcPfLfYTVWV91Quo0H2tWBfRrc',
        'response': recaptcha_response
    }
    response = requests.post(verify_url, value)
    result = response.json()
    if result['success'] is True:
        return True
    else:
        return {'status': result['success'], 'reason': result['error-codes']}
