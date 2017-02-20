from django.shortcuts import render, HttpResponse, redirect

from .models import Course

# Create your views here.
def index(request):
	all_courses = Course.objects.all()
	context = {
		"courses": all_courses
	}
	return render(request, 'index.html', context)

def create(request):
	if request.method == "POST":
		Course.objects.create(name=request.POST["name"], description=request.POST["description"])
		return redirect('/')

def delete(request, course_id):
	course_to_delete = Course.objects.get(id=course_id)
	course_to_delete.delete()
	return redirect('/')