from datetime import datetime

from django.shortcuts import render, redirect

from employee.forms import AttendanceForm, AttendanceFormset
from employee.models import EmployeeAttendance, Employee


def home(request):
    return render(request, 'test.html', context=None)


def todays_attendance(request):
    attendance = EmployeeAttendance.objects.filter(date=datetime.now().strftime("%Y-%m-%d"))
    print("attendance: ", attendance)
    print("attendance: ", not attendance)
    if not attendance:
        return redirect('update_todays_attendance')
    return render(request, 'todays_attendance.html', context={'attendance': attendance})


def update_todays_attendance(request):
    context = {}
    today_attendance = EmployeeAttendance.objects.filter(date=datetime.now().strftime("%Y-%m-%d"))
    print("today_attendance: ", today_attendance)
    print("today_attendance: ", not today_attendance)
    if today_attendance:
        return redirect('todays_attendance')

    employees = Employee.objects.all()

    if request.method == 'POST':
        bulk_data = []
        for employee in employees:
            attendance = request.POST.get("attendance-" + str(employee.id), False)
            if attendance == "on":
                attendance = True

            bulk_data.append(EmployeeAttendance(employee=employee, is_present=attendance))

        EmployeeAttendance.objects.bulk_create(bulk_data)
        return redirect('todays_attendance')

    context['employees'] = employees
    return render(request, 'update_todays_attendance.html', context=context)


def all_attendance(request):
    attendance = EmployeeAttendance.objects.all().order_by('-date')
    return render(request, 'all_attendance.html', context={'attendance': attendance})
