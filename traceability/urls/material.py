from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from traceability.views import material

urlpatterns = patterns(
    "",
    url(
        regex=r"^create/$",
        view=login_required(material.MaterialCreate.as_view()),
        name="material_create",
    ),
    url(
        regex=r"^$",
        view=material.MaterialList.as_view(),
        name='material_list',
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=material.MaterialDetail.as_view(),
        name="material_detail",
    ),
    url(
        regex=r"^update/(?P<pk>\d+)/$",
        view=login_required(material.MaterialUpdate.as_view()),
        name="material_update",
    ),
)
