# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
	userImage = forms.FileField(
		label='Select an image to upload',
		help_text='Images must be geotagged'
		)
