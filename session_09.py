from flask import Flask


app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "akbar",
        "phone_number": "09123456789",
    },
    {
        "id": 2,
        "name": "asqar",
        "phone_number": "09129876543",
    },
]

@app.route("/hello")
def hello_world():
    return {
        "message": "Hello World!",
    }


app.run()
