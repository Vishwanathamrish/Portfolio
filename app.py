from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from dotenv import load_dotenv
import os

# Configure logging for debug info (logs are printed to Render logs)
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = Flask(__name__)

# Gmail SMTP Configuration from env variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Basic health check route for Render
@app.route('/healthz')
def health():
    return "ok", 200

@app.route('/')
def portfolio():
    app.logger.debug("Home route accessed")
    return render_template("home.html")

@app.route('/projects')
def projects():
    app.logger.debug("Projects route accessed")
    return render_template("project.html")

@app.route('/education')
def education():
    app.logger.debug("Education route accessed")
    return render_template("education.html")

@app.route('/about')
def about():
    app.logger.debug("About route accessed")
    return render_template("about.html")

@app.route('/contact')
def contact():
    app.logger.debug("Contact route accessed")
    return render_template("contact.html")

@app.route('/submit', methods=['POST'])
def submit():
    app.logger.debug("Submit route accessed")
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    message = request.form.get('message', '')

    try:
        # Build the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL
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
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)  # Add timeout
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())
        server.quit()

        app.logger.info("✅ Email sent successfully!")
    except Exception as e:
        app.logger.error(f"❌ Error sending email: {e}")
        return "An error occurred while sending the email.", 500

    return redirect(url_for('contact'))

if __name__ == '__main__':
    # Only use for local development/testing
    app.run(debug=True)
