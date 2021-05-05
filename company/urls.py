from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('auth-company', views.auth_company, name='auth_company'),
    path('post-detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post-detail/<int:post_id>/accept/<int:a_id>', views.acceptStd, name='acceptStd'),
    path('post-detail/<int:post_id>/reject/<int:a_id>', views.rejectStd, name='rejectStd'),

    path('new-post', views.new_post, name='new-post'),
    path('edit-post/<int:post_id>/', views.internship_edit, name='internship_edit'),
    path('profile', views.company_profile, name='company-profile'),
    path('profile-edit', views.company_profile_edit, name='company-profile-edit'),
    path('student-profile/<int:std_id>/', views.std_profile, name='student-profile'),
]

