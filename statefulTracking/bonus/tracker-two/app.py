from flask import Flask, render_template, make_response, request, jsonify
import secrets

app = Flask(__name__)

synced_ids = {}

@app.route("/")
def home():
    return render_template("index.html", synced_ids=synced_ids)

@app.route("/sync")
def sync():
    aid_t2 = request.cookies.get("aid_t2")
    is_new = aid_t2 is None

    if is_new:
        aid_t2 = secrets.token_hex(4)

    t1_id = request.args.get("t1_id")
    if t1_id:
        synced_ids[aid_t2] = t1_id

    response = make_response(jsonify(status="synced", tracker_two_id=aid_t2, tracker_one_id=t1_id))

    if is_new:
        response.set_cookie(key="aid_t2", value=aid_t2, max_age=50000, path="/", httponly=True)

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9006, debug=True)
