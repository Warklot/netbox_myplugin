from django import forms
from dcim.models import Device

class CustomDeviceForm(forms.ModelForm):
    purchase_order = forms.CharField(max_length=100, required=False, label="Purchase Order")
    warranty_end = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Device
        fields = ['name', 'role', 'device_type', 'site', 'rack','config_template']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            if self.instance.custom_field_data:
                self.fields['purchase_order'].initial = self.instance.custom_field_data.get('myplugin_purchase_order', '')
                self.fields['warranty_end'].initial = self.instance.custom_field_data.get('myplugin_warranty_end', '')
    
    def save(self, commit=True):
        print("DEBUG: save() started")
        device = super().save(commit=commit)
        print(f"DEBUG: super().save() completed, device pk={device.pk}")
        
        if commit:
            print("DEBUG: commit=True, updating custom_field_data")
            
            if not device.custom_field_data:
                device.custom_field_data = {}
            
            device.custom_field_data['myplugin_purchase_order'] = self.cleaned_data.get('purchase_order', '')
            print(f"DEBUG: Set purchase_order")
            
            warranty_date = self.cleaned_data.get('warranty_end')
            if warranty_date:
                device.custom_field_data['myplugin_warranty_end'] = str(warranty_date)
                print(f"DEBUG: Set warranty_end to {warranty_date}")
            
            print("DEBUG: About to call device.save()...")
            device.save()  # ← ERROR LIKELY HERE!
            print("DEBUG: device.save() completed")
        
        return device