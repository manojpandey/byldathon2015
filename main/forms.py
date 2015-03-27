from django import forms
from models import Contact, Resource
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact


class RForm(forms.ModelForm):

	class Meta:
		model = Resource