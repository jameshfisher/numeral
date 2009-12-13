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

from utils import hierarchicize
from numeral import Numeral
from errors import UnparseableNumeralError
from decorators import deny_complex, deny_float, deny_negative, deny_large, inversion_test

class RomanNumeral(Numeral):
	"""
	ROMAN NUMERALS.
	"""
	
	TEST_CASES_MAKE = [
		(1, u'I'),
		(1000, u'M'),
		]
	
	FAIL_CASES_MAKE = []
	
	TEST_CASES_PARSE = [
		(u'XCIX', 99),
		(u'MMIX', 2009),
		]
	
	FAIL_CASES_PARSE = [
		u'ABC',
		u'XMX',
		u'IIII'
		]
	
	ROMAN_NUMERAL_CHAR_ORDER = [u'M',u'D',u'C',u'L',u'X',u'V',u'I']
	ROMAN_NUMERAL_CHARS = {
		u'M': 1000,
		u'D': 500,
		u'C': 100,
		u'L': 50,
		u'X': 10,
		u'V': 5,
		u'I': 1
		}
	
	@classmethod
	@deny_complex
	@deny_float
	@deny_negative
	@deny_large(1000000)
	def make(cls, number, ordinal=False):
		# Note that roman ordinal numbers are represented in the same way as cardinal.
		if number == 0:
			return u'nulla'
		
		thousands, hundreds, tens, ones = hierarchicize(number, [1000,100,10,1])
		
		string = ''
		
		for i in range(thousands):
			string += u'M'
			
		if hundreds > 0: 
			string += [u'C', u'CC', u'CCC', u'CD', u'D', u'DC', u'DCC', u'DCCC', u'CM'][hundreds-1]
		if tens > 0:
			string += [u'X', u'XX', u'XXX', u'XL', u'L', u'LX', u'LXX', u'LXXX', u'XC'][tens-1]
		if ones > 0:
			string += [u'I', u'II', u'III', u'IV', u'V', u'VI', u'VII', u'VIII', u'IX'][ones-1]
		
		return string
	
	@classmethod
	@inversion_test
	def parse(cls, numeral):
		numeral = numeral.upper()
		
		if numeral == u'NULLA':
			return 0
		
		n = 0
		for i in range(len(numeral)):
			if numeral[i] in cls.ROMAN_NUMERAL_CHAR_ORDER:
				if (not i == len(numeral) - 1) and cls.ROMAN_NUMERAL_CHAR_ORDER.index(numeral[i]) > cls.ROMAN_NUMERAL_CHAR_ORDER.index(numeral[i+1]):
					n -= cls.ROMAN_NUMERAL_CHARS[numeral[i]]
				else:
					n += cls.ROMAN_NUMERAL_CHARS[numeral[i]]
		
		return n

from formatter import Formatter
Formatter.register(RomanNumeral, 'ROM')
