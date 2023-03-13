from django.urls import path
from advertisements.views import CreateAdvertisementsView, advertisement_detail, advertisements_city, \
    AdvertisementViewList

# Create your views here.

urlpatterns = [

    path('create/', CreateAdvertisementsView.as_view(), name='adv-create'),
    path('list/', AdvertisementViewList.as_view(), name='adv-list'),
    path('detail/<int:pk>/', advertisement_detail, name='adv-detail'),
    path('<int:pk>/', advertisements_city, name='adv-city'),


]
