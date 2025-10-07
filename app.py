from http.server import BaseHTTPRequestHandler, HTTPServer
import os
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello, world 2!"
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    port = int(os.getenv("DATABRICKS_APP_PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), HelloHandler)
    print(f"Serving on port {port}")
    server.serve_forever()
