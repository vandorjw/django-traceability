"""Defaults urls for Traceability"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    url(r'^batch/', include(
        'traceability.urls.batch', namespace='batch', )),
    url(r'^customer/', include(
        'traceability.urls.customer', namespace='customer', )),
    url(r'^employee/', include(
        'traceability.urls.employee', namespace='employee', )),
    url(r'^incident/', include(
        'traceability.urls.incident', namespace='incident', )),
    url(r'^item/', include(
        'traceability.urls.item', namespace='item', )),
    url(r'^material/', include(
        'traceability.urls.material', namespace='material', )),
    url(r'^shipment/', include(
        'traceability.urls.shipment', namespace='shipment', )),
    url(r'^supplier/', include(
        'traceability.urls.supplier', namespace='supplier', )),
)
