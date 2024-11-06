import http.server

class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <head><title>Query Results</title></head>
        <body>
            <h1>Query Results</h1>
            <pre id="data">Waiting for updates...</pre>
            <script>
                const ws = new WebSocket('ws://localhost:8765');

                ws.onopen = () => console.log("Connected to WebSocket server.");
                ws.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    document.getElementById('data').textContent = JSON.stringify(data, null, 2);
                };
                ws.onclose = () => console.log("WebSocket closed.");
                ws.onerror = (error) => console.error("WebSocket error:", error);
            </script>
        </body>
        </html>
        """)

    def log_message(self, format, *args):
        return