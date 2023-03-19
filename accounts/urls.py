from django.urls import path

from accounts.views import ProfileView, SearchView, RegisterUserView, LoginUserView, LocationSelect

urlpatterns = [

    path('login/', LoginUserView.as_view(), name='LoginView'),
    path('register/', RegisterUserView.as_view(), name='RegisterView'),
    path('home/', LocationSelect.as_view(), name='Home'),
    path('home/search/', SearchView.as_view(), name='search-view'),
    path('profile/', ProfileView.as_view(), name='Profile'),
]



