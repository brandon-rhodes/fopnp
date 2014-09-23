"""Check that a server works.

Run the service under test (which should be another Python module in
this directory) like:

$ gunicorn -b '' timeapp_raw:app

"""
import requests

def display(r):
    print((r.status_code, r.headers['Content-Type'], r.text))

if __name__ == '__main__':

    # Wrong method

    r = requests.post('http://localhost:8000/')
    display(r)
    assert r.status_code == 501

    # Different hostnames

    r = requests.get('http://localhost:8000/')
    display(r)
    assert r.status_code == 200

    r = requests.get('http://127.0.0.1:8000/')
    display(r)
    assert r.status_code == 200

    r = requests.get('http://127.0.0.2:8000/')
    display(r)
    assert r.status_code == 404

    # Different paths

    r = requests.get('http://127.0.0.1:8000/foo')
    display(r)
    assert r.status_code == 404

    r = requests.get('http://127.0.0.1:8000/foo/')
    display(r)
    assert r.status_code == 404

    r = requests.get('http://127.0.0.1:8000/?abc=123')
    display(r)
    assert r.status_code == 200
