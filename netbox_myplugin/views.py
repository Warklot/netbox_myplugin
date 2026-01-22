from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import CustomDeviceForm
from dcim.models import Device

class CustomDeviceCreateView(View):
    def get(self, request):
        form = CustomDeviceForm()
        return render(request, 'netbox_myplugin/device_form.html', {'form': form})
    
    def post(self, request):
        form = CustomDeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            messages.success(request, f"Device {device.name} created")
            return redirect('dcim:device', pk=device.pk)
        return render(request, 'netbox_myplugin/device_form.html', {'form': form})

class CustomDeviceEditView(View):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        old_data = device.custom_field_data.copy() if device.custom_field_data else {}
        device.custom_field_data = {}
        
        form = CustomDeviceForm(instance=device)
        device.custom_field_data = old_data
        if old_data:
            form.fields['purchase_order'].initial = old_data.get('myplugin_purchase_order', '')
            form.fields['warranty_end'].initial = old_data.get('myplugin_warranty_end', '')
        
        return render(request, 'netbox_myplugin/device_form.html', {'form': form})
    
    def post(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        old_data = device.custom_field_data.copy() if device.custom_field_data else {}
        device.custom_field_data = {}
        
        form = CustomDeviceForm(request.POST, instance=device)
        
        if form.is_valid():
            device = form.save(commit=False)
            device.custom_field_data = old_data
            device.custom_field_data['myplugin_purchase_order'] = form.cleaned_data.get('purchase_order', '')
            
            warranty_date = form.cleaned_data.get('warranty_end')
            if warranty_date:
                device.custom_field_data['myplugin_warranty_end'] = str(warranty_date)
            
            device.save()
            messages.success(request, f"Device {device.name} updated")
            return redirect('dcim:device', pk=device.pk)
        
        return render(request, 'netbox_myplugin/device_form.html', {'form': form})