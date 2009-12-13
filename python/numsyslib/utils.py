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

def int_to_base_array(x, base):
	"""
	Pass the number you wish to format, plus a base number (e.g. for Arabic numerals, 10).
	You will receive an big-endian array of numbers representing each glyph of your formatted number.
	
	Examples:
		int_to_base_array(255,10) returns [2,5,5]
		int_to_base_array(255,2) returns [1,1,1,1,1,1,1,1]
	
	Don't try base-1!
	
	@type	x:		integer
	@param	x:		the integer you wish to convert to a base array
	
	@type	base:	integer
	@param	base:	the base-number of the array you wish to convert to
	
	@rtype:			list
	@return:		A list of integers representing each glyph of your base-X numeral, in big-endian format.
	"""
	arr = []
	modulo = base
	while modulo <= x:
		arr.append(int(math.floor((x % modulo)/(modulo/base))))
		modulo = modulo * base
	arr.append(int(math.floor((x % modulo)/(modulo/base))))	# And then once more
	
	arr.reverse()
	return arr


def split(x, y):
	"""
	This is a simple operator on two numbers `x` and `y`, returning a tuple (how many y's go into x, the remainder).
	
	@type	x:		number
	@param	x:		The number you are dividing up
	
	@type	y:		number
	@param	y:		The number to divide `x` into
	
	@rtype:			tuple
	@return:		A 2-tuple of (how many y's go into x, the remainder)
	"""
	a = x % y
	return ( (x - a)/y , a )

def hierarchicize(x, array):
	"""
	Many calculations require things like: so many A's make up a B, so many B's make up a C ... how many Cs, Bs, and As go into X?
	
	@type	x:		number
	@param	x:		the number to hierarchicize
	
	@type	array:	list
	@param	array:	A list representing the hierarchy you want to split into
	
	@rtype:			list
	@return:		The calculated hierarchy
	"""
	newarray = []
	
	for num in array:
		h, x = split(x, num)
		newarray.append(h)
	
	return newarray

