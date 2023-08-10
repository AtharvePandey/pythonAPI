# making my own api using Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Atharve Pandey",
        "email": "aspandey@umass.edu"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data),200
@app.route("/create_user", methods = ["POST"])
def create_user():
    data = request.get_json()
    #add data to database??

    return jsonify(data), 201
if __name__ == "__main__":
    app.run(debug=True) #this will run our flask server