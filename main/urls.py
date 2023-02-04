from django.urls import path
from .views import Registrview, LoginView, UserView, Logout

urlpatterns = [
    path('register',Registrview.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout',Logout.as_view())
]
