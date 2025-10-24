# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, TailwindCSS, and featuring dark/light mode.

## Features

- 🌓 Dark/Light mode toggle with persistent settings using localStorage
- 📱 Fully responsive design with TailwindCSS
- 🚀 Fast and optimized performance with inline CSS/JS
- 📧 Email integration using SMTP for contact form
- 📄 Multiple sections: About, Education, Experience, Projects, Contact
- 🔗 Social media integration
- 📝 Downloadable Resume
- 🖼️ Project showcase with images
- ⚡ Zero external CSS/JS dependencies for faster loading

## Tech Stack

- **Backend Framework:** Flask (Python)
- **Frontend:** HTML5, TailwindCSS, JavaScript
- **Icons:** Lucide Icons
- **Animation:** Smooth scrolling and transitions
- **Theme:** Dark/Light mode with localStorage persistence

## Project Structure

```
portfolio-site/
├── app.py              # Flask application entry point with SMTP email integration
├── static/            # Static assets
│   ├── images/       # Project and profile pictures
│   └── pdf/          # Resume and other documents
└── templates/         # HTML templates with inline TailwindCSS and JavaScript
    ├── about.html    # About page
    ├── contact.html  # Contact page with email form
    ├── education.html# Education page
    ├── home.html     # Home page
    └── project.html  # Projects page
```

Note: CSS and JavaScript are implemented inline in HTML files using TailwindCSS and vanilla JavaScript for optimal performance.

## Setup and Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd portfolio-site
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

The site will be available at `http://localhost:5000`

## Customization

1. **Content**: Update the HTML files in the `templates/` directory
2. **Styling**: Modify TailwindCSS classes directly in the HTML files
3. **Theme**: Default theme can be set to dark/light in the theme script
4. **Images**: Replace project and profile images in `static/images/`
5. **Resume**: Update your resume in `static/pdf/`
6. **Email**: Configure SMTP settings in `app.py` for the contact form
   ```python
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'
   ```

### How to Set Up SMTP Password

For Gmail, you need to use an App Password instead of your regular account password for better security:

1. Go to your Google Account settings.
2. Enable 2-Step Verification if not already enabled.
3. Navigate to 'Security' > 'App Passwords'.
4. Generate a new App Password for "Mail" and "Other" (give it a name like "Portfolio Site").
5. Copy the generated password and use it as `MAIL_PASSWORD` in your configuration or `.env` file.

**Never share your App Password or commit it to source control. Use environment variables or a `.env` file for deployment.**

## Features to Add

- [ ] Blog section
- [ ] Project filtering
- [ ] Skills progress bars
- [ ] Testimonials section
- [ ] Analytics integration

## Contributing

Feel free to fork this project and customize it for your own use. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


## Contact

Feel free to reach out to me for any questions or collaboration opportunities.

- Email: vishwanathamrish@gmail.com
- LinkedIn: https://www.linkedin.com/in/vishwanath-r-4a940721b
- GitHub: https://github.com/Vishwanathamrish

---
Made with ❤️ by Vishwanath.R