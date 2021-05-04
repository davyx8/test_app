from sanic import Sanic
from sanic_jwt import exceptions
import json
from sanic_jwt import initialize
from sanic import response
from sanic_jwt.decorators import protected
class User:

    def __init__(self, id, username, password):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}


users = [User(1, "user1", "abcxyz"), User(2, "user2", "abcxyz")]


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


app = Sanic('dickface')
initialize(app, authenticate=authenticate)


@app.route("/")
async def open_route(request):
    return response.json({"protected": False})


@app.post("/norm")
@protected()
async def protected_route(request):
    b = request.body
    print(b)
    j =  eval(b)
    to_ret = {}
    for obj in j:
        key = obj['name']
        val =  [x for x in obj if 'val' in x.lower() ][0]
        to_ret[key] = obj[val]
    return response.json(to_ret)
@app.route("/protected")
@protected()
async def protected_route(request):
    return response.json({"protected": True})

if __name__ == "__main__":
    with open('config.json' ) as f:
        auth_dts =  json.load(f)
    print(auth_dts)
    users.append(User(3, auth_dts['user'],auth_dts['pass']))

    username_table = {u.username: u for u in users}
    userid_table = {u.user_id: u for u in users}

    app.run(host="127.0.0.1", port=8888)
