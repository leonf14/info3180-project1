"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app, db
from app.models import Users
from flask import render_template, request, redirect, url_for, flash, g, jsonify
from sqlalchemy.sql import exists
from .forms import UserProfileForm
from datetime import datetime
from random import randint
from werkzeug import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile', methods=['POST', 'GET'])
def add_profile():
    """Add a profile"""
    form = UserProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username  = request.form['username'].strip()
            firstname = request.form['firstname'].strip()
            lastname = request.form['lastname'].strip()
            sex   = request.form['sex']
            age   = request.form['age']
            bio = request.form["bio"]
            image = request.files['img']
            
            while True:
                userid = randint(620000000,620099999)
                if not db.session.query(exists().where(Users.userid == str(userid))).scalar():
                    break
                  
            filename = "{}-{}".format(userid,secure_filename(image.filename))
            filepath = "app/static/uploads/{}".format(filename)
            image.save(filepath)
            
            user = Users(str(userid),username,firstname,lastname,sex,age, bio,filename,datetime.now())
            db.session.add(user)
            db.session.commit()
            
            flash('User successfully added!', category='success')
            return redirect(url_for('list_profiles'))
        
    return render_template('add_profile.html', form=form)


@app.route('/profiles', methods=['POST','GET'])
def list_profiles():
    """View a list of profiles"""
    ulist   = []
    result  = db.session.query(Users).all()
    for user in result:
        ulist.append({"username":user.username,"userid":user.userid})
    if request.headers.get('content-type') == 'application/json' or request.method == 'POST':
        return jsonify(users = ulist)
    return render_template('profiles.html',ulist=ulist)


@app.route('/profile/<int:userid>', methods=['POST','GET'])
def view_profile(userid):
    """View a profile"""
    user = db.session.query(Users).filter(Users.userid == str(userid)).first()
    if not user:
        flash('Oops, we couldn\'t find that user.', category='danger')
    else:
        if request.headers.get('content-type') == 'application/json' or request.method == 'POST':
            return jsonify(userid=user.userid, username=user.username, image=user.image, sex=user.sex, age=user.age,\
                          profile_added_on=user.profile_added_on)
        return render_template('profile.html', user=user)
    return redirect(url_for('list_profiles'))



@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
   
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
