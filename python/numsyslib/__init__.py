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

__version__ = "0.0"

from formatter import Formatter

# Let's import all the classes which are not supposed to be abstract.
from armenian import ArmenianNumeral
from base32 import Base32Numeral
from base64 import Base64Numeral
from chinese_financial_simplified import ChineseFinancialSimplifiedNumeral
from chinese_financial_traditional import ChineseFinancialTraditionalNumeral
from chinese_standard_simplified import ChineseStandardSimplifiedNumeral
from chinese_standard_traditional import ChineseStandardTraditionalNumeral
from cyrillic import CyrillicNumeral
from geez import GeezNumeral
from greek import GreekNumeral
from hebrew import HebrewNumeral
from hexadecimal import HexadecimalNumeral
from octal import OctalNumeral
from roman import RomanNumeral
from thai import ThaiNumeral
from urnfield import UrnfieldNumeral
