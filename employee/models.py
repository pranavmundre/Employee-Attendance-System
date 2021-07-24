from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from employee.manager import UserManager


class Employee(AbstractUser):
    DEPARTMENT = (
        ("development", "Development"),
        ("testing", "Testing"),
        ("hr", "Hr")
                  )
    username = None
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=12, blank=False, null=True)
    department = models.CharField(max_length=11, choices=DEPARTMENT, blank=False, null=True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee\'s'

    def __str__(self):
        return self.email


class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField(blank=False, null=True, default=datetime.now())
    is_present = models.BooleanField(default=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Attendance'
        unique_together = (('id', 'date'),)

    def __str__(self):
        return f"{self.employee} - {self.date}"
