
"""

 This project is protected by the following license
 --

  MIT License
  Copyright (c) 2021 http-samc
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""

from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cleanify",
    version="1.0.0",
    description="CLI utility to remove remove newlines, tabs from a file and copy it to your clipboard",
    url="https://github.com/http-samc/cleanify",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = ["cleanify"],
    entry_points = {
        'console_scripts': [
            'cleanify=cleanify.main:main'
        ]
    },
    install_requires = [
        "klembord==0.2.2"
    ],
    classifiers = [
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English"
    ]
)