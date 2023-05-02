from django.urls import path, re_path

from service.views import index, page

# register_converter(converts.CheckParam, "dif_type")

urlpatterns = [
    path('service/', index),
    re_path(r'^service/(?P<page_num>[0-9]{3})/$', page),
]

