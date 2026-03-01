#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        body = b'{"status":"ok","service":"<PROJECT_NAME>"}'
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', <DEFAULT_PORT>), Handler)
    print('Server listening on <DEFAULT_PORT>')
    server.serve_forever()
