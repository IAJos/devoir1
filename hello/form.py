from django import forms
from hello.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        # fields = ['name', 'email', 'site', 'creation_date', 'start_time', 'student_number', 'tuition_fees', 'sector', 'is_eed']
        # fields = ['name', 'email', 'password', 'site', 'creation_date', 'start_time', 'student_number', 'tuition_fees',
        #           'sector', 'eed_school']
        fields = '__all__'
