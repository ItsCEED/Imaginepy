from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='imaginepy',
    version='1.0.5',
    author='CEED',
    author_email='',
    description='Python library to create Art with AI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ItsCEED/ImaginePY-Midjourney-Free-Alternative',
    packages=find_packages(),
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'requests_toolbelt',
        'langdetect',
    ],
)
