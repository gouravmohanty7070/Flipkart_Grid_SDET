from django.contrib import admin
from django.urls import path,include
from landingPage.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('chat/', include('chat.urls')),
]
