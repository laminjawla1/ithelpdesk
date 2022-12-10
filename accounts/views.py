from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm
from blog.models import Profile


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if password == "" and username == "":
            messages.info(request, "Fill blanks")
            return redirect("login")
        elif username == "":
            messages.info(request, "Enter User Name")
            return redirect("login")
        elif password == "":
            messages.info(request, "Enter Password")
            return redirect("login")
        elif user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")


class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = "create_user_profile_page.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = 'edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
	success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'user_profile.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	return render(request, 'password_success.html', {})

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'edit_profile.html'
	success_url = reverse_lazy('index')

	def get_object(self):
		return self.request.user
