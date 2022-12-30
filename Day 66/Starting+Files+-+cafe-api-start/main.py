import flask
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return flask.jsonify(cafes=random_cafe.to_dict())

    # return flask.jsonify(cafe={
    #     # "id": random_cafe.id,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "map_url": random_cafe.map_url,
    #     "name": random_cafe.name,
    #     "seats": random_cafe.seats
    # },
    # amenities={
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    #     "has_sockets": random_cafe.has_sockets,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    # }
    # )

    # return render_template()

## HTTP POST - Create Record
@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes = []
    for cafe in cafes:
        all_cafes.append(cafe.to_dict())
    return flask.jsonify(cafes=all_cafes)


# HTTP GET - Find Cafe
@app.route("/search")
def search_cafe():
    cafe_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=cafe_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have cafe on this location"})


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("new"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=request.form.get("sockets"),
        has_toilet=request.form.get("toilet"),
        has_wifi=request.form.get("wifi"),
        can_take_calls=request.form.get("calls"),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"Successfully added the new cafe"})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success":"Successfully Updated the price"}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, cafe with your given id doesn't exist"}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key=request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success={"Success": "Successfully deleted the cafe from database"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, cafe with that id not found"}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct API Key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
