# secmail

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="secmail",
    version="1.0.0",
    url="https://github.com/SirLez/SAmino",
    download_url="https://github.com/SirLez/SAmino/archive/refs/heads/main.zip",
    description="A Libarry to generate emails!",
    long_description=README,
    long_description_content_type="text/markdown",
    author="SirLez",
    author_email="SirLezDV@gmail.com",
    license="MIT",
    keywords=[
        'capture',
        'captureS'
        'capture-bot',
        'capture-chat',
        'capture-lib',
        'cptr',
        'cptr.co',
        'api',
        'python',
        'python3',
        'python3.x',
        'SirLez',
        'sirlez',
        'Amino',
        'Amino.py',
        'Amino py',
        'amino',
        'amino py'
        'S-Amino',
        'amino',
        'amino',
        'amino-bot',
        'amino-bots',
        'amino-bot',
        'ndc',
        'narvii.apps',
        'aminoapps',
        'amino-py',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'slimakoi',
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
