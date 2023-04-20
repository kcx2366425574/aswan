# coding=utf8

from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView

from www.bk_config.views import (
    ConfigSourceListView, ConfigSourceAjaxView, ConfigSourceCreateView,
    ConfigDestroyView
)

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy("config:source_list"), permanent=True), name="config_index"),

    re_path(r'^source/list/$', ConfigSourceListView.as_view(), name="source_list"),
    re_path(r'^source/ajax/$', ConfigSourceAjaxView.as_view(), name="source_ajax"),
    re_path(r'^source/create/$', ConfigSourceCreateView.as_view(), name="source_create"),
    re_path(r'^source/destroy/$', ConfigDestroyView.as_view(), name="source_destroy"),
]
