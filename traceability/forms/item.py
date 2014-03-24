from django.forms import ModelForm
from traceability.models.item import Item


class ItemCreate(ModelForm):
    class Meta:
        model = Item
        exclude = ('incidents', )


class ItemUpdate(ModelForm):
    class Meta:
        model = Item
        fields = ['incidents', ]
