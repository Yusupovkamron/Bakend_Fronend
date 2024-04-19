from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher
# Create your views here.

class CourseListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            courses = Course.objects.all()
            context = {
                "courses": courses,
                "res": search
            }
            return render(request,"main/course.html", context)
        else:
            course = Course.objects.filter(title__icontains=search)
            if course:
                context = {
                    "courses": courses,
                    "res": search
                }
                return render(request, "main/course.html", context)

            else:
                context = {
                    "courses": courses,
                    "res": search
                }
                return render(request, "main/course.html", context)



class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            "teachers": teachers
        }
        return render(request,"main/teacher.html", context)


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)

        return render(request, "course_detail.html", {"course":course})




class CourseUpdateViev(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)

        return render(request,"course_update.html", {"course":course})


    def post(self, request, id):
        new_title = request.POST.get("title")
        new_description = request.POST.get("description")
        price = request.POST.get("price")
        # id = request.POST.get(id)
        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = price
        course.save()
        return redirect("course")



class CourseDeleteView(View):
    def get(self, id):
        course=Course.objects.get(id=id)
        course.delete()
        return redirect("course")


class AddNewCourse(View):
    def get(self, request):
        return render(request, "add_new_course.html")













