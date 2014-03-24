from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from traceability.views import item

urlpatterns = patterns(
    "",
    url(
        regex=r"^$",
        view=item.ItemList.as_view(),
        name='item_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=item.ItemDetail.as_view(),
        name="item_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(item.ItemUpdate.as_view()),
        name="item_update",
    ),

)
