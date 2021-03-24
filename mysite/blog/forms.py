from django import forms

# Standard convention is to add forms inside a forms.py for each application


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)  # max_length is a validation field
    email = forms.EmailField()  # manages email validation for you
    to = forms.EmailField()
    # The widget attribute overrides the default widget - here Textarea is used instead of <input> element
    comments = forms.CharField(required=False, widget=forms.Textarea)
