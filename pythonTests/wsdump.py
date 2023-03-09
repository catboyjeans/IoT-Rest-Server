import websocket
ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/listen")
print(ws.recv())