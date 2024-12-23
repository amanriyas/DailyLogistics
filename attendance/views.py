from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.http import Http404, JsonResponse
from rest_framework.views import APIView


# Create your views here.

class AllEmployeesList(APIView):
    def get (self, request):
       all_employees = Employee.objects.all()
       serializer = AllEmployeeSerializer(all_employees, many=True)
       sample_employee = {
        "name": "John Doe",
        "role_id": 1,
        "join_date": "2020-01-01"
        }
       return JsonResponse(sample_employee, status=status.HTTP_200_OK)
    
class AllRoles(APIView):
    def get (self, request):
       all_roles = Role.objects.all()
       serializer = AllRoleSerializer(all_roles, many=True)
       
       sample_role = {
        "role_name": "Manager",
        "role_description": "Manages the site",
        "hourly_wage": 1000
        }


       return JsonResponse(sample_role, status=status.HTTP_200_OK)    
    

class AllSites(APIView):
    def get (self, request):
       all_sites = Sites.objects.all()
       serializer = AllSiteSerializer(all_sites, many=True)
       
       sample_site = {
        "site_name": "Site 1",
        "site_location": "Location 1",
        "site_status": "Active"
        }
       return JsonResponse(sample_site, status=status.HTTP_200_OK)  


class SiteAttendanceList(APIView):
    def get (self, request):
       all_site_attendance = SiteAttendance.objects.all()
       serializer = SiteAttendanceSerializer(all_site_attendance, many=True)
       
       sample_site_attendance = {
        "employee_id": 1,
        "site_id": 1,
        "date": "2020-01-01",
        "no_of_hours": 8,
        "status": "Present"
        }
       return JsonResponse(sample_site_attendance, status=status.HTTP_200_OK)
    
class EmployeeAttendanceList(APIView):
    def get (self, request):
       all_employee_attendance = EmployeeAttendance.objects.all()
       serializer = EmployeeAttendanceSerializer(all_employee_attendance, many=True)
       
       sample_employee_attendance = {
        "employee_id": 1,
        "site_id": 1,
        "date": "2020-01-01",
        "status": "Present"
        }
       return JsonResponse(sample_employee_attendance, status=status.HTTP_200_OK)    
    
class AddEmployee(APIView):
    def post(self, request):
        data = request.data
        serializer = AllEmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddRole(APIView):
    def post(self, request):
        data = request.data
        serializer = AllRoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddSite(APIView):
    def post(self, request):
        data = request.data
        serializer = AllSiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            