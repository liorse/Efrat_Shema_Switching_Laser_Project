# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from pywinauto import application, keyboard
from time import sleep

app = application.Application()
app.connect(path=r"C:\windows\system32\win32Calc.exe")
dlg = app['Calculator']

hostName = "localhost"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/change_to_Laser_1'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            dlg.send_keystrokes('%1', with_spaces=False, with_tabs=False, with_newlines=False)
        elif self.path.endswith('/change_to_Laser_2'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            dlg.send_keystrokes('%2', with_spaces=False, with_tabs=False, with_newlines=False)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    '''
    URL url = new URL("http://127.0.0.1:80/?do_GET");
HttpURLConnection httpCon = (HttpURLConnection) url.openConnection();
httpCon.setDoOutput(true);
httpCon.setRequestMethod("GET");
OutputStreamWriter out = new OutputStreamWriter(
  httpCon.getOutputStream());
out.write("GET");
out.close();
httpCon.getInputStream();
'''