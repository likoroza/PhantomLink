import keyboard
from http.server import HTTPServer, BaseHTTPRequestHandler
from time import sleep

class ProofOfConceptServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length).decode()

            if data == "super":
                keyboard.press_and_release('windows')
                keyboard.write("מנהל המשימות")
                sleep(0.5)
                keyboard.press_and_release('enter')


            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(f'<h1>{data}</h1>'.encode())

        self.send_response(200)
        
def run(handler_class, address=('0.0.0.0', 5555)):
    httpd = HTTPServer(address, handler_class)
    print('Serving...')
    httpd.serve_forever()

run(ProofOfConceptServer)