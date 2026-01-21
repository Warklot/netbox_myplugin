from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import CustomDeviceForm

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