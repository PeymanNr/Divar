from django.urls import path
from advertisements.views import CreateAdvertisementsView, AdvertisementDetailView, AdvertisementCityView, \
    AdvertisementViewList

# Create your views here.

urlpatterns = [

    path('create/', CreateAdvertisementsView.as_view(), name='adv-create'),
    path('list/', AdvertisementViewList.as_view(), name='adv-list'),
    path('detail/<int:pk>/', AdvertisementDetailView.as_view(), name='adv-detail'),
    path('<int:pk>/', AdvertisementCityView.as_view(), name='adv-city'),


]
