import asyncio
import websockets
import json
import os
import socketserver
import webbrowser
import threading
from pathlib import Path

from json_handler import JSONHandler
from scripts import query1, query2, query3, query4, query5, query6

OUTPUT_FILE = Path(__file__).resolve().parent / "response.json"
PORT = 8000
WEBSOCKET_PORT = 8765
QUERIES = [
    query1,
    query2,
    query3,
    query4,
    query5,
    query6
]

last_mod_time = None
stop_flag = threading.Event()

def clear_screen():
    if os.name == 'nt': os.system('cls')    # Windows
    else: os.system('clear')                # Linux
        
async def send_data(websocket):
    if OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0:
        try:
            with open(OUTPUT_FILE, 'r') as file:
                data = json.load(file)
                await websocket.send(json.dumps(data))
        except json.decoder.JSONDecodeError:
            await websocket.send(json.dumps({"error": "Invalid JSON or empty response."}))
    else:
        await websocket.send(json.dumps({"error": "No valid data available."}))
            
async def notify_clients(websocket, path):
    global last_mod_time
    await websocket.send("Connected to WebSocket server for live updates.")
    
    while True:
        try:
            current_mod_time = os.path.getmtime(OUTPUT_FILE)
            if last_mod_time is None or current_mod_time > last_mod_time:
                last_mod_time = current_mod_time
                await send_data(websocket)
            await asyncio.sleep(1)

            if stop_flag.is_set():
                print("WebSocket server stopping...")
                break
        
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed.")
            break
    
def start_websocket_server():
    loop = asyncio.new_event_loop()  
    asyncio.set_event_loop(loop)     
    loop.run_until_complete(
        websockets.serve(notify_clients, "localhost", WEBSOCKET_PORT)
    )
    loop.run_forever()

def start_server():
    with socketserver.TCPServer(("", PORT), JSONHandler) as httpd:
        print(f"Serving JSON at http://localhost:{PORT}")
        # Open the web page immediately when the server starts
        webbrowser.open(f"http://localhost:{PORT}", 0)
        while not stop_flag.is_set():
            httpd.handle_request()
        print("Server stopping...")
 
def main():
    try:
        # Start the server thread to handle HTTP requests
        server_thread = threading.Thread(target=start_server)   
        server_thread.daemon = True
        server_thread.start()

        # Start the WebSocket server thread
        websocket_thread = threading.Thread(target=start_websocket_server)
        websocket_thread.daemon = True
        websocket_thread.start()

        # Main loop for handling user input
        while True:
            clear_screen()
            i = int(input("""
                          Which query would you like to run?
                            1. Field boost
                            2. Independent boost
                            3. Phrase match
                            4. Proximity
                            5. Term boost
                            6. Wildcard
                            7. Exit
                    """))
            if i >= 1 and i <= 6:
                response = QUERIES[i - 1]()
                if response.status_code == 200:
                    try:
                        json_data = response.json()
                        OUTPUT_FILE.write_text(json.dumps(json_data, indent=2))
                    except ValueError:
                        print("Received non-JSON response or empty body.")
                else:
                    print(f"Error: {response.status_code}")
            elif i == 7:
                stop_flag.set()
                break
            else:
                print("Invalid input. Please try again.")

    except OSError as e:
        if e.errno == 98:
            print(f"""
                Port {PORT} is already in use. Please close any other services using that port.
                Use 'sudo lsof -i :8000' to find the process using the port.
                Use 'kill -9 <PID>' to kill the process.
                """)
            print(f"Error: {e}")
        else:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
