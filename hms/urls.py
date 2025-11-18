from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home (landing page)
    path('', home, name='home'),

    # Reception App
    path('reception/', include('reception.urls')),

     #nursing app
    path('nursing/', include('nursing.urls')),  

     #doctor app
    path('doctor/', include('doctor.urls')),

    # Pharmacy App
    path('pharmacy/', include('pharmacy.urls')),

    # Laboratory App
    path('lab/', include('lab.urls')),

    path('billing/', include('billing.urls')),

    # Django Admin Site
    path('admin/', admin.site.urls),

    # Authentication (Login / Logout)
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]
