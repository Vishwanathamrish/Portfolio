from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Gmail SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'vishwanathamrish@gmail.com'
SENDER_PASSWORD = 'qplt yhqf kpya kbti'  # Consider moving this to environment variable for security

# Routes
@app.route('/')
def portfolio():
    return render_template("home.html")

@app.route('/projects')
def projects():
    return render_template("project.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL  # You receive the message
        msg['Subject'] = f'New Contact Form Submission from {name}'

        body = f"""
        📬 Contact Form Submission:

        🔹 Name: {name}
        🔹 Email: {email}
        🔹 Phone: {phone if phone else 'Not provided'}
        🔹 Message: {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())
        server.quit()

        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return "An error occurred while sending the email.", 500

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
