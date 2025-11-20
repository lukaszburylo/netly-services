from setuptools import setup, find_packages

setup(
    name="netly_services",           # nazwa paczki, taka jak w pip install
    version="0.0.1",                 # wersja paczki
    packages=find_packages(),        # automatyczne znalezienie folderów z __init__.py
    install_requires=[               # opcjonalne zależności
        # "requests>=2.28.0",
    ],
    python_requires='>=3.10',         # wersja Pythona
)