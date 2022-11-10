from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'    

        self.fields['postcode'].widget.attrs['id'] = 'address_postcode'
        self.fields['doromeong_address'].widget.attrs['id'] = 'doromeong_address'
        self.fields['detail_address'].widget.attrs['id'] = 'detail_address'
        self.fields['extra_address'].widget.attrs['id'] = 'extra_address'
        self.fields['order_note'].widget.attrs['id'] = 'order_note'
        self.fields['to_save'].widget.attrs['class'] = 'custom-control-input'
        self.fields['to_save'].widget.attrs['id'] = 'customSwitches'
        self.fields['to_save'].widget.attrs['type'] = 'checkbox'
        self.fields['order_note'].widget.attrs['id'] = 'order_note'
        self.fields['order_note'].widget.attrs['list'] = 'datalistOptions'
        self.fields['order_note'].widget.attrs['placeholder'] = '배송시 요청사항을 입력합니다.'

    class Meta:
        model = Order
        # *question: how to decide to call which fields to include and not?
        fields = ['recipient','phone_1','phone_2','email','order_note', 'postcode','doromeong_address', 'detail_address','extra_address','to_save']

