from django.shortcuts import render
from .models import Fact, Skill, Service, Testimonial

def index(request):
    
    fact1 = Fact()
    fact1.heading = 'Years of Experience'
    fact1.emoji = 'bi bi-calendar'
    fact1.count = 1
    fact1.data_delay = 0

    fact2 = Fact()
    fact2.heading = 'Projects Completed'
    fact2.emoji = 'bi bi-file-earmark-bar-graph'
    fact2.count = 5
    fact2.data_delay = 100

    fact3 = Fact()
    fact3.heading = 'Clients or Companies Worked With'
    fact3.emoji = 'bi bi-emoji-smile'
    fact3.count = 0
    fact3.data_delay = 200

    fact4 = Fact()
    fact4.heading = 'Countries Visited or Worked In'
    fact4.emoji = 'bi bi-airplane'
    fact4.count = 1
    fact4.data_delay = 300

    facts = [fact1, fact2, fact3, fact4]

    skill1 = Skill()
    skill1.name = 'HTML'
    skill1.value = 70

    skill2 = Skill()
    skill2.name = 'CSS'
    skill2.value = 50

    skill3 = Skill()
    skill3.name = 'Javascript'
    skill3.value = 40

    skill4 = Skill()
    skill4.name = 'C'
    skill4.value = 90

    skill5 = Skill()
    skill5.name = 'python'
    skill5.value = 90

    skill6 = Skill()
    skill6.name = 'Django'
    skill6.value = 70

    skills_row = [[skill1, skill2, skill3], [skill4, skill5, skill6]]

    services1 = Service()
    services1.delay = 0
    services1.icon = 'bi bi-briefcase'
    services1.title = 'Django Web Development'
    services1.description = 'Custom web application development using the Django framework. Building and maintaining database-driven websites. E-commerce platform development with Django.'

    services2 = Service()
    services2.delay = 100
    services2.icon = 'bi bi-code-slash'
    services2.title = 'Full-Stack Development'
    services2.description = 'End-to-end development of web applications, covering both front-end and back-end aspects.'

    services3 = Service()
    services3.delay = 200
    services3.icon = 'bi bi-bar-chart'
    services3.title = 'Machine Learning Services'
    services3.description = 'Developing machine learning models for predictive analysis. Natural Language Processing (NLP) solutions for text data. Computer Vision applications for image and video analysis.'

    services4 = Service()
    services4.delay = 300
    services4.icon = 'bi bi-bar-chart'
    services4.title = 'Data Analysis and Visualization'
    services4.description = 'Analyzing and interpreting data to derive actionable insights. Designing interactive dashboards for data visualization.'

    services5 = Service()
    services5.delay = 400
    services5.icon = 'bi bi-file-code'
    services5.title = 'Code Review and Optimization'
    services5.description = 'Reviewing existing codebases for best practices and optimization opportunities. Performance tuning of applications for better efficiency.'

    services6 = Service()
    services6.delay = 500
    services6.icon = 'bi bi-file-earmark-text'
    services6.title = 'Technical Documentation'
    services6.description = 'Creating comprehensive documentation for projects, APIs, or codebases.'

    services = [services1, services2, services3, services4, services5, services6]

    testimonial1 = Testimonial()
    testimonial1.data_delay = 0
    testimonial1.description = ''
    testimonial1.image_location = 'assets/img/testimonials/testimonials-1.jpg'
    testimonial1.name = 'Ben'
    testimonial1.work = 'noob'

    testimonial2 = Testimonial()
    testimonial2.data_delay = 100
    testimonial2.description = ''
    testimonial2.image_location = 'assets/img/testimonials/testimonials-2.jpg'
    testimonial2.name = 'Shek'
    testimonial2.work = 'lol'

    testimonials = [testimonial1, testimonial2]

    return render(request, 'index.html', {'facts': facts, 'skills_row': skills_row, 'services': services, 'testimonials' : testimonials})