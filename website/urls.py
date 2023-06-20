from django.urls import path
from website import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("read_more/<id>", views.read_more, name="read_more"),
    path("user_contact/", views.user_contact, name="user_contact"),
    path("get_quote/", views.get_quote, name="get_quote"),
]
