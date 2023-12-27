
from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject','review','rating']



#from accounts.models import Account, UserProfile

#from .models import Review
 
 
#class OrderForm(forms.ModelForm):
   #  class Meta:
    #     model = Order
     #   fields = ['first_name','last_name','phone','email','address_line_1','address_line_2','country','state','city','order_note']-->
            