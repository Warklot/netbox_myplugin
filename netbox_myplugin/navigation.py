from netbox.plugins import PluginMenu, PluginMenuItem

menu = PluginMenu(
    label='My Plugin',
    groups=(
        ('Devices', (
            PluginMenuItem(
                link='plugins:netbox_myplugin:custom_device_add',
                link_text='Add Custom Device',
                permissions=['dcim.add_device']
            ),
        )),
    )
)