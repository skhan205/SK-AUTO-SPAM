from flask import Flask
import time
import threading

app = Flask(__name__)

def simple_task():
    while True:
        print("🤖 Bot is active...")
        time.sleep(60)

@app.route('/')
def home():
    return "✅ Bot is LIVE and RUNNING!"

if __name__ == "__main__":
    # Background mein task start karo
    thread = threading.Thread(target=simple_task, daemon=True)
    thread.start()
    
    # Flask server start karo
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
