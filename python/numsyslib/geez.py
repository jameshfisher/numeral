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

class GeezNumeral(AdditiveNumeral):
	
	NUMERALS = {	# These are Ge'ez numerals C&P'd from http://en.wikipedia.org/wiki/Ge%27ez_alphabet#Numerals
		1: u"፩",
		2: u"፪",
		3: u"፫",
		4: u"፬",
		5: u"፭",
		6: u"፮",
		7: u"፯",
		8: u"፰",
		9: u"፱",
		10: u"፲",
		20: u"፳",
		30: u"፴",
		40: u"፵",
		50: u"፶",
		60: u"፷",
		70: u"፸",
		80: u"፹",
		90: u"፺",
		100: u"፻",
		200: u"፻፻",
		300: u"፻፻፻",
		400: u"፻፻፻፻",
		500: u"፻፻፻፻፻",
		600: u"፻፻፻፻፻፻",
		700: u"፻፻፻፻፻፻፻",
		800: u"፻፻፻፻፻፻፻፻",
		900: u"፻፻፻፻፻፻፻፻፻"
		}

from formatter import Formatter
Formatter.register(GeezNumeral, u'ETH')
