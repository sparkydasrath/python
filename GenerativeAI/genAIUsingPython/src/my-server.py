from http.server import HTTPServer, BaseHTTPRequestHandler
from fastapi import FastAPI
import uvicorn


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")


if __name__ == "__main__":
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()

    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"message": "Hello, World!"}

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)

    