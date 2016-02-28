from django.http import HttpResponse
from main.models import Course
from .forms import CourseForm
from django.shortcuts import render, get_object_or_404, redirect


def course_list(request):
    courses = Course.objects.filter()
    return render(request, 'main/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'main/course_detail.html', {'course': course})

def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'main/course_edit.html', {'form': form})

def course_edit(request, pk):
    post = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=post)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=post)
    return render(request, 'main/course_edit.html', {'form': form})
