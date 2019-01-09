from django.shortcuts import render
from cbv_app.forms import school_form
from cbv_app.forms import student_form
from cbv_app.models import Student,School
from django.urls  import  reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
# Create your views here.
def register_school(request):
    if request.method == 'POST':
        schoolform=school_form(data=request.POST)
        if schoolform.is_valid():
            schoolform.save()
            return render(request,'home.html')
    else:
        schoolform=school_form()
    return render(request,'register.html',context={'schoolform':schoolform })

def register_student(request):
    if request.method == 'POST':
        studentform=student_form(data=request.POST)
        if  studentform.is_valid():
            studentform.save()
            return render(request,'home.html')
    else:
        studentform=student_form()
    return render(request,'register_student.html',context={'studentform':studentform })


class home(TemplateView):
    template_name="home.html"

class SchoolListView(ListView):
    context_object_name="schools"
    model=models.School
    template_name="list.html"

class SchoolDetailView(DetailView):
     context_object_name="schools"
     model=models.School
     template_name="detail.html"

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School
    template_name="school_form.html"


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("cbv_app:school_list")
    template_name="school_confirm_delete.html"
