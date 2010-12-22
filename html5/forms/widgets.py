"""
HTML5 input widgets.
TODO: Date widgets
"""
from django.forms.widgets import Input

class HTML5Input(Input):
    use_autofocus_fallback = False
    
    def render(self, *args, **kwargs):
        rendered_string = super(HTML5Input, self).render(*args, **kwargs)
        # js only works when an id is set
        if self.use_autofocus_fallback and kwargs.has_key('attrs') and kwargs['attrs'].get("id",False) and kwargs['attrs'].has_key("autofocus"):
            rendered_string += """<script>
if (!("autofocus" in document.createElement("input"))) {
  document.getElementById("%s").focus();
}
</script>""" % kwargs['attrs']['id']
        return rendered_string

class TextInput(HTML5Input):
    input_type = 'text'

class EmailInput(HTML5Input):
    input_type = 'email'

class TelephoneInput(HTML5Input):
    input_type = 'tel'

class URLInput(HTML5Input):
    input_type = 'url'

class SearchInput(HTML5Input):
    input_type = 'search'

class ColorInput(HTML5Input):
    """
    Not supported by any browsers at this time (Jan. 2010).
    """
    input_type = 'color'
    
class NumberInput(HTML5Input):
    input_type = 'number'
    
class RangeInput(NumberInput):
    input_type = 'range'
    
class DateInput(HTML5Input):
    input_type = 'date'
    
class MonthInput(HTML5Input):
    input_type = 'month'

class WeekInput(HTML5Input):
    input_type = 'week'

class TimeInput(HTML5Input):
    input_type = 'time'

class DateTimeInput(HTML5Input):
    input_type = 'datetime'

class DateTimeLocalInput(HTML5Input):
    input_type = 'datetime-local'
