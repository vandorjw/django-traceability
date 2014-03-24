from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import customer

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(customer.CustomerCreate.as_view()),
        name="customer_create",
    ),
    url(
        regex=r"^$",
        view=customer.CustomerList.as_view(),
        name='customer_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=customer.CustomerDetail.as_view(),
        name="customer_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(customer.CustomerUpdate.as_view()),
        name="customer_update",
    ),
)
