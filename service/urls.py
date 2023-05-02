from django.urls import path, re_path

from service.views import index, page, about

# register_converter(converts.CheckParam, "dif_type")

urlpatterns = [
    path('service/', index, name='service'),
    re_path(r'^service/(?P<page_num>[0-9]{3})/$', page),
    path('about/<int:id>', about, name='about')
]

