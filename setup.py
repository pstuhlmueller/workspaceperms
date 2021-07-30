from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in workspaceperms/__init__.py
from workspaceperms import __version__ as version

setup(
	name='workspaceperms',
	version=version,
	description='Manage the availability of workspaces within Frappe/ ERPNext (sidebar) based on user-roles',
	author='Patrick Stuhlmüller',
	author_email='p.stuhlmueller@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
