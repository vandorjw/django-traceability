from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import employee

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(employee.EmployeeCreate.as_view()),
        name="employee_create",
    ),
    url(
        regex=r"^$",
        view=employee.EmployeeList.as_view(),
        name='employee_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=employee.EmployeeDetail.as_view(),
        name="employee_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(employee.EmployeeUpdate.as_view()),
        name="employee_update",
    ),
)
