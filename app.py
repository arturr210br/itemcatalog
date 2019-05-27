''' Whole project is based on the Udacity FSND course materials'''

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
import string
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import relationship
from database_setup import Division, User, Base, Driver

from urllib3.connectionpool import xrange

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from flask import session as login_session
app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "divisions-239523"


engine = create_engine('sqlite:///division.db')
Base.metadata.create_all(engine)


DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;' \
        'height: 300px;' \
        'border-radius: 150px;' \
        '-webkit-border-radius: 150px;' \
        '-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


@app.route('/logout')
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % \
        login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token .', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/divisions/JSON')
def divisionsJSON():
    divisions = session.query(Division).all()
    return jsonify(divisions=[d.serialize for d in divisions])


@app.route('/divisions/<int:division_id>/driver/JSON')
@app.route('/divisions/<int:division_id>/drivers/JSON')
def driversJSON(division_id):
    d_json = session.query(Driver).filter_by(division_id=division_id).all()
    return jsonify(d_json=[d.serialize for d in d_json])


@app.route('/divisions/<int:division_id>/driver/<int:driver_id>/JSON')
@app.route('/divisions/<int:division_id>/drivers/<int:driver_id>/JSON')
def driverIdJSON(division_id, driver_id):

    if division_id > 1:
        driver_id = driver_id + (division_id-1) * 10
    else:
        driver_id = driver_id
    driver_json = session.query(Driver).filter_by(id=driver_id).one()
    return jsonify(jDriver=driver_json.serialize)


@app.route('/')
@app.route('/divisions/')
def showDivisions():
    print(login_session)
    division = session.query(Division).all()
    if 'username' not in login_session:
        return render_template('publicDivisions.html', division=division)
    else:
        return render_template('divisions.html', division=division,
                               login_session=login_session)


@app.route('/divisions/<int:division_id>/')
@app.route('/divisions/<int:division_id>/drivers')
def showDivisionDetail(division_id):
    divisions = session.query(Division).filter_by(id=division_id).one()
    drivers = session.query(Driver).filter_by(
        division_id=division_id).all()
    if 'username' not in login_session:
        return render_template('publicdriver.html',
                               divisions=divisions,
                               division_id=division_id,
                               drivers=drivers)
    else:
        return render_template("driver.html",
                               divisions=divisions,
                               division_id=division_id,
                               drivers=drivers)


@app.route('/divisions/new/', methods=['GET', 'POST'])
def newDivision():
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        newDivision = Division(name=request.form['name'],
                               user_id=login_session['username'])
        session.add(newDivision)
        flash('New Division %s Successfully Created' % newDivision.name)
        session.commit()
        return redirect(url_for('showDivisions'))
    else:
        return render_template('newDivision.html', login_session=login_session)


@app.route('/divisions/<int:division_id>/edit/', methods=['GET', 'POST'])
def editDivision(division_id):
    editedDivision = session.query(
        Division).filter_by(id=division_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedDivision.user_id != login_session['username']:
        return "<script>function myFunc() {alert('You \
             are not authorized to edit this division.\
             Please create your own division in order \
             to edit.');}</script><body onload='myFunc()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedDivision.name = request.form['name']
        session.add(editedDivision)
        session.commit()
        flash(" %s has been edited" % editedDivision.name)
        return redirect(url_for('showDivisions'))
    else:
        return render_template(
            'editDivision.html', division=editedDivision,
            division_id=division_id)


@app.route('/divisions/<int:division_id>/delete/', methods=['GET', 'POST'])
def deleteDivision(division_id):
    divisionDelete = session.query(
        Division).filter_by(id=division_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if divisionDelete.user_id != login_session['username']:
        return "<script>function myFunc() " \
               "{alert('You are not authorized to delete this division." \
               "Create your own one in order to delete it.');}</script>" \
               "<body onload='myFunc()''>"
    if request.method == 'POST':
        session.delete(divisionDelete)
        session.commit()
        flash("%s has been deleted" % divisionDelete.name)
        return redirect(
            url_for('showDivisions', division_id=division_id))
    else:
        return render_template(
            'deleteDivision.html', division=divisionDelete)


@app.route('/divisions/<int:division_id>/driver/new/', methods=['GET', 'POST'])
def newDriver(division_id):
    if 'username' not in login_session:
        return redirect('/login')
    tempdivisions = session.query(Division).filter_by(id=division_id).one()

    if request.method == 'POST':
        newdriver = Driver(name=request.form['name'],
                           description=request.form['description'],
                           rank=request.form['rank'],
                           country=request.form['country'],
                           division_id=division_id,
                           user_id=tempdivisions.user_id)
        session.add(newdriver)
        session.commit()
        flash('New Driver: %s . Successfully Created' % (newdriver.name))
        return redirect(url_for('showDivisionDetail', division_id=division_id))
    else:
        return render_template('newdriver.html', division_id=division_id)


@app.route('/divisions/<int:division_id>/driver/<int:driver_id>/edit',
           methods=['GET', 'POST'])
def editDriver(division_id, driver_id):
    if 'username' not in login_session:
        return redirect('/login')

    editedDriver = session.query(Driver).filter_by(id=driver_id).one()
    editedDivisions = session.query(Division).filter_by(id=division_id).all()
    print(login_session['username'])
    print(editedDriver)
    print(editedDriver.user_id)
    if login_session['username'] != editedDriver.user_id:
        return "<script>function myFunc() " \
               "{alert('You are not authorized to edit this driver." \
               " Please create your own one in order to add drivers.');}" \
               "</script><body onload='myFunc()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedDriver.name = request.form['name']
        if request.form['description']:
            editedDriver.description = request.form['description']
        if request.form['rank']:
            editedDriver.rank = request.form['rank']
        if request.form['country']:
            editedDriver.country = request.form['country']
        session.add(editedDriver)
        session.commit()
        flash('Driver Successfully Edited')
        return redirect(url_for('showDivisionDetail',
                                division_id=division_id))
    else:

        return render_template(
            'editdriver.html', division_id=division_id, driver_id=driver_id,
            driver=editedDriver, editedDivisions=editedDivisions)


@app.route('/divisions/<int:division_id>/driver/<int:driver_id>/delete',
           methods=['GET', 'POST'])
def deleteDriver(division_id, driver_id):
    if 'username' not in login_session:
        return redirect('/login')

    deletedDriver = session.query(Driver).filter_by(id=driver_id).one()
    editedDivisions = session.query(Division).filter_by(id=division_id).all()
    if login_session['username'] != deletedDriver.user_id:
        return "<script>function myFunc() " \
               "{alert('You are not authorized to edit this driver." \
               " Create your own one in order to add drivers.');}" \
               "</script><body onload='myFunc()''>"
    if request.method == 'POST':
        session.delete(deletedDriver)
        session.commit()
        return redirect(url_for('showDivisions',
                                division_id=division_id))
    else:
        return render_template('deleteDriver.html', division_id=division_id,
                               driver_id=driver_id, driver=deletedDriver)


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']

        flash("You have successfully been logged out.")
        return redirect(url_for('showDivisions'))
    else:
        flash("You were not logged in")


if __name__ == '__main__':
    app.secret_key = 'my_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
