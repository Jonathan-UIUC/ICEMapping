from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

GENDER = (
    ('', 'Choose...'),
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('NA', 'Prefer not to answer')
)


RACE = (
    ('', 'Choose...'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Asian', 'Asian'),
    ('Other', 'Other Race'),
    ('NA', 'Prefer not to answer')
)

Age = (
    ('', 'Choose...'),
    ('Young', 'Young'),
    ('Middle', 'Middle'),
    ('Old', 'Old'),
    ('NA', 'Prefer not to answer')
)

Dept = (
    ('', 'Choose...'),
    ('North','North'),
    ('South','South'),
    ('Main','Main' )
)

RATE = (
    ('', 'Choose...'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

Area = (
    ('', 'Choose...'),
    ('south', 'South Quad'),
    ('main', 'Main Quad'),
    ('engin', 'North Quad'),
)

#   Forms for user to filled out. I use the 'crispy_forms' API to beautify the form.
#   You can google this API to see how it works and use their documentation as reference.
class UserInfoForm(forms.Form):
    geoid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GeoID'}))
    block = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Block Number'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Your age'}))
    race = forms.ChoiceField(choices=RACE)
    gender = forms.ChoiceField(choices=GENDER)
    dept = forms.ChoiceField(choices=Dept)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('geoid', css_class='form-group col-md-4 mb-0'),
                Column('block', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dept', css_class='form-group col-md-4 mb-0'),
                Column('race', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

class CommentForm(forms.Form):
    rate = forms.ChoiceField(choices=RATE)
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Leave your comment: '}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'rate',
            'comment',
            Submit('submit', 'Submit')
        )

class recommandationForm(forms.Form):
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Your age'}))
    race = forms.ChoiceField(choices=RACE)
    gender = forms.ChoiceField(choices=GENDER)
    age = forms.ChoiceField(choices=Age)
    area = forms.ChoiceField(choices=Area)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('age', css_class='form-group col-md-3 mb-0'),
                Column('race', css_class='form-group col-md-3 mb-0'),
                Column('gender', css_class='form-group col-md-3 mb-0'),
                Column('area', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )
