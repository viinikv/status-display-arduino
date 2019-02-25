from websocket import WebSocketApp
import json
import sys
import time
import _thread

URL = "wss://ws-feed.gdax.com"
LCDLEN = 16
ROUND = 100

def on_message(ws, message):
	j =json.loads(message)
	p = int(float(j["price"]))
	p = int(p/ROUND)*ROUND
	if p != ws.last:
		ws.last = p

def on_error(_, err):
	print(err, file=sys.stderr)

def on_open(ws):
	params = {
		"type": "subscribe",
		"channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
	}
	ws.send(json.dumps(params))

def main():
	ws = WebSocketApp(URL, on_open=on_open, on_message=on_message, on_error=on_error)
	ws.last = -1
	def run(ws):
		while True:
			ws.run_forever()
			print("WebSocket connection died, restarting", file=sys.stderr)
			ws.last = -1
			time.sleep(5)
	_thread.start_new_thread(run, (ws,))
	old_seconds = 0
	while True:
		t = time.time()
		seconds = int(t)
		if seconds != old_seconds:
			old_seconds = seconds
			timestamp = time.strftime("%_H.%M.%S", time.localtime(t))
			label = timestamp + str(ws.last).rjust(LCDLEN-len(timestamp.replace('.','')))
			print(label)
			sys.stdout.flush()
		# sleep until the next second
		time.sleep(1 - (t % 1) + 0.01)

if __name__ == '__main__':
	main()
