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

import math

from utils import hierarchicize
from numeral import Numeral
from errors import UnparseableNumeralError
from decorators import deny_complex, deny_float, deny_negative, deny_large, inversion_test

class AdditiveNumeral(Numeral):
	"""
		This function deals with base-10 systems of an additive nature that are (broadly speaking) not positional.
	"""
	
	BIG_NUMBER_PREFIX = ''

	END_OF_NUMBER_SUFFIX = ''
	
	TEST_CASES_MAKE = []
	
	FAIL_CASES_MAKE = []
	
	TEST_CASES_PARSE = []
	
	FAIL_CASES_PARSE = []
	
	
	@classmethod
	@deny_complex
	@deny_negative
	@deny_float
	def make(cls, number, ordinal=False):
		return cls._recurse(number, ordinal)
	
	@classmethod
	def _recurse(cls, number, ordinal, eon=True):
		"""
		eon = End Of Number; due to recursion we have to tell the function whether to add the end-of-number symbol
		"""
		
		h = hierarchicize(number, [1000,100,10,1])
		
		s = u''

		"""
		The number of thousands X is indicated simply by the number X.
		I'm a bit confused as to whether this simple recursion is really how
		really big numbers are represented though... it must be confusing!
		In the Greek numeral system, is the prefix ONLY added before the thousands?
		And what happens after a million?
		"""
		if h[0] > 0:
			s += cls._recurse(h[0], ordinal, False)
		if h[1] > 0:
			s += cls.NUMERALS[h[1] * 100]
		if h[2] > 0:
			s += cls.NUMERALS[h[2] * 10]
		if h[3] > 0:
			if not eon:
				s += cls.BIG_NUMBER_PREFIX
			s += cls.NUMERALS[h[3]]
		
		if eon:
			s += cls.END_OF_NUMBER_SUFFIX
		
		# I'm confused as to which order we should return the string in: Hebrew is an RTL language, and yet UTF seems to autoformat ... ???  I'm going to leave it as-is for now; you can reverse on your own
		return s
	
	@classmethod
	@inversion_test
	def parse(cls, numeral, ordinal=False):
		# The parsing of additive numerals is very simple: get the value for each character; add them up.
		reverse = dict(zip(cls.NUMERALS.values(), cls.NUMERALS.keys()))	# slow. this should be done in __init__, or somewhere.  make not classmethod?
		return sum([reverse.get(char, 0) for char in numeral])
