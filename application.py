#importing all the important libraries
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

#application name is application
application = Flask(__name__)

#database configuration
application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contact.db'
application.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db=SQLAlchemy(application)

#model of the database
class contactme(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    sub = db.Column(db.String(100))
    body = db.Column(db.String(200))  

    def __repr__(self):
        return 'contact me ' +str(self.id)  

#landing page
@application.route('/')
@application.route('/home')
def home():
    return render_template('ishan.html')
#contact me page
@application.route('/contactme')
def contact_me():
    return render_template('contactme.html')

#sending the data to database
@application.route('/contactme', methods=['POST'])
def contactform():
    contact_name = request.form['name']
    contact_email = request.form['email']
    contact_sub = request.form['sub']
    contact_body = request.form['body']
    new_entry =contactme(name=contact_name ,email=contact_email, sub=contact_sub, body=contact_body)
    db.session.add(new_entry)
    db.session.commit()
    return redirect('/contactme')

if __name__ == "__main__":
    application.run(debug=True)