from flask import Flask, render_template,make_response,request
import secrets

app=Flask(__name__)
@app.route("/")
def home():
    
  

    response=make_response(render_template("index.html"))

    return response


if __name__=="__main__":
    app.run(host="127.0.0.1",port=9001,debug=True)