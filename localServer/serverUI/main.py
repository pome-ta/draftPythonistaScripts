
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler,  BaseHTTPRequestHandler
import requests

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)

print(SimpleHTTPRequestHandler)
webbrowser.open('http://localhost:8000/')
try:
  httpd.serve_forever()
except KeyboardInterrupt:
  httpd.shutdown()
  print('Server stopped')

