from django.urls import path
from .views import CourseListView, TeacherListView, CourseDetailView, CourseUpdateViev, CourseDeleteView, AddNewCourse
urlpatterns = [
    path("courses/", CourseListView.as_view(), name="courses"),
    path("teachers/", TeacherListView.as_view(), name="teachers"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course-detail"),
    path("update/<int:id>/", CourseUpdateViev.as_view(), name="course-update"),
    path("delete/<int:id>/", CourseDeleteView.as_view(), name="course-delete"),
    path("add_course/", AddNewCourse.as_view(), name="add-course"),
]