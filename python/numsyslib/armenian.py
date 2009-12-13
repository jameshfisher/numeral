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

class ArmenianNumeral(AdditiveNumeral):
	NUMERALS = {		# Armenian
		1: u"Ա",
		2: u"Բ",
		3: u"Գ",
		4: u"Դ",
		5: u"Ե",
		6: u"Զ",
		7: u"Է",
		8: u"Ը",
		9: u"Թ",
		10: u"Ժ",
		20: u"Ի",
		30: u"Լ",
		40: u"Խ",
		50: u"Ծ",
		60: u"Կ",
		70: u"Հ",
		80: u"Ձ",
		90: u"Ղ",
		100: u"Ճ",
		200: u"Մ",
		300: u"Յ",
		400: u"Ն",
		500: u"Շ",
		600: u"Ո",
		700: u"Չ",
		800: u"Պ",
		900: u"Ջ",
		1000: u"Ռ",
		2000: u"Ս",
		3000: u"Վ",
		4000: u"Տ",
		5000: u"Ր",
		6000: u"Ց",
		7000: u"Ւ",
		8000: u"Փ",
		9000: u"Ք"
		}

from formatter import Formatter
Formatter.register(ArmenianNumeral, u'ARM')
