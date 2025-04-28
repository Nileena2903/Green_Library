from django import forms
from .models import signup_table

# class Regform(forms.Form):
#     Fullname = forms.CharField(max_length=50)
#     Email =forms.EmailField()
#     mobile = forms.IntegerField()
#     password = forms.CharField(max_length=20)
    

    
'''we use modelform class instead of form class when the model or table is  already exist(we take fields from signup_table model)'''


# class Regform(forms.ModelForm):
    
#     class Meta:
#         model =signup_table
#         fields = ("__all__")

''' if we only need 2 fields which is  name and mobile'''

class Regform(forms.ModelForm):
    
    class Meta:
        model =signup_table
        fields = ['name','mobile',]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name','color':'yellow'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number','color':'yellow'})
        }
