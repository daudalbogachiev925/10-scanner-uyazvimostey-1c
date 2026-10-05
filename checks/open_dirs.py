import requests

def check(base_url):
    issues = []
    for path in ['/base/', '/config/', '/1c/', '/ru_RU/']:
        r = requests.get(base_url + path, timeout=5, allow_redirects=False)
        if r.status_code == 200 and 'Пароль' not in r.text:
            issues.append({'path': path, 'severity': 'high'})
    return issues
