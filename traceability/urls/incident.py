from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import incident

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(incident.IncidentCreate.as_view()),
        name="incident_create",
    ),
    url(
        regex=r"^$",
        view=incident.IncidentList.as_view(),
        name='incident_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=incident.IncidentDetail.as_view(),
        name="incident_detail",
    ),
    url(
        regex=r"^(?P<pk>\d+)/affected/$",
        view=incident.IncidentAffected.as_view(),
        name="incident_affected",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(incident.IncidentUpdate.as_view()),
        name="incident_update",
    ),
)
