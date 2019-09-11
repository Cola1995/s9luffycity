from django.conf.urls import url,include

from api.views import course


urlpatterns = [
    url(r'^course/$', course.CourseView.as_view()),
]
