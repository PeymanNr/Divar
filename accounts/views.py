from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from accounts.forms import RegisterForm, LoginFrom, ProfileForm, EditProfileForm
from accounts.models import MyUser
from locations.models import City, Location
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    """Show user profile and all advertisements posted by user"""
    model = MyUser
    template_name = 'accounts/profile.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['user'] = self.request.user
        context['nickname'] = self.request.user.nickname
        return context


class LocationSelect(View):
    def get(self, request, *args, **kwargs):
        queryset = Location.objects.all()
        if queryset.exists():
            cities = queryset
        return render(request, 'select.html', {"cities": cities})


class LoginUserView(FormView):
    form_class = LoginFrom
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            user = authenticate(
                request, phone_number=phone_number, password=password)
            if user is None:
                context = {"error": 'Invalid Phone Number Or Password'}
                return render(request, 'accounts/login.html', context)
            login(request, user)
            return redirect('Home')
        return render(request, 'accounts/login.html', {})


class RegisterUserView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            register = RegisterForm(request.POST)
            if register.is_valid():
                register.save()
                MyUser(
                    phone_number=request.POST['phone_number'],
                    password=request.POST['password2']
                )
            return redirect('Home')

        else:
            register = RegisterForm()
        return render(request, 'accounts/register.html', {"register": register})


class SearchView(View):
    def get(self, request, *args, **kwargs):

        try:
            query = request.GET['search']
        except:
            query = None

        if query is not None:
            data = City.objects.get(name=query)

        return render(request, 'select.html', {'object': data})


class EditProfileView(UpdateView):
    """
        Edit user profile
    """
    model = MyUser
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('Profile')
    slug_field = "phone_number"

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('adv-list')
