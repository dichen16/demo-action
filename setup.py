from setuptools import find_packages, setup

setup(
    name='demo-action',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
