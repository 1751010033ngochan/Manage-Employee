from flask import render_template, redirect, request, url_for, flash
from app import app, dao
from app.models import *


# Read
@app.route("/")
def index():
    all_emp = Data.query.all()
    return render_template("index.html", employees=all_emp)


# Create
@app.route("/create", methods=["get", "post"])
def create():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        flash('Create Succeed!', 'Success')

        dao.create(name=name, email=email, phone=phone)

    return redirect(url_for('index'))


# Update
@app.route("/update", methods=["get", "post"])
def update():
    if request.method == "POST":

        employee = Data.query.get(request.form.get('id'))
        employee.name = request.form.get('name')
        employee.email = request.form.get('email')
        employee.phone = request.form.get('phone')

        db.session.commit()

        flash('Update Succeed!', 'Success')

    return redirect(url_for('index'))


# Delete
@app.route("/delete/<id>/", methods=["get", "post"])
def delete(id):
    dao.delete_by_id(id)

    flash('Delete Succeed!', 'Success')

    return redirect(url_for('index'))


# Starting the app
if __name__ == "__main__":
    app.run(debug=True)
