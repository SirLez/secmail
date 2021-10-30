import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="secmail",
    version="1.0.2",
    url="https://github.com/SirLez/secmail",
    download_url="https://github.com/SirLez/secmail/archive/refs/heads/main.zip",
    description="A Libarry to generate emails!",
    long_description=README,
    long_description_content_type="text/markdown",
    author="SirLez",
    author_email="SirLezDV@gmail.com",
    license="MIT",
    keywords=[
        'SirLez',
        'sirlez',
        'api',
        'python',
        'python3',
        'python3.x',
        'official',
        'secmail',
        '1secmail',
        'mail',
        'email-generator-python',
        'email-generator',
        'email-python'
    ],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    setup_requires=[
        'wheel'
    ],
    packages=find_packages(),
)
