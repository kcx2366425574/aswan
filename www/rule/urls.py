# coding=utf8
from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView

from www.rule.views import (
    RulesListView, RulesCreateView, RulesDestroyView, RulesChangeView, RulesDetailView, RulesTestView, RulesDataView,
    RulesThresholdEdit, RulesEdit
)


urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy("rule:list"), permanent=True), name="rule_index"),
    re_path(r'^list/$', RulesListView.as_view(), name="list"),
    re_path(r'^create/$', RulesCreateView.as_view(), name="create"),
    re_path(r'^destroy/$', RulesDestroyView.as_view(), name="destroy"),
    re_path(r'^change/$', RulesChangeView.as_view(), name="change"),
    re_path(r'^detail/$', RulesDetailView.as_view(), name="detail"),
    re_path(r'^test/$', RulesTestView.as_view(), name="test"),
    re_path(r'^data/$', RulesDataView.as_view(), name="data"),
    re_path(r'^edit/$', RulesEdit.as_view(), name="edit"),
    re_path(r'^threshold_edit/$', RulesThresholdEdit.as_view(), name="threshold_edit"),
]
