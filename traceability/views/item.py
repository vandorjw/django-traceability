from django.views import generic
from traceability.models.item import Item
from traceability.forms.item import ItemUpdate


class ItemDetail(generic.DetailView):
    template_name = 'traceability/item/item_detail.html'
    model = Item


class ItemList(generic.ListView):
    template_name = 'traceability/item/item_list.html'
    model = Item
    paginate_by = 25


class ItemUpdate(generic.UpdateView):
    template_name = 'traceability/item/item_form.html'
    model = Item
    form_class = ItemUpdate
