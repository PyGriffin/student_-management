from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('这里必须是一个数字')

    class Meta:
        model = Student
        fields = (
            'name','sex','profession',
            'email','qq','phone'
        )