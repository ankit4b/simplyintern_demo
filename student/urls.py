from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='std_home'),
    path('internships', views.internships, name='internships'),
    path('internships/detail/<int:post_id>/', views.detail, name='detail'),
    path('internships/detail/apply/<int:post_id>/', views.internshipApplied, name='internshipApplied'),
    path('auth-student', views.auth_student, name='auth_student'),
    path('profile', views.profile, name='profile'),
    path('profileEdit', views.profileEdit, name='profileEdit'),
    path('StudentCertificateAdd', views.StudentCertificateAdd, name='StudentCertificateAdd'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('token', views.token_sent, name='token_sent'),
    path('success', views.success, name='success'),
    path('verify/<recieved_token>', views.verify_email, name='verify_email'),
    path('error', views.error_page, name='error_page'),
]