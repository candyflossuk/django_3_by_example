from django import forms
from .models import Comment

# Standard convention is to add forms inside a forms.py for each application


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)  # max_length is a validation field
    email = forms.EmailField()  # manages email validation for you
    to = forms.EmailField()
    # The widget attribute overrides the default widget - here Textarea is used instead of <input> element
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # indicates which model to use to build the form - Django builds the form dynamically
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField()
