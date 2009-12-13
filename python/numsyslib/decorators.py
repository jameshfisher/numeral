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

from errors import (
	NotIntegerError, NumberIsNegativeError, 
	NumberIsZeroError, NumberIsComplexError,
	NumberTooLargeError, UnparseableNumeralError
	)

def deny_float(f):
	# Decorator to deny floating-point numbers from make().
	def wrap(cls, number, ordinal=False):
		if not int(number) == number:
			raise NotIntegerError("The number %s is not an integer." % number)
		return f(cls, number, ordinal)
	return wrap

def deny_negative(f):
	# Decorator to deny negative numbers from make().
	def wrap(cls, number, ordinal=False):
		if number < 0:
			raise NumberIsNegativeError()
		return f(cls, number, ordinal)
	return wrap

def deny_zero(f):
	# Decorator to deny zero from make().
	def wrap(cls, number, ordinal=False):
		if number == 0:
			raise NumberIsZeroError()
		return f(cls, number, ordinal)
	return wrap

def deny_complex(f):
	# Decorator to deny complex numbers from make().
	def wrap(cls, number, ordinal=False):
		if isinstance(number, complex):
			raise NumberIsComplexError()
		return f(cls, number, ordinal)
	return wrap

def deny_ordinal(f):
	# Decorator to deny making ordinal numerals.
	def wrap(cls, number, ordinal=False):
		if ordinal:
			raise NumberIsOrdinalError()
		return f(cls, number, ordinal)
	return wrap

def deny_large(cutoff):
	# Decorator to deny arbitrarily large numbers from make().
	def wrap(f):
		def wrapped_f(*args):
			if args[1] > cutoff:
				raise NumberTooLargeError()
			return f(*args)
		return wrapped_f
	return wrap

def deny(f, float=False, zero=False, negative=False, complex=False):
	if float:
		f = deny_float(f)
	if zero:
		f = deny_zero(f)
	if negative:
		f = deny_negative(f)
	if complex:
		f = deny_complex(f)
	return f

def inversion_test(f):
	"""
	A check to perform on parse(): when re-making the numeral, it should
	be the same as the passed numeral.  This acts as a convenient sanity
	check.
	"""
	def wrap(cls, numeral, ordinal=False):
		n = f(cls, numeral)
		new = cls.make(n)
		if new != numeral:
			print "The numeral failed the inversion test: %s -> %s, but %s -> %s" % (numeral, n, n, new)
			raise UnparseableNumeralError()
		return n
	return wrap
