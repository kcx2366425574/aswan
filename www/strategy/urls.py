# coding=utf8

from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView

from www.strategy.views import (
    MenuStrategyListView, MenuStrategyCreateView, MenuStrategyDestroyView,
    MenuStrategyTestView, MenuStrategyDataView, BoolStrategyListView, BoolStrategyCreateView, BoolStrategyDestroyView,
    BoolStrategyTestView, BoolStrategyDataView, FreqStrategyListView, FreqStrategyCreateView, FreqStrategyDestroyView,
    FreqStrategyTestView, FreqStrategyDataView, UserStrategyListView, UserStrategyCreateView, UserStrategyDestroyView,
    UserStrategyTestView, UserStrategyDataView
)

urlpatterns = [
    re_path(r'^$',
        RedirectView.as_view(url=reverse_lazy("strategy:menu_strategy_list"), permanent=True), name="strategy_index"),
    # 名单型策略
    re_path(r'^menu_strategy/list/$', MenuStrategyListView.as_view(), name="menu_strategy_list"),
    re_path(r'^menu_strategy/create/$', MenuStrategyCreateView.as_view(), name="menu_strategy_create"),
    re_path(r'^menu_strategy/destroy/$', MenuStrategyDestroyView.as_view(), name="menu_strategy_destroy"),
    re_path(r'^menu_strategy/test/$', MenuStrategyTestView.as_view(), name="menu_strategy_test"),
    re_path(r'^menu_strategy/data/$', MenuStrategyDataView.as_view(), name="menu_strategy_data"),

    # 布尔型策略
    re_path(r'^bool_strategy/list/$', BoolStrategyListView.as_view(), name="bool_strategy_list"),
    re_path(r'^bool_strategy/create/$', BoolStrategyCreateView.as_view(), name="bool_strategy_create"),
    re_path(r'^bool_strategy/destroy/$', BoolStrategyDestroyView.as_view(), name="bool_strategy_destroy"),
    re_path(r'^bool_strategy/test/$', BoolStrategyTestView.as_view(), name="bool_strategy_test"),
    re_path(r'^bool_strategy/data/$', BoolStrategyDataView.as_view(), name="bool_strategy_data"),

    # 时段频控策略
    re_path(r'^freq_strategy/list/$', FreqStrategyListView.as_view(), name="freq_strategy_list"),
    re_path(r'^freq_strategy/create/$', FreqStrategyCreateView.as_view(), name="freq_strategy_create"),
    re_path(r'^freq_strategy/destroy/$', FreqStrategyDestroyView.as_view(), name="freq_strategy_destroy"),
    re_path(r'^freq_strategy/test/$', FreqStrategyTestView.as_view(), name="freq_strategy_test"),
    re_path(r'^freq_strategy/data/$', FreqStrategyDataView.as_view(), name="freq_strategy_data"),

    # 限用户数型策略
    re_path(r'^user_strategy/list/$', UserStrategyListView.as_view(), name="user_strategy_list"),
    re_path(r'^user_strategy/create/$', UserStrategyCreateView.as_view(), name="user_strategy_create"),
    re_path(r'^user_strategy/destroy/$', UserStrategyDestroyView.as_view(), name="user_strategy_destroy"),
    re_path(r'^user_strategy/test/$', UserStrategyTestView.as_view(), name="user_strategy_test"),
    re_path(r'^user_strategy/data/$', UserStrategyDataView.as_view(), name="user_strategy_data"),
]
