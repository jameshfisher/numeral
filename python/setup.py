#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2009 James Harrison Fisher <jameshfisher@gmail.com>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

try:
	from setuptools import setup, find_packages
except ImportError:
	import ez_setup
	ez_setup.use_setuptools()
	from setuptools import setup, find_packages

import os

setup(
	name="numeral",
	version="0.0",
	url = 'http://bitbucket.org/eegg/numeral/',
	description="Python library providing for the formatting (and unformatting) of world numeral systems",
	license='MIT',
	author="eegg (James Harrison Fisher)",
	author_email="jameshfisher@gmail.com",
	packages = find_packages(),
	include_package_data = True,
	classifiers = [
		"Development Status :: 1 - Planning",
		"Environment :: Plugins",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 2.6",
		]
	)
