from django.urls import path
from attendance.views import *

urlpatterns = [
    path('all-employees/', AllEmployeesList.as_view(), name='all-employees'),
    path('add-employee/', AddEmployee.as_view(), name='add-employee'),
    path('edit-employee/<int:pk>/', EditEmployee.as_view(), name='edit-employee'),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view(), name='delete-employee'),

    path('all-roles/', AllRoles.as_view(), name='all-roles'),
    path('add-role/', AddRole.as_view(), name='add-role'),
    path('edit-role/<int:pk>/', EditRole.as_view(), name='edit-role'),
    path('delete-role/<int:pk>/', DeleteRole.as_view(), name='delete-role'),

    path('all-sites/', AllSites.as_view(), name='all-sites'),
    path('add-site/', AddSite.as_view(), name='add-site'),
    path('edit-site/<int:pk>/', EditSite.as_view(), name='edit-site'),
    path('delete-site/<int:pk>/', DeleteSite.as_view(), name='delete-site'),

    path('site-attendance/', SiteAttendanceList.as_view(), name='site-attendance'),
    path('add-site-attendance/', AddSiteAttendance.as_view(), name='add-site-attendance'),

    path('employee-attendance/', EmployeeAttendanceList.as_view(), name='employee-attendance'),   
]