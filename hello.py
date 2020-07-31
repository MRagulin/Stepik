#!/usr/bin/python

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING']
    if '&' in resp:
        resp = resp.split("&")
    if len(resp) > 1:
        #resp = [item+"\r\n" for item in resp]
        resp = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return resp



# def fun(a,b):
#     return
# t= {}
# t['QUERY_STRING'] = 'a=1&a=2&b=3'
# r = app(t, fun)
# print(r)