from django.urls import path

from .views import login, logout, UserEditView, PasswordsChangeView, password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', password_success, name="password_success"),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
