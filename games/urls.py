from django.urls import path
from.import views

urlpatterns =[
    path("",views.index,name="index"),
    path("about", views.about, name="about"),
    path("404",views.html, name="404"),
    path("contact",views.contact, name="contact"),
    path("feature",views.feature, name="feature"),
    path("service",views.service, name="service"),
    path("appointment",views.appointment, name="appointment"),
    path("testimonial",views.testimonial, name="testimonial.html"),
    path("team",views.team, name="team.html"),
]