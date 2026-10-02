from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print("\n========== [PASSIVE HTTP HEADERS] ==========")
    print("IP Address          :", request.remote_addr)
    print("HTTP Method         :", request.method)
    print("User-Agent          :", request.headers.get("User-Agent"))
    print("Accept-Language     :", request.headers.get("Accept-Language"))
    print("Accept-Encoding     :", request.headers.get("Accept-Encoding"))
    print("Sec-CH-UA           :", request.headers.get("Sec-CH-UA"))
    print("Sec-CH-UA-Platform  :", request.headers.get("Sec-CH-UA-Platform"))
    print("Sec-Fetch-Site      :", request.headers.get("Sec-Fetch-Site"))
    print("============================================\n")
    return render_template("index.html")

@app.route("/collect", methods=["POST"])
def collect():
    data = request.get_json()
    print("\n========== [COMBINED CLIENT FINGERPRINT (PARTS 2 & 3)] ==========")
    for key, val in data.items():
        print(f"  {key:20}: {val}")
    print("=================================================================\n")
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)