from django import forms
from dcim.models import Device

class CustomDeviceForm(forms.ModelForm):
    purchase_order = forms.CharField(max_length=100, required=False, label="Purchase Order")
    warranty_end = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Device
        fields = ['name', 'role', 'device_type', 'site', 'rack','config_template']
    
    def save(self, commit=True):
        device = super().save(commit=commit)
        
        if commit:
            if not device.custom_field_data:
                device.custom_field_data = {}
            
            device.custom_field_data['myplugin_purchase_order'] = self.cleaned_data.get('purchase_order', '')
            
            warranty_date = self.cleaned_data.get('warranty_end')
            if warranty_date:
                device.custom_field_data['myplugin_warranty_end'] = str(warranty_date)
            
            device.save()
        
        return device