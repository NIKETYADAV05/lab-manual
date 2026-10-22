from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('books/', views.book_list, name='book_list'),
    path('contact/', views.contact_form, name='contact_form'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='blog/login.html',
            next_page='/',
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/'),
        name='logout',
    ),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

    # Catch invalid routes
    path('<path:invalid_path>', views.not_found),
]