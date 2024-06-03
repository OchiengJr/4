from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from wtforms import Form, StringField, validators
from models import Hero, Power, HeroPower

app = Flask(__name__)

# Define a route for the root URL to return a welcome message
@app.route('/')
def index():
    return "Welcome to the superhero API"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Forms for Validation
class HeroPowerForm(Form):
    strength = StringField('Strength', [validators.InputRequired(), validators.AnyOf(['Strong', 'Weak', 'Average'])])

class PowerForm(Form):
    description = StringField('Description', [validators.InputRequired(), validators.Length(min=20)])

# Define Schemas for Serialization
class HeroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'super_name', 'hero_powers')

class PowerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)
power_schema = PowerSchema()
powers_schema = PowerSchema(many=True)

# Routes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify(heroes_schema.dump(heroes))

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero_schema.dump(hero))
    else:
        return jsonify({"error": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify(powers_schema.dump(powers))

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power_schema.dump(power))
    else:
        return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        description = request.json.get('description')
        if description and len(description) >= 20:
            power.description = description
            db.session.commit()
            return jsonify(power_schema.dump(power))
        else:
            return jsonify({"errors": ["Description must be present and at least 20 characters long"]}), 400
    else:
        return jsonify({"error": "Power not found"}), 404

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    form = HeroPowerForm(request.form)
    if form.validate():
        hero_id = request.json.get('hero_id')
        power_id = request.json.get('power_id')
        strength = request.json.get('strength')

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if hero and power:
            if strength in ['Strong', 'Weak', 'Average']:
                hero_power = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_power)
                db.session.commit()
                return jsonify(hero_power.to_dict())
            else:
                return jsonify({"errors": ["Strength must be one of 'Strong', 'Weak', 'Average'"]}), 400
        else:
            return jsonify({"error": "Hero or Power not found"}), 404
    else:
        return jsonify({"errors": form.errors}), 400

if __name__ == '__main__':
    app.run(debug=True)
