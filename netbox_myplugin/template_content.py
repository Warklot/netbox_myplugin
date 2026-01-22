from netbox.plugins import PluginTemplateExtension

class DeviceListButtons(PluginTemplateExtension):
    def list_buttons(self):
        request = self.context.get('request')
        if not request:
            return ''
        if request.resolver_match.view_name != 'dcim:device_list':
            return ''

        return self.render('netbox_myplugin/device_list_button.html')


class DeviceDetailButtons(PluginTemplateExtension):
    model = 'dcim.device'
    
    def buttons(self):
        # Show Edit button on device detail page
        device = self.context['object']
        return self.render('netbox_myplugin/device_detail_button.html', extra_context={
            'device': device
        })

class DeviceMyPluginInfo(PluginTemplateExtension):
    model = 'dcim.device'
    
    def right_page(self):
        device = self.context['object']
        return self.render('netbox_myplugin/device_info_panel.html', extra_context={
            'device': device
        })

template_extensions = [DeviceListButtons, DeviceDetailButtons, DeviceMyPluginInfo]