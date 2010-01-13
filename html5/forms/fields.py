from django.forms.fields import IntegerField as DjangoIntegerField

from html5.forms import NumberInput

class IntegerField(DjangoIntegerField):
    widget = NumberInput

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), returns a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        attrs = {}
        if self.min_value is not None:
            attrs['min'] = self.min_value
        if self.max_value is not None:
            attrs['max'] = self.max_value
        return attrs
