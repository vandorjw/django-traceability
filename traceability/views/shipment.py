from django.views import generic
from traceability.models.shipment import Shipment
from traceability.forms.shipment import ShipmentCreate, ShipmentUpdate


class ShipmentDetail(generic.DetailView):
    template_name = 'traceability/shipment/shipment_detail.html'
    model = Shipment


class ShipmentList(generic.ListView):
    template_name = 'traceability/shipment/shipment_list.html'
    model = Shipment
    paginate_by = 25


class ShipmentCreate(generic.CreateView):
    template_name = 'traceability/shipment/shipment_form.html'
    model = Shipment
    form_class = ShipmentCreate


class ShipmentUpdate(generic.UpdateView):
    template_name = 'traceability/shipment/shipment_form.html'
    model = Shipment
    form_class = ShipmentUpdate
