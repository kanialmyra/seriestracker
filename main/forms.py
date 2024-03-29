from django.forms import ModelForm
from main.models import Item

class SeriesForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]