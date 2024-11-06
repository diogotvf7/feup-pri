import asyncio
import websockets
import json
import os
import requests
import http.server
import socketserver
import webbrowser
import threading
from pathlib import Path

OUTPUT_FILE = Path(__file__).resolve().parent / "response.json"
PORT = 8000
WEBSOCKET_PORT = 8765

last_mod_time = None

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux
        os.system('clear')

async def notify_clients(websocket, path):
    global last_mod_time
    await websocket.send("Connected to WebSocket server for live updates.")
    
    while True:
        current_mod_time = os.path.getmtime(OUTPUT_FILE)
        if last_mod_time is None or current_mod_time > last_mod_time:
            last_mod_time = current_mod_time

            if OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0:  # Check if file has data
                with open(OUTPUT_FILE, 'r') as file:
                    try:
                        data = json.load(file)
                        await websocket.send(json.dumps(data))
                    except json.decoder.JSONDecodeError:
                        await websocket.send(json.dumps({"error": "Invalid JSON or empty response."}))
            else:
                await websocket.send(json.dumps({"error": "No valid data available."}))
        
        await asyncio.sleep(1)
    
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

                ws.onopen = () => {
                    console.log("Connected to WebSocket server.");
                };

                ws.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    document.getElementById('data').textContent = JSON.stringify(data, null, 2);
                };

                ws.onclose = () => {
                    console.log("WebSocket connection closed.");
                };

                ws.onerror = (error) => {
                    console.error("WebSocket error:", error);
                };
            </script>
        </body>
        </html>
        """)
    def log_message(self, format, *args):
        return

def start_websocket_server():
    # print(f"Starting WebSocket server on ws://localhost:{WEBSOCKET_PORT}")
    loop = asyncio.new_event_loop()  
    asyncio.set_event_loop(loop)     
    loop.run_until_complete(
        websockets.serve(notify_clients, "localhost", WEBSOCKET_PORT)
    )
    loop.run_forever()

def start_server():
    with socketserver.TCPServer(("", PORT), JSONHandler) as httpd:
        print(f"Serving JSON at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}", 0)
        httpd.serve_forever()

from scripts import query1, query2, query3, query4, query5, query6

queries = [
    query1,
    query2,
    query3,
    query4,
    query5,
    query6
]

def main():
    try:
        server_thread = threading.Thread(target=start_server)   # Thread to start http server
        server_thread.daemon = True
        server_thread.start()

        websocket_thread = threading.Thread(target=start_websocket_server) # Thread to start websocket server
        websocket_thread.daemon = True
        websocket_thread.start()

        while True:
            # clear_screen()
            i = input("""
                          Which query would you like to run?
                            1. Field boost
                            2. Independent boost
                            3. Phrase match
                            4. Proximity
                            5. Term boost
                            6. Wildcard
                            7. Exit
                    """)
            if i >= "1" and i <= "6":
                response = queries[int(i) - 1]()
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        OUTPUT_FILE.write_text(json.dumps(json_data, indent=2))
                    except ValueError:
                        print("Received non-JSON response or empty body.")
                else:
                    print(f"Error: {response.status_code}")
            elif i == "7":
                break
            else:
                print("Invalid input. Please try again.")

    except OSError as e: # TODO: Ainde é preciso??
        if e.errno == 98:
            print(f"""
                Port {PORT} is already in use. Please close any other services using that port.
                Use 'sudo lsof -i :8000' to find the process using the port.
                Use 'kill -9 <PID>' to kill the process.
                """)
        else:
            raise

if __name__ == "__main__":
    main()