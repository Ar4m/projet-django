from django import forms

statusDev = (
    ("1", "Développeur Front-end"),
    ("2", "Développeur Back-end"),
    ("3", "Développeur FullStack"),
)

class ResumeForm(forms.Form):
    Nom = forms.CharField()
    Email = forms.EmailField()
    Poste = forms.ChoiceField(choices = statusDev)
    Message = forms.CharField()

# crispyform