from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch-users-1', methods=['GET'])
def fetch_users():
    url = "https://fake-json-api.mock.beeceptor.com/users"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify({"status": "ok", "data": response.json()})
        else:
            return jsonify({"status": "not ok", "data": response.json()})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
