from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):
    students = Student.get_all()
    if request.method == 'post':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # 将数据添加到数据库
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.profession = cleaned_data['profession']
            student.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        print('1212')
        form = StudentForm()

    context = {
        'form':form,
        'students':students
    }

    return render(request,'index.html',context=context)
