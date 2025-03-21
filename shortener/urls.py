from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Anasayfa: uç URL eklemek için kullanılan form sayfası
    path('<str:short_url>/', views.redirect_to_long_url, name='redirect'),  # Kısa URL'yi yönlendirme
]
