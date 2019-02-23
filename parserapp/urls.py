from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProvideUrl.as_view(), name='url-create'),
    path('urlkeywords/<int:pk>/', views.DetailUrl.as_view(), name='url-detail'),
]
