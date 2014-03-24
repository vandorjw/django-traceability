from django import forms
from django.forms.models import BaseInlineFormSet
from django.forms.models import inlineformset_factory
from django.core.exceptions import ValidationError
from traceability.models.batch import Batch, Input


class BatchUpdate(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['incidents', ]


class BatchCreate(forms.ModelForm):
    start_serial = forms.IntegerField(max_value=99999)
    end_serial = forms.IntegerField(max_value=99999)

    class Meta:
        model = Batch
        exclude = ('incidents', )


InputFormSet = inlineformset_factory(
    Batch,
    Input,
    extra=1, )
