from app import app, db
from flask import render_template, request, redirect, url_for, session,flash
from models import Plant, Employee, Salon
from utils.helpers import encrypt_string
from utils.helpers import convert_list
from sqlalchemy import or_
import json
@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()

    return render_template('index.html', plants=plants, employees=employees, salons=salons, session=session)


@app.route('/login')
def login():
    return render_template('login.html', session=session)


@app.route('/auth', methods=['POST'])
def auth():
    form = request.form
    user = Employee.query.filter(Employee.email == form['login']).filter(
        Employee.password == encrypt_string(form['password'])).first()
    print(user)
    if user is not None:
        session['user'] = user.serialize
    return redirect(url_for('main'))

@app.route('/logout')
def logout():
    session.pop('user')
    # return redirect("http://localhost:8082/")
    return redirect(url_for('main'))


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant, session=session)


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    if session.get('user') is None:
        return redirect(url_for('main'))
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, session=session)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
    plant = Plant.query.get(id)
    form_data = request.form
    plant.name = form_data.get('name')
    plant.location = form_data.get('location')
    plant.director_id = form_data.get('director_id')
    db.session.add(plant)
    db.session.commit()
    return redirect(url_for('plant', id=id))


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee, session=session)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    employee = Employee.query.get(id)
    form_data = request.form
    employee.email = form_data.get('email')
    employee.name = form_data.get('name')
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    if session.get('user') is None:
        return redirect(url_for('main'))
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee, salons=salons, session=session)


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon, session=session)


@app.route('/salon/<int:id>/update', methods=['POST'])
def salon_update(id):
    salon = Salon.query.get(id)
    form_data = request.form
    salon.name = form_data.get('name')
    salon.city = form_data.get('city')
    salon.address = form_data.get('address')
    db.session.add(salon)
    db.session.commit()
    return redirect(url_for('salon', id=id))


@app.route('/salon/<int:id>/edit')
def salon_edit_page(id):
    if session.get('user') is None:
        return redirect(url_for('main'))
    salon = Salon.query.get(id)
    return render_template('edit-salon.html', salon=salon, session=session)

