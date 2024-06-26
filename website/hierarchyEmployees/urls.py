from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, InfoEmployeesFiltr
from . import views

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'all_employees', InfoEmployeesFiltr, basename='employees_filter')

urlpatterns = [
    path('api/', include(router.urls)),

    path("", views.index, name="index"),
    path("all_info_employees", views.all_info_employees, name="all_info_employees"),
    path("crud/", views.crud, name="crud"),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),

    path("login_User/", views.login_User, name="login_User"),
    path("logout", views.logoutView, name="account_logout"),
]
