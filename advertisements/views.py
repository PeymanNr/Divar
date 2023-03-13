from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement
from locations.models import City, Location


class AdvertisementViewList(ListView):

    model = Advertisement
    template_name = 'advertisement/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class CreateAdvertisementsView(FormView):
    form_class = AdvertisementForm
    template_name = 'advertisement/create.html'
    success_url = reverse_lazy('adv-list')

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            return super().form_valid(form)


def home_view(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/home.html', {'advertisements': advertisements})


def advertisement_detail(request, pk):
    queryset = Advertisement.objects.filter(pk=pk)
    if queryset.exists():
        advertisements = queryset.first()
        return render(request, 'advertisement/detail.html', {"advertisements": advertisements})
    raise Http404


def advertisements_city(request, pk):
    location = Location.objects.prefetch_related('ad_location').get(pk=pk)
    queryset = location.ad_location.all()
    if queryset.exists():
        advertisements = queryset
    return render(request, 'home.html', {"advertisements": advertisements})


