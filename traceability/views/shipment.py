from django.views import generic
from traceability.models.shipment import Shipment
from traceability.forms.shipment import ShipmentCreate, ShipmentUpdate


class ShipmentDetail(generic.DetailView):
    model = Shipment


class ShipmentList(generic.ListView):
    model = Shipment
    paginate_by = 25


class ShipmentCreate(generic.CreateView):
    model = Shipment
    form_class = ShipmentCreate


class ShipmentUpdate(generic.UpdateView):
    model = Shipment
    form_class = ShipmentUpdate
