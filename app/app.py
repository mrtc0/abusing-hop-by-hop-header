from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/")
def api():
    x = request.headers.get("Xxx")
    if x == None:
        return "missing header"

    headers = [header for header in request.headers]
    return json.dumps(headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
