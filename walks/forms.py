from django import forms

class CreateWalkForm(forms.Form):
    title = forms.CharField()
    walk_description = forms.CharField(widget=forms.Textarea,required=False)
    walk_is_public = forms.BooleanField()

    def someFunc(self):
        # send email using the self.cleaned_data dictionary
        pass