''' from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),  # This includes the URL patterns from 'chatbot/urls.py'
] '''

# chatbot_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),
    path('', RedirectView.as_view(url='/chatbot/chat/')),  # Redirect root to chatbot
]
