from flask import Flask

app = Flask(__name__)

# Members for API Route

@app.route("/getResult")
def get_result():
    return {"Hello": "World"}
    ## return "This is a test return from the Flask API"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8000", debug=True)
