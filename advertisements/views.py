from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.http import Http404
from django.views.generic import ListView
from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement
from locations.models import Location


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


class HomeView(View):
    def get(self, request, *args, **kwargs):
        advertisements = Advertisement.objects.all()
        return render(request, 'advertisement/home.html', {'advertisements': advertisements})


class AdvertisementDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        queryset = Advertisement.objects.filter(pk=pk)
        if queryset.exists():
            advertisements = queryset.first()
            return render(request, 'advertisement/detail.html', {"advertisements": advertisements})
        raise Http404


class AdvertisementCityView(View):
    def get(self, request, pk, *args, **kwargs):
        location = Location.objects.prefetch_related('ad_location').get(pk=pk)
        queryset = location.ad_location.all()
        if queryset.exists():
            advertisements = queryset
        return render(request, 'home.html', {"advertisements": advertisements})
