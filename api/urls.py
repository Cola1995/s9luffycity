from django.conf.urls import url,include

from api.views import course


urlpatterns = [

    # 方式1
    # url(r'^course/$', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    url(r'^course/$', course.CourseView.as_view({"get":"list"})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({"get":"retrieve"})),
]
