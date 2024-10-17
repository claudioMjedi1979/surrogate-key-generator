from setuptools import setup, find_packages

setup(
    name="surrogate_lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="Biblioteca para gerar surrogate keys mascarando IDs",
    author="Claudio",
    zip_safe=False,  # Isso garante que a biblioteca funcione corretamente como um arquivo .zip
)

