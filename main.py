from flask import Flask, render_template, redirect, url_for, request
import smtplib
import config


app = Flask(__name__)

MY_EMAIL = config.MY_EMAIL
MY_PASSWORD = config.MY_PASSWORD

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return redirect(url_for('home', msg_sent=True))
    return render_template("index.html", msg_sent=False)

def send_email(name, email, message):
    email_message = f"Subject:Message from My Website\n\nName: {name}\nEmail: {email}\nMessage:{message}".encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == "__main__":
   app.run(debug=True)