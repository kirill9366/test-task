from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path(
        'sign-in/',
        LoginView.as_view(
            template_name='signin.html',
            success_url='/',
        ),
        name='signin'
    )
]
