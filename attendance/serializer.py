from rest_framework import serializers
from .models import *

class AllEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__" 
class AllRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class AllSiteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sites
        fields = "__all__"
        

class SiteAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAttendance
        fields = "__all__"

# class EmployeeAttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeAttendance
#         fields = "__all__"
