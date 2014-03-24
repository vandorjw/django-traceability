from django import forms
from traceability.models.shipment import Shipment
from traceability.models.item import Item

class ShipmentCreate(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Item.inventory.all())
    
    class Meta:
        model = Shipment
        
    def __init__(self, *args, **kwargs):
        super(ShipmentCreate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['items'].initial = self.instance.item_set.all()

    def save(self, *args, **kwargs):
        instance = super(ShipmentCreate, self).save()
        self.fields['items'].initial.update(shipment=None)
        self.cleaned_data['items'].update(shipment=instance)
        return instance


class ShipmentUpdate(forms.ModelForm):
    class Meta:
        model = Shipment
