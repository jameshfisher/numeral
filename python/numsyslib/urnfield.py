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

from utils import split
from numeral import Numeral
from errors import UnparseableNumeralError

from decorators import (
	deny_complex, deny_float, deny_negative, deny_zero, deny_large,
	deny_ordinal, inversion_test
	)

class UrnfieldNumeral(Numeral):
	"""
	http://en.wikipedia.org/wiki/Urnfield_culture_numerals
	
	This does not take into account the rather odd symbols suggested for
	higher numbers; it is only reliable up to about 20
	"""
	
	FAIL_CASES_MAKE = [
		21,
		]
	
	TEST_CASES_PARSE = [
		(u'////', 4),
		(u'////\u005C', 9),
		]
	
	FAIL_CASES_PARSE = [
		u'',		# Is there any documented 'zero'?
		u'\u005C/',	# Wrong order
		]
	
	under_5_glyph = u'/'
	
	"""
	The following is a backslash: python can't do things like r'\' or '\\'
	because it's STUPID
	<http://stackoverflow.com/questions/647769/why-cant-pythons-raw-string-literals-end-with-a-single-backslash>
	"""
	over_5_glyph = u'\u005C'
	
	@classmethod
	@deny_ordinal
	@deny_complex
	@deny_float
	@deny_negative
	@deny_zero
	@deny_large(20)
	def make(cls, number, ordinal=False):
		if not isinstance(number, int):
			raise NotIntegerError()
		over_5, under_5 = split(number, 5)
		return unicode(cls.under_5_glyph * under_5 + cls.over_5_glyph * over_5)
	
	@classmethod
	@inversion_test
	def parse(cls, numeral):
		n = 0
		for i in range(len(numeral)):
			if numeral[i] == cls.under_5_glyph:
				n += 1
			elif numeral[i] == cls.over_5_glyph:
				n += 5
			else:
				raise UnparseableNumeralError("The numeral contained unknown glyphs")
		return n

from formatter import Formatter
Formatter.register(UrnfieldNumeral, 'URN')
