from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	title = forms.CharField(
				label='',
				widget=forms.TextInput(attrs={"placeholder":"Your title"}))
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
			"placeholder":"your desc",
			"id":"my id for area",
			"rows":20,
			"cols":120
			}))
	class Meta:
		model = Product
		fields = [
		'title',
		'description',
		'price',
		'summary'
		]

	# Used to add your own validation!
	# In this case, the form will raise an error if CFE is not in title
	def clean_title(self,*args,**kwargs):
		title=self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("NOT VALID TITLE")
		else:
			return title