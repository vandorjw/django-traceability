from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import supplier

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(supplier.SupplierCreate.as_view()),
        name="supplier_create",
    ),
    url(
        regex=r"^$",
        view=supplier.SupplierList.as_view(),
        name='supplier_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=supplier.SupplierDetail.as_view(),
        name="supplier_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(supplier.SupplierUpdate.as_view()),
        name="supplier_update",
    ),
)
