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

from additive import AdditiveNumeral

class HebrewNumeral(AdditiveNumeral):
	"""
		The Hebrew calendar is currently one of the few uses of Hebrew numerals.
		http://en.wikipedia.org/wiki/Hebrew_numerals
	"""
	
	NUMERALS = {
		1: u"א",
		2: u"ב",
		3: u"ג",
		4: u"ד",
		5: u"ה",
		6: u"ו",
		7: u"ז",
		8: u"ח",
		9: u"ט",
		10: u"י",
		20: u"כ",
		30: u"ל",
		40: u"מ",
		50: u"נ",
		60: u"ס",
		70: u"ע",
		80: u"פ",
		90: u"צ",
		100: u"ק",
		200: u"ר",
		300: u"ש",
		400: u"ת",
		500: u"ת\"ק",
		600: u"ת\"ר",
		700: u"ת\"ש",
		800: u"ת\"ת",
		900: u"תת\"ק"
		}
	
	TEST_CASES_MAKE = []
	
	FAIL_CASES_MAKE = []
	
	TEST_CASES_PARSE = []
	
	FAIL_CASES_PARSE = []

from formatter import Formatter
Formatter.register(HebrewNumeral, u'HEB')
