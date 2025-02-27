# Generated by Django 5.1.4 on 2024-12-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_employee_table_alter_employeeattendance_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteattendance',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='siteattendance',
            name='status',
            field=models.CharField(choices=[('absent', 'Absent'), ('present', 'Present'), ('leave', 'Leave')], max_length=200),
        ),
    ]
