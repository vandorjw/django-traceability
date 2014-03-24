from django.views import generic
from traceability.models.item import Item
from traceability.forms.item import ItemUpdate


class ItemDetail(generic.DetailView):
    model = Item


class ItemList(generic.ListView):
    model = Item
    paginate_by = 25


class ItemUpdate(generic.UpdateView):
    model = Item
    form_class = ItemUpdate
