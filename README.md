# Satadru Halder — Personal Portfolio Website

This is my personal portfolio website showcasing my skills, projects, education, and achievements. Built with HTML, CSS (Bootstrap), and served via Django on PythonAnywhere, it’s a central hub for everything about me.

🔗 Live: [https://satadru03.pythonanywhere.com/](https://satadru03.pythonanywhere.com/)

---

## ✨ Features

- Hero section with dynamic role typing
- About section with profile and background
- Skills & tools I’ve used in real-world projects
- Project showcase with descriptions
- Achievements from competitions and hackathons
- Resume download & view options
- Contact information for collaboration or freelance

---

## 🧠 Technologies Used

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Templating**: Django Template Engine
- **Backend**: Django (lightweight use for deployment + templating)
- **Hosting**: PythonAnywhere
- **Version Control**: Git & GitHub

---

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Satadru03/portfolio.git
   cd portfolio/portfolio
   ```
   
2. **Create and activate a virtual environment**  

   **On Windows CMD**  
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **On PowerShell**  
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

    **On macOS/Linux**  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

5. **Navigate to the Django project folder**  
    ```bash
    cd portfolio
    ```

6. **Collect static files**  
    ```bash
    python manage.py collectstatic
    ```

7. **Run migrations**  
    ```bash
    python manage.py migrate
    ```

8. **Start the development server**  
    ```bash
    python manage.py runserver
    ```

9. **Visit your site**  
    Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Project Structure
```
portfolio/
├── myportfolio/           # Django project (settings, urls, wsgi)
├── portfolio/             # Django app (views, templates)
│   └── templates/
│       └── index.html
├── static/                # Custom static assets (CSS, JS, images)
├── staticfiles/           # Collected static files for production
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignored files
├── README.md              # This README
└── manage.py              # Django management script
```
---

## 📄 License

This project is free to use for educational or portfolio purposes. If you find it useful, feel free to fork or build on top of it — just consider giving credit.

---

## 🙋‍♂️ Contact

- 📧 Email: [satadruhalder03@gmail.com](mailto:satadruhalder03@gmail.com)
- 🌐 Portfolio: [https://satadru03.pythonanywhere.com/](https://satadru03.pythonanywhere.com/)
- 🔗 LinkedIn: [linkedin.com/in/satadru-h-791415213](https://www.linkedin.com/in/satadru-h-791415213/)
- 🐙 GitHub: [github.com/Satadru03](https://github.com/Satadru03)
