from django.urls import path

from accounts.views import login_view, register_user, location_select, search_view, ProfileView

# Create your views her

urlpatterns = [

    path('login/', login_view, name='LoginView'),
    path('register/', register_user, name='RegisterView'),
    path('home/', location_select, name='Home'),
    path('home/search/', search_view, name='search-view'),
    path('profile/', ProfileView.as_view(), name='Profile'),
]



