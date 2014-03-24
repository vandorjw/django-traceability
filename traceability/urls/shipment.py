from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import shipment

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(shipment.ShipmentCreate.as_view()),
        name="shipment_create",
    ),
    url(
        regex=r"^$",
        view=shipment.ShipmentList.as_view(),
        name='shipment_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=shipment.ShipmentDetail.as_view(),
        name="shipment_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(shipment.ShipmentUpdate.as_view()),
        name="shipment_update",
    ),
)
