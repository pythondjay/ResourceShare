from django import forms


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "title-input", "placeholder": "Enter a title"}
        )
    )  # type text
    link = forms.URLField()
    description = forms.CharField(widget=forms.Textarea)
    choices = [("1", "Programming Languages"), ("2", "Databases")]
    category = forms.ChoiceField(
        widget=forms.RadioSelect, choices=choices, label="Category"
    )
    tag_choices = [("1", "Python"), ("2", "Django")]
    tag = forms.MultipleChoiceField(choices=tag_choices, label="Tags")
