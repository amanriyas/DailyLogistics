from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.http import Http404, JsonResponse
from rest_framework.views import APIView


# Create your views here.


############# Employee Views ####################
class AllEmployeesList(APIView):
    def get (self, request):
       all_employees = Employee.objects.all()
       serializer = AllEmployeeSerializer(all_employees, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddEmployee(APIView):
    def post(self, request):
        data = request.data
        serializer = AllEmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Employee added successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class EditEmployee(APIView):

    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = AllEmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Employee updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteEmployee(APIView):
    def delete(self, request, pk):
        Employee.objects.filter(pk=pk).delete()
        return JsonResponse({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



############# Role Views ####################
class AllRoles(APIView):
    def get (self, request):
       all_roles = Role.objects.all()
       serializer = AllRoleSerializer(all_roles, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)    

class AddRole(APIView):
    def post(self, request):
        data = request.data
        serializer = AllRoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Role added successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class EditRole(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Role, pk=pk)

    def put(self, request, pk):
        role = self.get_object(pk)
        serializer = AllRoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Role updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class DeleteRole(APIView):
    def delete(self, request,pk):
        Role.objects.filter(pk=pk).delete()

        return JsonResponse({"message": "Role deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    
    
############# Site Views ####################
class AllSites(APIView):
    def get (self, request):
       all_sites = Sites.objects.all()
       serializer = AllSiteSerializer(all_sites, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)  

class AddSite(APIView):
    def post(self, request):
        data = request.data
        serializer = AllSiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            response_data = {
                "message": "Site added successfully",
                "data": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class EditSite(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Role, pk=pk)
    

    def put(self, request, pk):
        site = self.get_object(pk)
        serializer = AllSiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Site updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteSite(APIView):
    def delete(self, request, pk):
        Sites.objects.filter(pk=pk).delete()
        return JsonResponse({"message": "Site deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    

############# Attendance Views ####################
class SiteAttendanceList(APIView):
    def get (self, request):
       all_site_attendance = SiteAttendance.objects.all()
       serializer = SiteAttendanceSerializer(all_site_attendance, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    
class EmployeeAttendanceList(APIView):
    def get (self, request):
       all_employee_attendance = EmployeeAttendance.objects.all()
       serializer = EmployeeAttendanceSerializer(all_employee_attendance, many=True)
       return JsonResponse(serializer.data, status=status.HTTP_200_OK)    
    



         