from django.urls import path
from attendance.views import *

urlpatterns = [
    path('all-employees/', AllEmployeesList.as_view(), name='all-employees'),
    path('add-employee/', AddEmployee.as_view(), name='add-employee'),
    path('all-roles/', AllRoles.as_view(), name='all-roles'),
    path('add-role/', AddRole.as_view(), name='add-role'),
    path('all-sites/', AllSites.as_view(), name='all-sites'),
    path('add-site/', AddSite.as_view(), name='add-site'),
    path('site-attendance/', SiteAttendanceList.as_view(), name='site-attendance'),
    path('employee-attendance/', EmployeeAttendanceList.as_view(), name='employee-attendance'),   
]