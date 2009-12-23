"""
HTML5 input widgets.
TODO: Date widgets
"""
from django.forms.widgets import TextInput

class EmailInput(TextInput):
    input_type = 'email'
    
class URLInput(TextInput):
    input_type = 'url'

class SearchInput(TextInput):
    input_type = 'search'
    
class NumberInput(TextInput):
    input_type = 'number'
    
class RangeInput(NumberInput):
    input_type = 'range'
    
    

