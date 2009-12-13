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

class Numeral:
	TEST_CASES_MAKE = {}
	FAIL_CASES_MAKE = []
	
	@classmethod
	def make(self, number, ordinal=False):
		"""
		Convert a number to its numeral representation and return it.
		
		@type	number:		number
		@param	number:		The number to convert (whether float or integer)
		
		@rtype:				unicode
		@return:			The numeral representation of this number
		"""		
		raise NotImplementedError()
	
	TEST_CASES_PARSE = {}
	FAIL_CASES_PARSE = []
	
	@classmethod
	def parse(self, numeral, ordinal=False):
		"""
		Try to parse a numeral representation of a number into a python float.
		
		@type	numeral:	unicode
		@param	numeral:	The numeral that requires parsing
		
		@rtype:				float
		@return:			The float representation of the numeral
		"""
		raise NotImplementedError()
