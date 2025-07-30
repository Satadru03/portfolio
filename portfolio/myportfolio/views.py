from django.shortcuts import render, redirect
from .models import Fact, Skill, Service
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    # Handle contact form submission
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name} <{email}>\n Subject: {subject}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # from email
                ['satadru03@gmail.com'], # to email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent. Thank you!")
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")

        return redirect('index')  # reload the same page (update URL name accordingly)

    # Your usual homepage content
    fact1 = Fact(heading='Years of Experience', emoji='bi bi-calendar', count=0, data_delay=0)
    fact2 = Fact(heading='Machine Learning Projects', emoji='bi bi-cpu', count=4, data_delay=100)
    fact3 = Fact(heading='Technical Skills', emoji='bi bi-tools', count=10, data_delay=200)
    fact4 = Fact(heading='Hackathons & Competitions', emoji='bi bi-trophy', count=5, data_delay=100)
    facts = [fact1, fact2, fact3, fact4]

    skill1 = Skill(name='Python', value=90)
    skill2 = Skill(name='C', value=85)
    skill3 = Skill(name='NumPy & pandas', value=85)
    skill4 = Skill(name='scikit-learn', value=80)
    skill5 = Skill(name='TensorFlow', value=70)
    skill6 = Skill(name='Data Visualization (Seaborn/Matplotlib)', value=80)
    skills_row = [[skill1, skill2, skill3], [skill4, skill5, skill6]]

    services1 = Service(delay=0, icon='bi bi-bar-chart', title='Machine Learning',
                        description='Building predictive models, working with real-world data, and applying NLP and computer vision techniques.')
    services2 = Service(delay=100, icon='bi bi-pie-chart', title='Data Analysis & Visualization',
                        description='Cleaning, analyzing, and visualizing datasets using Python libraries like pandas, matplotlib, and seaborn.')
    services4 = Service(delay=300, icon='bi bi-journal-code', title='Technical Documentation',
                        description='Creating clean and clear documentation for ML pipelines, APIs, and datasets.')
    services = [services1, services2, services4]

    context = {
        'facts': facts,
        'skills_row': skills_row,
        'services': services,
        'year': datetime.now().year,
        'age': datetime.now().year - 2003,
    }

    return render(request, 'index.html', context)
