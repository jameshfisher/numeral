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

from errors import (
	NotIntegerError, NumberIsZeroError, 
	NumberIsNegativeError, NumberIsComplexError,
	NumberTooLargeError
	)

from armenian import ArmenianNumeral
from urnfield import UrnfieldNumeral
from roman import RomanNumeral
from base64 import Base64Numeral
from base32 import Base32Numeral
from hexadecimal import HexadecimalNumeral
from octal import OctalNumeral
from chinese_financial_simplified import ChineseFinancialSimplifiedNumeral
from chinese_financial_traditional import ChineseFinancialTraditionalNumeral
from chinese_standard_simplified import ChineseStandardSimplifiedNumeral
from chinese_standard_traditional import ChineseStandardTraditionalNumeral
from cyrillic import CyrillicNumeral
from geez import GeezNumeral
from greek import GreekNumeral
from hebrew import HebrewNumeral

from formatter import Formatter

numbers = [
0,	# zero
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 99, 100,		# natural numbers
1000, 1234, 1234567890,	# big numbers
-1, -5, -10, -20, -21, -99, -100,	# negative integers
0.5, 0.7, 0.99, 9.99, 3.14,	# floats
-0.5, -1.1, -1000.1,	# negative floats
]

for numeral in Formatter.code_map.values():
	print u"\nTesting %s" % numeral
	for number in numbers:
		try:
			s = numeral.make(number)
			i = numeral.parse(s)
			assert i == number
		except AssertionError:
			print u"For number %s, the make() and parse() functions for %s are not inverse.  make() returned %s; parse() returned %s" % (number, numeral, s, i) 
			raise AssertionError
		except NotIntegerError:
			print u"-- For number %d, module '%s' does not accept floats." % (number, numeral)
		except NumberIsZeroError:
			print u"-- Module '%s' does not accept zero." % numeral
		except NumberIsNegativeError:
			print u"-- For number %s, module '%s' does not accept negative numbers." % (number, numeral)
		except NumberIsComplexError:
			print u"-- For number %s, module '%s' does not accept complex numbers." % (number, numeral)
		except NumberTooLargeError:
			print u"-- For number %s, module '%s' does not accept numbers this large." % (number, numeral)
		except NotImplementedError:
			print u"Module '%s' has FAILED to implement all required functionality." % numeral
		else:
			print u"Module %s PASSED on inversion test for number %s: numeral '%s', reparsed number %s" % (numeral, number, s, i)
	
	for (n, s) in numeral.TEST_CASES_MAKE:
		test = numeral.make(n)
		try:
			assert numeral.make(n) == s
		except AssertionError:
			print u"Module %s FAILED on its self-defined test: it says %s should make '%s', but it made '%s'." % (numeral, n, s, test)
			raise AssertionError
		else:
			print u"Module %s PASSED on its self-defined test %s -> %s" % (numeral, n, s)
	
	for n in numeral.FAIL_CASES_MAKE:
		try:
			s = numeral.make(n)
		except (NotIntegerError, NumberIsZeroError, NumberIsNegativeError, NumberIsComplexError, NumberTooLargeError):
			print u"Module %s PASSED on its assertion that attempting to make %s should fail" % (numeral, n)
		except:
			raise AssertionError(u"Module %s FAILED: making %s raised an UNKNOWN exception" % (numeral, n) )
		else:
			raise AssertionError(u"Module %s FAILED on its assertion that making %s should fail (it made %s)" % (numeral, n, s) )
	
