from flask import Flask, request, jsonify

app = Flask(__name__)

analytics_profiles = {}

@app.route("/")
def view_profiles():
    return analytics_profiles

@app.route("/collect")
def collect():
    aid = request.args.get("aid", "unknown")
    page = request.args.get("page", "unknown")

    if aid not in analytics_profiles:
        analytics_profiles[aid] = []
    analytics_profiles[aid].append(page)

    return jsonify(status="success"), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9004, debug=True)