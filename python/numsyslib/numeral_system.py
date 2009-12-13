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

import helpers
import string
import math

# BASIC ENUMERATION
BASE_36,			\
BASE_30,			\
HEXADECIMAL,			\
OCTAL,				\
ENGLISH_TEXT,			\
FRENCH_TEXT,			\
SPANISH_TEXT,			\
ROMAN_NUMERAL,			\
HEBREW_NUMERAL,			\
GREEK_NUMERAL,			\
CYRILLIC_NUMERAL,		\
URNFIELD_NUMERAL,		\
ETHIOPIC_NUMERAL,		\
GEEZ_NUMERAL,			\
THAI_NUMERAL,			\
ARMENIAN_NUMERAL,		\
CHINESE_STANDARD_SIMPLIFIED,	\
CHINESE_STANDARD_TRADITIONAL,	\
CHINESE_FINANCIAL_SIMPLIFIED,	\
CHINESE_FINANCIAL_TRADITIONAL = range(20)

__encode__ = {
	BASE_36:			lambda x: int_to_scientific_base(x,36),
	BASE_30:			lambda x: int_to_scientific_base(x,30),
	HEXADECIMAL:			lambda x: int_to_scientific_base(x,16),
	OCTAL:				lambda x: int_to_scientific_base(x,8),
	ENGLISH_TEXT:			lambda x: int_to_text(x,'en'),
	FRENCH_TEXT:			lambda x: int_to_text(x, 'fr'),
	SPANISH_TEXT:			lambda x: int_to_text(x, 'sp'),
	ROMAN_NUMERAL:			lambda x: int_to_roman_numeral(x),
	HEBREW_NUMERAL:			lambda x: int_to_additive_numeral(x,'he'),
	GREEK_NUMERAL:			lambda x: int_to_additive_numeral(x,'el'),
	CYRILLIC_NUMERAL:		lambda x: int_to_additive_numeral(x, 'ru'),	# No ISO-639 code for cyrillic, being just an alphabet...
	ETHIOPIC_NUMERAL:		lambda x: int_to_additive_numeral(x, 'ethi'),
	GEEZ_NUMERAL:			lambda x: int_to_additive_numeral(x, 'ethi'),
	URNFIELD_NUMERAL:		lambda x: int_to_urnfield_numeral(x),
	ARMENIAN_NUMERAL:		lambda x: int_to_additive_numeral(x,'hy'),
	CHINESE_STANDARD_SIMPLIFIED:	lambda x: int_to_chinese_numeral(x, 'standard_simplified'),
	CHINESE_STANDARD_TRADITIONAL:	lambda x: int_to_chinese_numeral(x, 'standard_traditional'),
	CHINESE_FINANCIAL_SIMPLIFIED:	lambda x: int_to_chinese_numeral(x, 'financial_simplified'),
	CHINESE_FINANCIAL_TRADITIONAL:	lambda x: int_to_chinese_numeral(x, 'financial_traditional'),
	THAI_NUMERAL:		lambda x: int_to_arabic_numeral(x,'th')
	}
def encode(x,e):
	if e in __encode__.keys():
		return __encode__[e](x)
	else:
		return 'Not in enum!'

__decode__ = {
	ROMAN_NUMERAL:		lambda x: roman_numeral_to_int(x),
	BASE_36:		0,
	URNFIELD_NUMERAL:	lambda x: urnfield_numeral_to_int(x)
	}

def decode(x,e):
	if e in __decode__.keys():
		return __decode__[e](x)
	else:
		return 'Not in enum!'

class Nonsense():
	"""This is returned by a function attempting to decode a string if all attempts fail and its meaning cannot be deduced."""
	pass
