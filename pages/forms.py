from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name")
    email = forms.EmailField()
    phone = forms.CharField(
        max_length=14,
        label="Phone number",
    )
    message = forms.CharField(widget=forms.Textarea)
