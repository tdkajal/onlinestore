from django import forms
from django.forms import ModelForm
from owner.models import Books

# class BookForm(forms.Form):
    # book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # author_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # price=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # copies=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
class BookForm(ModelForm):
    class Meta:
        model=Books
        # exclude=('published_date',)
        # fields=['book_name','author','price','copies']
        fields='__all__'
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'copies':forms.NumberInput(attrs={'class':'form-control'}),
            'published_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

    def  clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        copies=cleaned_data.get("copies")

        if int (price)<0:
            msg="invalid value"
            self.add_error("price",msg)
        if int(copies)<0:
            msg="invalid value"
            self.add_error("copies",msg)