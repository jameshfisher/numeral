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

class GreekNumeral(AdditiveNumeral):
	"""
	http://en.wikipedia.org/wiki/Greek_numerals
	"""

	NUMERALS = {	
		1: u"α",
		2: u"β",
		3: u"γ",
		4: u"δ",
		5: u"ε",
		6: u"ϝ",
		7: u"ζ",
		8: u"η",
		9: u"θ",
		10: u"ι",
		20: u"κ",
		30: u"λ",
		40: u"μ",
		50: u"ν",
		60: u"ξ",
		70: u"ο",
		80: u"π",
		90: u"ϟ",
		100: u"ρ",
		200: u"σ",
		300: u"τ",
		400: u"υ",
		500: u"φ",
		600: u"χ",
		700: u"ψ",
		800: u"ω",
		900: u"ϡ"
		}
	
	BIG_NUMBER_PREFIX = u"͵"

	END_OF_NUMBER_SUFFIX = u"ʹ"

from formatter import Formatter
Formatter.register(GreekNumeral, u'GRC')
