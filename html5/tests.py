# -*- coding: utf-8 -*-
r"""
>>> from html5.forms import *

# Field Tests   ############################################################\n
>>> i = IntegerField(max_value = 10, min_value=1)
>>> i.widget.render('name','')
u'<input max="10" type="number" name="name" min="1" />'
>>> i = IntegerField(max_value = 10, min_value=0)
>>> i.widget.render('name','')
u'<input max="10" type="number" name="name" min="0" />'
>>> i = IntegerField()
>>> i.widget.render('name','')
u'<input type="number" name="name" />'

#  Widget Tests ############################################################\n

>>> w = TextInput()
>>> w.render('email', '')
u'<input type="text" name="email" />'
>>> w = EmailInput()
>>> w.render('email', '')
u'<input type="email" name="email" />'
>>> w = TelephoneInput()
>>> w.render('phone_number', '')
u'<input type="tel" name="phone_number" />'
>>> w = URLInput()
>>> w.render('url', '')
u'<input type="url" name="url" />'
>>> w = SearchInput()
>>> w.render('q', '')
u'<input type="search" name="q" />'
>>> w = ColorInput()
>>> w.render('color', '')
u'<input type="color" name="color" />'
>>> w = NumberInput()
>>> w.render('number', '')
u'<input type="number" name="number" />'
>>> w = RangeInput()
>>> w.render('number_range', '')
u'<input type="range" name="number_range" />'
>>> w = DateInput()
>>> w.render('start_date', '')
u'<input type="date" name="start_date" />'
>>> w = MonthInput()
>>> w.render('month', '')
u'<input type="month" name="month" />'
>>> w = WeekInput()
>>> w.render('week', '')
u'<input type="week" name="week" />'
>>> w = TimeInput()
>>> w.render('time', '')
u'<input type="time" name="time" />'
>>> w = DateTimeInput()
>>> w.render('datetime', '')
u'<input type="datetime" name="datetime" />'
>>> w = DateTimeLocalInput()
>>> w.render('datetime_local', '')
u'<input type="datetime-local" name="datetime_local" />'

# Test Placeholder attr #####################################\n
>>> w = TextInput()
>>> w.render('name', '', attrs={'placeholder':'placeholder text'})
u'<input type="text" name="name" placeholder="placeholder text" />'

# Test autofocus attr #######################################\n
>>> w.render('name', '', attrs={'autofocus':'true'})
u'<input type="text" name="name" autofocus="true" />'
>>> w.use_autofocus_fallback = True
>>> w.render('name', '', attrs={'autofocus':'true', 'id': "id_name"})
u'<input type="text" name="name" id="id_name" autofocus="true" /><script>\nif (!("autofocus" in document.createElement("input"))) {\n  document.getElementById("id_name").focus();\n}\n</script>'
>>> w.render('name', '', attrs={'autofocus':'true'})
u'<input type="text" name="name" autofocus="true" />'

# should not render js when autofocus attribute is not present\n
>>> w.render('name', '', attrs={'id': "id_name"})
u'<input type="text" name="name" id="id_name" />'

# should not render js when id is blank\n
>>> w.render('name', '', attrs={'id': "", 'autofocus':'true'})
u'<input autofocus="true" type="text" name="name" id="" />'
"""