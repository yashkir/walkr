from django import forms

class CreateWalkForm(forms.Form):
    title = forms.CharField()
    walk_description = forms.CharField(widget=forms.Textarea)
    walk_is_public = forms.BooleanField()

    stop_title = forms.CharField()
    stop_description = forms.CharField(widget=forms.Textarea)
    stop_location_text = forms.CharField(max_length=256)

    def someFunc(self):
        # send email using the self.cleaned_data dictionary
        pass