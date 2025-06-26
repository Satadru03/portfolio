from django.shortcuts import render
from .models import Fact, Skill, Service, Testimonial
from datetime import datetime

def index(request):
    
    fact1 = Fact()
    fact1.heading = 'Years of Experience'
    fact1.emoji = 'bi bi-calendar'
    fact1.count = 0
    fact1.data_delay = 0

    fact2 = Fact()
    fact2.heading = 'Machine Learning Projects'
    fact2.emoji = 'bi bi-cpu'
    fact2.count = 4
    fact2.data_delay = 100

    fact3 = Fact()
    fact3.heading = 'Technical Skills'
    fact3.emoji = 'bi bi-tools'
    fact3.count = 10
    fact3.data_delay = 200

    fact4 = Fact()
    fact4.heading = 'Hackathons & Competitions'
    fact4.emoji = 'bi bi-trophy'
    fact4.count = 5
    fact4.data_delay = 100

    facts = [fact1, fact2, fact3, fact4]

    skill1 = Skill()
    skill1.name = 'Python'
    skill1.value = 90

    skill2 = Skill()
    skill2.name = 'C'
    skill2.value = 85

    skill3 = Skill()
    skill3.name = 'NumPy & pandas'
    skill3.value = 85

    skill4 = Skill()
    skill4.name = 'scikit-learn'
    skill4.value = 80

    skill5 = Skill()
    skill5.name = 'TensorFlow'
    skill5.value = 70

    skill6 = Skill()
    skill6.name = 'Data Visualization (Seaborn/Matplotlib)'
    skill6.value = 80

    skills_row = [[skill1, skill2, skill3], [skill4, skill5, skill6]]

    services1 = Service()
    services1.delay = 0
    services1.icon = 'bi bi-bar-chart'
    services1.title = 'Machine Learning'
    services1.description = 'Building predictive models, working with real-world data, and applying NLP and computer vision techniques.'

    services2 = Service()
    services2.delay = 100
    services2.icon = 'bi bi-pie-chart'
    services2.title = 'Data Analysis & Visualization'
    services2.description = 'Cleaning, analyzing, and visualizing datasets using Python libraries like pandas, matplotlib, and seaborn.'

    # services3 = Service()
    # services3.delay = 200
    # services3.icon = 'bi bi-code-slash'
    # services3.title = 'Code Review & Optimization'
    # services3.description = 'Writing clean, efficient code and reviewing others\' code for performance and maintainability.'

    services4 = Service()
    services4.delay = 300
    services4.icon = 'bi bi-journal-code'
    services4.title = 'Technical Documentation'
    services4.description = 'Creating clean and clear documentation for ML pipelines, APIs, and datasets.'

    services = [services1, services2, services4]

    # testimonial1 = Testimonial()
    # testimonial1.data_delay = 0
    # testimonial1.description = ''
    # testimonial1.image_location = 'assets/img/testimonials/testimonials-1.jpg'
    # testimonial1.name = 'Ben'
    # testimonial1.work = 'noob'

    # testimonial2 = Testimonial()
    # testimonial2.data_delay = 100
    # testimonial2.description = ''
    # testimonial2.image_location = 'assets/img/testimonials/testimonials-2.jpg'
    # testimonial2.name = 'Shek'
    # testimonial2.work = 'lol'

    # testimonials = [testimonial1, testimonial2]

    return render(request, 'index.html', {'facts': facts, 'skills_row': skills_row, 'services': services, 'year': datetime.now().year})