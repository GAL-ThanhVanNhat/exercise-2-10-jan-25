from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from shared.constant import POST_METHOD, GET_METHOD, CONNECTION_STRING, PUT_METHOD

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = CONNECTION_STRING

db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(512), nullable=False)
    createdDate = db.Column(db.DateTime, server_default=db.func.now())
    
    def __init__(self, firstName, lastName, salary, address):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.address = address
    
    def __repr__(self):
        return f"Doctor('{self.firstName}', '{self.lastName}', {self.salary}, '{self.address}')"
    
# Home Page    
@app.route('/', methods = [POST_METHOD, GET_METHOD])
def index():
    # add doctor
    if request.method == POST_METHOD: 
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        salary = request.form["salary"]
        address = request.form["address"]
        doctor = Doctor(firstName, lastName, salary , address)
        try:
            db.session.add(doctor)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"{e}")
            return e
    
    # get all doctors
    if request.method == GET_METHOD:
        try:
            doctors = Doctor.query.order_by(Doctor.createdDate).all()
            return render_template("index.html", doctors = doctors)
        except Exception as e:
            print(f"{e}")
            return "There was an issue getting all doctors"
    return render_template("index.html")

@app.route('/delete/<int:id>')
def delete(id: int):
    doctor = Doctor.query.get_or_404(id)
    try:
        db.session.delete(doctor)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"{e}")
        return e

@app.route('/update/<int:id>', methods = [POST_METHOD, GET_METHOD])
def update(id: int):
    doctor : Doctor = Doctor.query.get_or_404(id)
    if request.method == POST_METHOD:
        doctor.firstName = request.form["firstName"]
        doctor.lastName = request.form["lastName"]
        doctor.salary = request.form["salary"]
        doctor.address = request.form["address"]
        try:
            #db.session.update(doctor)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"{e}")
            return e
    else :
        return render_template('/update.html', doctor = doctor)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)