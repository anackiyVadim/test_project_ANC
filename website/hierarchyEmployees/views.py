from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import EmployeeSerializer
from .models import Employee
from .forms import OptionsEmploeeForm


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        level = self.request.query_params.get('level', None)
        parent_id = self.request.query_params.get('parent_id', None)
        if level is not None:
            level = int(level)
            if level == 1:
                return Employee.objects.filter(supervisor__isnull=True)
            elif parent_id is not None:
                return Employee.objects.filter(supervisor_id=parent_id)
        return super().get_queryset()

class InfoEmployeesFiltr(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        surname_patronymic = self.request.query_params.get('surname_patronymic', None)
        data_admission = self.request.query_params.get('data_admission', None)
        email = self.request.query_params.get('email', None)
        position = self.request.query_params.get('position', None)
        supervisor = self.request.query_params.get('supervisor', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if surname:
            queryset = queryset.filter(surname__icontains=surname)
        if surname_patronymic:
            queryset = queryset.filter(surname_patronymic__icontains=surname_patronymic)
        if data_admission:
            queryset = queryset.filter(data_admission__icontains=data_admission)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if position:
            queryset = queryset.filter(position__position_name__icontains=position)
        if supervisor:
            queryset = queryset.filter(supervisor__name__icontains=supervisor)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        return Response({
            'employees': data,
            'is_authenticated': request.user.is_authenticated
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def base():
    context = {}
    return context


def index(request):
    # filt_position = Position.objects.all()
    context = {}
    context.update(base())
    return render(request, 'hierarchyEmployees/index.html', context)

def all_info_employees(request):
    employee = Employee.objects.all()
    context = {'employee': employee}
    context.update(base())
    return render(request, 'hierarchyEmployees/all_info_employees.html', context)


@login_required
def crud(request):
    if request.method == 'POST':
        form_new_emploee = OptionsEmploeeForm(request.POST)
        if form_new_emploee.is_valid():
            form_new_emploee.save()
            return redirect('index')
    else:
        form_new_emploee = OptionsEmploeeForm()
    context = {"form_new_emploee": form_new_emploee}
    return render(request, 'hierarchyEmployees/CRUD.html', context)

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        edit_form = OptionsEmploeeForm(request.POST, instance=employee)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_info_employees')
    else:
        edit_form = OptionsEmploeeForm(instance=employee)
    context = {'edit_form': edit_form, 'employee': employee}
    return render(request, 'hierarchyEmployees/edit_employees.html', context)

def login_User(request):
    context = {}
    context.update(base())
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crud')
        else:
            return render(request, 'hierarchyEmployees/login.html',
                          {'error_message': 'Неправильное имя пользователя или пароль.'})
    else:
        return render(request, 'hierarchyEmployees/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('index')
