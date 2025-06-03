from flask import render_template, request, redirect

from models import Person


def register_routes(app, db):
    
    @app.route('/', methods=['GET'])
    def index():
        people = Person.query.all()
        return render_template(template_name_or_list='index.html',people=people)
            
    @app.route('/add_person', methods = ['POST'])
    def add_person():
        name = request.form.get('name')
        age = int(request.form.get('age'))
        job = request.form.get('job')
    
        person = Person(name=name, age=age, job=job)
        db.session.add(person)
        db.session.commit()
        return redirect('/')
    
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        people = Person.query.all()
        return render_template(template_name_or_list='index.html',people=people)

