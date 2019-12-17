from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ngenicpy',
   version='0.1.2b2',
   description='Python package for simple access to Ngenic Tune API',
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Simon Falkman',
   author_email='sfalkman@gmail.com',
   url="https://github.com/sfalkman/ngenic-py",
   packages=find_packages(exclude=["tests"]),
   install_requires=['requests'],
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
