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

from chinese_traditional import ChineseTraditionalNumeral

class ChineseStandardTraditionalNumeral(ChineseTraditionalNumeral):
	NEGATIVE_GLYPH = u'負'
	GLYPHS = {
		0: u"〇",
		1: u"一",
		2: u"二",
		3: u"三",
		4: u"四",
		5: u"五",
		6: u"六",
		7: u"七",
		8: u"八",
		9: u"九",
		10: u"十",
		math.pow(10,2): u"百",
		math.pow(10,3): u"千",
		math.pow(10,4): u"萬",
		math.pow(10,8): u"億",
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
Formatter.register(ChineseStandardTraditionalNumeral, u'CST')
