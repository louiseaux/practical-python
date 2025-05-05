# setup.py
#
# Exercise 9.5

import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="Ashlyn Barry",
    author_email="ashlyn.barry1@gmail.com",
    description="Practical Python Code",
    packages=setuptools.find_packages(),
    scripts=['print-report.py'],
)