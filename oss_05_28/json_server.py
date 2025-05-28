import flask

app=flask.Flask(__name__)

@app.route("/api/hello")
def hello():
    return flask.jsonify(message="Hello, Flask!")

@app.route("/api/echo",methods=["POST"])
def ech():
    data=flask.request.get_json()
    name=data.get("name","World")
    return flask.jsonify(greeting=f"Hello, {name}! Your age is {data.get("age","unknown")}.",echo=data)

if __name__=="__main__":
    app.run("0.0.0.0",10015)
