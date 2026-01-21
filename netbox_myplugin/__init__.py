from netbox.plugins import PluginConfig

class MyPluginConfig(PluginConfig):
    name = 'netbox_myplugin'
    verbose_name = 'My Custom Plugin'
    description = 'Custom device forms'
    version = '0.1.0'
    base_url = 'myplugin'
    
    def ready(self):
        from . import navigation
        super().ready()

config = MyPluginConfig