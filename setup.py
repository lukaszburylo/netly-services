"""setup.py file"""

from setuptools import setup, find_packages

setup(
    name="netly_services",  # nazwa paczki, taka jak w pip install
    version="0.0.3",  # wersja paczki
    packages=find_packages(),  # automatyczne znalezienie folderów z __init__.py
    install_requires=[  # opcjonalne zależności
        "netly_shared @ git+https://github.com/lukaszburylo/netly-shared.git#egg=netly_shared",
        "docker",
        "psutil",
    ],
    python_requires=">=3.10",  # wersja Pythona
)
