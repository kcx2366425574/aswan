# coding=utf8
from django.views.generic import RedirectView
from django.urls import reverse_lazy, re_path
from .views import (HitListDetailView, RuleStrategyMapView, AuditLogListView)

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy("log_manage:hit_list_detail"), permanent=True),
         name="log_manage_index"),

    re_path(r'^hit/list_detail/$', HitListDetailView.as_view(), name="hit_list_detail"),
    re_path(r'^rule_strategy_map/$', RuleStrategyMapView.as_view(), name="rule_strategy_map"),
    re_path(r'^audit_log_list/$', AuditLogListView.as_view(), name='audit_logs')
]
