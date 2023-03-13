from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.forms import RegisterForm, ProfileForm
from accounts.models import MyUser, Profile
from locations.models import City, Location


def location_select(request):
    queryset = Location.objects.all()
    if queryset.exists():
        cities = queryset
    return render(request, 'select.html', {"cities": cities})


def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is None:
            context = {"error": 'Invalid Phone Number Or Password'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect(location_select)
    return render(request, 'accounts/login.html', {})


def register_user(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            new_user = MyUser(phone_number=request.POST['phone_number'],
                              password=request.POST['password2']
                              )
            new_profile = Profile(user=new_user,
                                  first_name=request.POST['first_name'],
                                  last_name=request.POST['last_name'],
                                  )
            return render(request, 'accounts/profile.html')
    else:
        register = RegisterForm()
    return render(request, 'accounts/register.html', {"register": register})


def search_view(request):
    data = City.objects.all()
    try:
        query = request.GET['search']
    except:
        query = None

    if query is not None:
        data = City.objects.get(name=query)

    return render(request, 'select.html', {'object': data})


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('adv-list')






