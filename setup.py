from setuptools import find_packages, setup

setup(
    name='netbox-myplugin',
    version='0.1.0',
    description='Custom device forms for NetBox',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)