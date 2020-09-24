from setuptools import find_packages, setup

setup(
    name='demoaction',
    version='1.0.2',
    description="A playground for everything",
    author="Di Chen",
    author_email="di.chen16@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
