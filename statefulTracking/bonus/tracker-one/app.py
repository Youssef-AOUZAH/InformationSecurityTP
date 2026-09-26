from flask import Flask, render_template, make_response, request
import secrets

app = Flask(__name__)

@app.route("/")
def home():
    aid = request.cookies.get("aid_t1")
    is_new = aid is None

    if is_new:
        aid = secrets.token_hex(4)

    response = make_response(render_template("index.html", aid=aid))

    if is_new:
        response.set_cookie(key="aid_t1", value=aid, max_age=50000, path="/", httponly=True)

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9005, debug=True)
