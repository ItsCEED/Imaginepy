from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='imaginepy',
    version='2.0.0',
    author='CEED',
    author_email='',
    description='Python library to create Art with AI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ItsCEED/imaginepy',
    license="GPL-3.0-only",
    packages=find_packages(),
    keywords=[
        "art",
        "image",
        "ai",
        "stable-diffusion"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities"
    ],
    python_requires='>=3.7',
    install_requires=[
        'aiohttp',
        'requests_toolbelt',
        'langdetect',
        'pybase64'
    ],
)