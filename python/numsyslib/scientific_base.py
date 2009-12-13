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

from utils import hierarchicize, int_to_base_array
from numeral import Numeral
from errors import UnparseableNumeralError
from decorators import deny_complex, deny_float, deny_negative

class ScientificBaseNumeral(Numeral):
	"""
	Abstract base class for base-X numerals.
	The only common implementations here are 8, 16, 32, 64.
	"""
	
	BASE_CHARS=[
		'0',
		'1',
		'2',
		'3',
		'4',
		'5',
		'6',
		'7',
		'8',
		'9',
		'A',	# 10
		'B',	# 11
		'C',	# 12
		'D',	# 13
		'E',	# 14
		'F',	# 15
		'G',	# 16
		'H',	# 17
		'I',	# 18
		'J',	# 19
		'K',	# 20
		'L',	# 21
		'M',	# 22
		'N',	# 23
		'O',	# 24
		'P',	# 25
		'Q',	# 26
		'R',	# 27
		'S',	# 28
		'T',	# 29
		'U',	# 30
		'V',	# 31
		'W',	# 32
		'X',	# 33
		'Y',	# 34
		'Z'		# 35
		]
	
	@classmethod
	@deny_float
	@deny_complex
	@deny_negative
	def make(cls, number, ordinal=False):
		arr = int_to_base_array(number, cls.base)
		s = ''
		for i in range(len(arr)):
			s += cls.BASE_CHARS[arr[i]]
		return s
	
	@classmethod
	def parse(cls, numeral, ordinal=False):
		little_endian = list(numeral)
		little_endian.reverse()
		n = 0
		for i in range(len(little_endian)):
			n += cls.BASE_CHARS.index(little_endian[i]) * math.pow(cls.base,i)
		return n
