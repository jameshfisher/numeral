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

from chinese_simplified import ChineseSimplifiedNumeral

class ChineseFinancialSimplifiedNumeral(ChineseSimplifiedNumeral):
	GLYPHS = {
		0: u"零",
		1: u"壹",
		2: u"贰",
		3: u"叁",
		4: u"肆",
		5: u"伍",
		6: u"陆",
		7: u"柒",
		8: u"捌",
		9: u"玖",
		10: u"拾",
		100: u"佰",
		1000: u"仟",
		10000: u"萬",
		100000000: u"億",
		math.pow(10,12): u"兆",
		math.pow(10,16): u"京",
		math.pow(10,20): u"垓",
		math.pow(10,24): u"秭",
		math.pow(10,28): u"穰",
		math.pow(10,32): u"沟",
		math.pow(10,36): u"涧",
		math.pow(10,40): u"正",
		math.pow(10,44): u"载"
		}

from formatter import Formatter
Formatter.register(ChineseFinancialSimplifiedNumeral, 'CFS')


