from rest_framework import serializers
from .models import *

class AllEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'role_id', 'join_date']

class AllRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_name', 'role_description', 'hourly_wage']

class AllSiteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sites
        fields = ['site_name', 'site_location', 'site_status']
        

class SiteAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAttendance
        fields = ['employee_id', 'site_id', 'date', 'no_of_hours', 'status']


class EmployeeAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAttendance
        fields = ['employee_id', 'site_id', 'date', 'status']
