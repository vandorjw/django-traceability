from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import batch

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(batch.BatchCreate.as_view()),
        name="batch_create",
    ),
    url(
        regex=r"^$",
        view=batch.BatchList.as_view(),
        name='batch_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=batch.BatchDetail.as_view(),
        name="batch_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(batch.BatchUpdate.as_view()),
        name="batch_update",
    ),
)
