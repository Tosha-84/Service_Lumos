from django.shortcuts import render

from django.shortcuts import render, redirect
# from .models import Task
from .forms import ProjectForm, EmployeeForm, PropsForm, OrderForm
from django.http import HttpResponse
from .models import Project, Order, Task, Props, Employee
from django.views.generic import DetailView, UpdateView, DeleteView, View, CreateView


class ProjectDetailView(DetailView):
    model = Project
    template_name = "main/project.html"
    context_object_name = 'project'


class RefactorProjectView(UpdateView):
    model = Project
    template_name = "main/addProject.html"
    form_class = ProjectForm


class DeleteProjectView(DeleteView):
    model = Project
    success_url = '/projects'
    template_name = "main/delete_project.html"


class RefactorEmployeeView(UpdateView):
    model = Employee
    template_name = "main/add_employee.html"
    form_class = EmployeeForm


class DeleteEmployeeView(DeleteView):
    model = Employee
    success_url = '/employees'
    template_name = "main/delete_employee.html"


class RefactorPropsView(UpdateView):
    model = Props
    template_name = "main/add_props.html"
    form_class = PropsForm


class DeletePropsView(DeleteView):
    model = Props
    success_url = '/props'
    template_name = "main/delete_props.html"


class RefactorOrderView(UpdateView):
    model = Order
    template_name = "main/add_order.html"
    form_class = OrderForm


class DeleteOrderView(DeleteView):
    model = Order
    success_url = '/orders'
    template_name = "main/delete_order.html"


class CompleteOrderView(UpdateView):
    model = Order
    # success_url = '/orders'
    template_name = "main/complete_order.html"
    form_class = OrderForm



def go_to_index(request):
    return render(request, 'main/index.html')


def go_to_projects(request):
    projects = Project.objects.order_by('name')
    return render(request, 'main/projects.html', {'projects': projects})


def go_to_orders(request):
    orders = Order.objects.order_by('date')
    projects = Project.objects.order_by('name')
    # projects = Project.objects.all().filter(name='Киберы')
    # projects = Project

    return render(request, 'main/orders.html', {'orders': orders, 'projects': projects})


def go_to_order(request):
    orders = Order.objects.order_by('date')
    projects = Project.objects.order_by('name')
    print('Работает?')
    print(projects)
    return render(request, 'main/employees.html', {'orders': orders, 'projects': projects})


def complete_order(request):
    orders = Order.objects.order_by('date')
    projects = Project.objects.order_by('name')
    print('Работает?')
    print(projects)
    return render(request, 'main/employees.html', {'orders': orders, 'projects': projects})


def go_to_add_order(request):
    error = ''
    if request.method == 'POST':
        print("AAAAAAAAA")
        # print(request.data)
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save()
            project = Project.objects.get(id = form.data['project'])
            project.order.set([new_order.id])
            project.save()
            return redirect('orders')
        else:
            error = 'Форма заполнена неверно'

    form = OrderForm()
    projects = Project.objects.order_by('name')


    context = {
        'form': form,
        'error': error,
        'projects': projects,
    }
    print("Сюда прошло")
    return render(request, 'main/add_order.html', context)


# def go_to_complete_order(request):
#     error = ''
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#
#             new_order = form.save()
#             # order = Order.objects.get()
#             project = Project.objects.get(id = form.data['project'])
#             project.order.set([new_order.id])
#             project.save()
#             return redirect('orders')
#         else:
#             print("Не сработало")
#             print(form.data)
#             error = 'Форма заполнена неверно'
#
#     form = OrderForm()
#     projects = Project.objects.order_by('name')
#
#
#     context = {
#         'form': form,
#         'error': error,
#         'projects': projects,
#     }
#     print("Сюда прошло")
#     return render(request, 'main/complete_order.html', context)


def go_to_tasks(request):
    return render(request, 'main/tasks.html')


def go_to_calendar(request):
    return render(request, 'main/calendar.html')


def go_to_props(request):
    props = Props.objects.order_by('name')
    return render(request, 'main/props.html', {'props': props})


def go_to_employees(request):
    employees = Employee.objects.order_by('name')
    projects = Project.objects.order_by('name')
    print('Работает?')
    print(projects)
    return render(request, 'main/employees.html', {'employees': employees, 'projects': projects})


def go_to_statistics(request):

    projects = Project.objects.order_by('name')
    employees = Employee.objects.order_by('name')
    props = Props.objects.order_by('name')


    return render(request, 'main/statistics.html', {'projects': projects, 'employees': employees, 'props': props})


# def go_to_project(request):
#     return render(request, 'main/project.html')


def go_to_addProject(request):
    error = ''
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            print(form.data)
            return redirect('projects')
        else:
            print("Не сработало")
            print(form.data)
            error = 'Форма заполнена неверно'

    form = ProjectForm()
    employees = Employee.objects.order_by('name')

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/addProject.html', context)


def go_to_employee(request):
    return render(request, 'main/employee.html')


def go_to_add_employee(request):
    error = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            print("Уходит ли в ошибку")
            error = 'Форма заполнена неверно'
            return request

    form = EmployeeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_employee.html', context)


def go_to_prop(request):
    return render(request, 'main/prop.html')


def go_to_add_props(request):
    error = ''
    if request.method == 'POST':
        form = PropsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('props')
        else:
            print("Уходит ли в ошибку")
            error = 'Форма заполнена неверно'
            return request

    form = PropsForm()


    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/add_props.html', context)

