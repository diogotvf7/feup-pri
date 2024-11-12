import asyncio
import websockets
import json
import os
import socketserver
import webbrowser
import threading
from pathlib import Path
import importlib
import inspect
from requests.exceptions import ConnectionError


OUTPUT_FILE = Path(__file__).resolve().parent / "response.json"
PORT = 8000
WEBSOCKET_PORT = 8765

last_mod_time = None
stop_flag = threading.Event()

import importlib
import inspect
from pathlib import Path

QUERIES = []

queries_folder = Path(__file__).resolve().parent / "scripts"

# Track imported modules to avoid double imports
loaded_modules = set()

# Load all Python files in the queries folder and sort them by the numeric suffix
for file in sorted(queries_folder.glob("query*.py"), key=lambda f: int(f.stem[5:])):
    module_name = f"scripts.{file.stem}"
    
    if module_name not in loaded_modules:
        module = importlib.import_module(module_name)
        loaded_modules.add(module_name)
        
        # Find all functions in the module
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and name.startswith("query"):  # Only load functions that start with 'query'
                if obj not in QUERIES:  # Avoid adding the same function twice
                    QUERIES.append(obj)


def clear_screen():
    if os.name == 'nt': os.system('cls')  # Windows
    else: os.system('clear')  # Linux

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


async def start_websocket_server():
    # Directly pass notify_clients as the handler without using a lambda
    async with websockets.serve(notify_clients, "localhost", WEBSOCKET_PORT):
        print(f"WebSocket server running on ws://localhost:{WEBSOCKET_PORT}")
        await asyncio.Future()  # Keeps the server running

def websocket_server_thread():
    asyncio.run(start_websocket_server())

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
        websocket_thread = threading.Thread(target=websocket_server_thread)
        websocket_thread.daemon = True
        websocket_thread.start()

        # Main loop for handling user input
        while True:
            clear_screen()

            # Display the number of queries
            print(f"There are {len(QUERIES)} queries available.\n")

            try:
                # Ask the user for the query number or 0 to exit
                i = int(input(f"Please enter the number of the query you want to run:\n (0 to exit, 1 to {len(QUERIES)} for queries):\n "))
                
                if i == 0:
                    # Exit option
                    stop_flag.set()
                    print("Exiting...")
                    break
                elif 1 <= i <= len(QUERIES):
                    try:
                        response = QUERIES[i - 1]()  # Run the selected query
                        print(f"Executing query {i}...\n")
                        if response.status_code == 200:
                            try:
                                json_data = response.json()
                                OUTPUT_FILE.write_text(json.dumps(json_data, indent=2))
                                print("Response saved to response.json.")
                                input("Press Enter to continue...")  # Pause before re-displaying the prompt

                            except ValueError:
                                print("Received non-JSON response or empty body.")
                        else:
                            print(f"Error: {response.status_code}")
                            input("Press Enter to continue...")
                    except ConnectionError:
                        print("Error: Unable to connect to the server. Please make sure the server is running.")
                        input("Press Enter to continue...")

                else:
                    print(f"Invalid input. Please enter a number between 0 and {len(QUERIES)}.")
                    input("Press Enter to continue...")  # Pause before re-displaying the prompt

            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                input("Press Enter to continue...")  # Pause before re-displaying the prompt

    except OSError as e:
        if e.errno == 98:
            print(f"""
                Port {PORT} is already in use. Please close any other services using that port.
                Use 'sudo lsof -i :{PORT}' to find the process using the port.
                Use 'kill -9 <PID>' to kill the process.
                """)
            print(f"Error: {e}")
        else:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
