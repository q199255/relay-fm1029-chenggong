from flask import Flask, Response
import requests
import os

app = Flask(__name__)

@app.route('/')
def stream():
    url = os.environ.get("STREAM_URL", "http://211.75.60.169:5200/mp3_128.mp3")
    headers = {
        'ngrok-skip-browser-warning': '1'
    }
    r = requests.get(url, headers=headers, stream=True)
    return Response(r.iter_content(chunk_size=1024), content_type=r.headers['Content-Type'])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
