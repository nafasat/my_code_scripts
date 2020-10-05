#!/usr/bin/env python3

import requests


def debug_get(session, url, auth=None):
    Response = session.get(url, verify=False, auth=auth)
    print('== [session.get debug] ==================')
    print('cookies:')
    print('--------')
    print(session.cookies.get_dict())
    print('\nrequests headers:')
    print('-----------------')
    print(Response.request.headers)
    print('\nResponse headers:')
    print('-----------------')
    print(Response.headers)
    print('=========================================')
    print(Response.text[:50] + '[...]')
    print(Response.content)
    return Response


session = requests.Session()
# first check page without auth
#response = debug_get(session, url_login)  # failed as expected with .htaccess
# provide credentials to pass .htacess is OK
response = debug_get(session, 'http://10.64.50.252:8080/dashboard.html#upstreams', auth=('UserName', 'Password'))
# retry again to authenticate to the regular web app fails...
#response = debug_get(session, url_login, auth=(USER, PASSW))
