from django import forms
from django.forms import inlineformset_factory

from employee.models import EmployeeAttendance, Employee


class AttendanceForm(forms.ModelForm):
    employee = forms.CharField(max_length=200)
    is_present = forms.BooleanField(label="ss")
    aa = forms.BooleanField(label="ss")

    class Meta:
        model = EmployeeAttendance
        fields = ('employee', 'is_present',)
        # fields = '__all__'

    # def save(self, commit=True, *args, **kwargs):
    #     print("Dd: ", kwargs)
    #
    #     return None


AttendanceFormset = inlineformset_factory(Employee, EmployeeAttendance, 
                                          fields=('is_present', 'employee'),
                                          can_delete=False, )
