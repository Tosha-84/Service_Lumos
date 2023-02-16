from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.go_to_index, name='notifications'),
    path('projects', views.go_to_projects, name='projects'),
    path('orders', views.go_to_orders, name='orders'),
    path('tasks', views.go_to_tasks, name='tasks'),
    path('calendar', views.go_to_calendar, name='calendar'),
    path('props', views.go_to_props, name='props'),
    path('employees', views.go_to_employees, name='employees'),
    path('statistics', views.go_to_statistics, name='statistics'),

    path('addProject', views.go_to_addProject, name='addProject'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project'),
    path('projects/<int:pk>/refactor', views.RefactorProjectView.as_view(), name='refactor_project'),
    path('projects/<int:pk>/delete', views.DeleteProjectView.as_view(), name='delete_project'),

    path('add_order', views.go_to_add_order, name='add_order'),
    path('order', views.go_to_order, name='order'),
    path('orders/<int:pk>/refactor', views.RefactorOrderView.as_view(), name='refactor_order'),
    path('orders/<int:pk>/complete', views.CompleteOrderView.as_view(), name='complete_order'),
    # path('orders/<int:pk>/complete1', views.go_to_complete_order, name='go_to_complete_order'),
    path('orders/<int:pk>/delete', views.DeleteOrderView.as_view(), name='delete_order'),


    path('add_employee', views.go_to_add_employee, name='add_employee'),
    path('employee', views.go_to_employee, name='employee'),
    path('employees/<int:pk>/refactor', views.RefactorEmployeeView.as_view(), name='refactor_employee'),
    path('employees/<int:pk>/delete', views.DeleteEmployeeView.as_view(), name='delete_employee'),

    path('add_props', views.go_to_add_props, name='add_props'),
    path('props', views.go_to_prop, name='props'),
    path('props/<int:pk>/refactor', views.RefactorPropsView.as_view(), name='refactor_props'),
    path('props/<int:pk>/delete', views.DeletePropsView.as_view(), name='delete_props'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
