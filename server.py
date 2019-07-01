import subprocess
import cherrypy

class Root(object):
    def index(self):
        def content():
            proc = subprocess.Popen(['python3', 'sysinfoRemote.py'], stdout=subprocess.PIPE)
            line = proc.stdout.readline()
            while line:
                yield line
                line = proc.stdout.readline()
        return content()
    index.exposed = True
    index._cp_config = {'response.stream': True}
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(Root())