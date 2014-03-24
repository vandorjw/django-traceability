from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from supplier import views

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(views.SupplierCreateView.as_view()),
        name="supplier_create",
    ),
    url(
        regex=r"^$",
        view=views.SupplierListView.as_view(),
        name='supplier_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.SupplierDetailView.as_view(),
        name="supplier_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(views.SupplierUpdateView.as_view()),
        name="supplier_update",
    ),
)
