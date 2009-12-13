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

class CyrillicNumeral(AdditiveNumeral):
	
	NUMERALS = {	
		1: u"а",		# I've taken these from the image at http://en.wikipedia.org/wiki/Cyrillic_numerals and http://en.wikipedia.org/wiki/Early_Cyrillic_alphabet
		2: u"в",
		3: u"г",
		4: u"д",
		5: u"є",
		6: u"ѕ",
		7: u"з",
		8: u"и",
		9: u"ѳ",
		10: u"ї",
		20: u"к",
		30: u"л",
		40: u"м",
		50: u"н",
		60: u"ѯ",	# This is the awesomest letter ever
		70: u"о",
		80: u"п",
		90: u"ц",
		100: u"р",
		200: u"с",
		300: u"т",
		400: u"у",
		500: u"ф",
		600: u"х",
		700: u"ѱ",
		800: u"ѡ",
		900: u"ѵ"	# Going for a break now; my fingers are copy-and-pasted out
		}
	
	BIG_NUMBER_PREFIX = u"҂"


from formatter import Formatter
Formatter.register(CyrillicNumeral, 'CYR')
