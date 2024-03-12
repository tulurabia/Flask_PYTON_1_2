from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "hello word clarusway-17"


@app.route("/second")
def head2():
    return "ahanda ikinci page"

@app.route("/third")
def head3():
    return "buda 3 ncü sayfa"

if __name__ == '__main__':

    #app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8081)