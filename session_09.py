from flask import Flask, Response, request


app = Flask(__name__)

users = {
    1: {
        "name": "akbar",
        "phone_number": "09123456789",
    },
    2: {
        "name": "asqar",
        "phone_number": "09129876543",
    },
}

@app.route("/hello")
def hello_world():
    return {
        "message": "Hello World!",
    }


@app.route("/profile/<int:id>")
def profile(id: int):
    user = users.get(id)
    if user is not None:
        return user

    return Response(
        "NOT FOUND",
        status=404,
    )


@app.route("/profile/<id>")
def profile_test(id):
    return f"Hello {id}"


@app.route("/register", methods=["POST"])
def register():
    users[3] = request.json
    return "OK"

app.run()
