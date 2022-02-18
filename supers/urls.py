from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk/>', views.supers_list),
    path('optional params/', views.supers_list)
]