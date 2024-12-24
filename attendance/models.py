from django.db import models

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=200)
    role_description = models.CharField(max_length=200)
    hourly_wage = models.IntegerField()

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.role_name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    join_date = models.DateField()

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name


class Sites(models.Model):
     
    SITE_STATUS = [('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Under Construction', 'Under Construction')]
        
    site_name = models.CharField(max_length=200)
    site_location = models.CharField(max_length=200)
    site_status = models.CharField(max_length=200, choices=SITE_STATUS)

    class Meta:
        db_table = 'sites'

    def __str__(self):
        return self.site_name


class SiteAttendance(models.Model):
    
    ATTENDANCE_STATUS = [('absent','Absent'),('present','Present'),('leave','Leave')]


    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    no_of_hours = models.IntegerField()
    status = models.CharField(max_length=200,choices=ATTENDANCE_STATUS)   

    class Meta:
        db_table = 'site_attendance'


class EmployeeAttendance(models.Model):
     
    ATTENDANCE_STATUS = [('absent','Absent'),('present','Present'),('leave','Leave')]

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=200, choices=ATTENDANCE_STATUS)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'employee_attendance'
    
