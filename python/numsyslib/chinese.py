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

class ChineseNumeral(Numeral):
	""" --- CHINESE NUMERALS ---
		http://en.wikipedia.org/wiki/Chinese_numerals
	"""
	
	FAIL_CASES_MAKE = []
	
	TEST_CASES_PARSE = []
	
	FAIL_CASES_PARSE = []
	
	HIERARCHY = [
		math.pow(10,44),
		math.pow(10,40),
		math.pow(10,36),
		math.pow(10,32),
		math.pow(10,28),
		math.pow(10,24),
		math.pow(10,20),
		math.pow(10,16),
		math.pow(10,12),
		math.pow(10,8),
		10000,
		1000,
		100,
		10,
		1
		]
	
	ORDINAL_GLYPH = u'第'
	
	@classmethod
	@deny_complex
	@deny_float
	def make(cls, number, ordinal=False):
		s = ''
		
		if ordinal:
			s += cls.ORDINAL_GLYPH
		
		if number < 0:
			s += cls.NEGATIVE_GLYPH
			number = -number
			
		if number < 10:
			return s + cls.GLYPHS[number]
		
		h = hierarchicize(number, cls.HIERARCHY)
		
		
		
		for i in range(len(h)):
			if h[i] == 0:	# If there are more than one pegs on this row of the abacus ... (otherwise, do nothing)
				continue
			else:
				if cls.HIERARCHY[i] != 1 and h[i] != 1:	# Leave out the 'one' in e.g. 'one ten' if it is obvious
					s += cls.GLYPHS[h[i]]
				if cls.HIERARCHY[i] != 1:
					s += cls.GLYPHS[cls.HIERARCHY[i]]
		return s
