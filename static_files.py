import bottle

from bottle import static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/static')


