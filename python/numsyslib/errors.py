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

"""
Of the following four classes of exceptions for making numerals, if the 
number passed to make() fails on more than one count then you should
return errors with the following precedence:
	NotIntegerError
	NumberIsZeroError
	NumberIsNegativeError
	NumberIsComplexError
"""

class NotIntegerError(Exception):
	"""
	This exception should be raised by numeral classes that cannot handle
	non-integers.  It should only be raised in the make() method.
	
	This should only be raised if it is a shortcoming of the numeral system,
	not your implementation of it - if it is the latter, use
	NotImplementedError.
	"""
	pass

class NumberIsZeroError(Exception):
	"""
	This exception should be raised by numeral classes that cannot handle
	the number zero.  It should only be raised in the make() method.
	
	This should only be raised if it is a shortcoming of the numeral system,
	not your implementation of it - if it is the latter, use
	NotImplementedError.
	"""
	pass

class NumberIsNegativeError(Exception):
	"""
	This exception should be raised by numeral classes that cannot handle
	negative numbers.  It should only be raised in the make() method.
	
	This should only be raised if it is a shortcoming of the numeral system,
	not your implementation of it - if it is the latter, use
	NotImplementedError.
	"""
	pass

class NumberIsComplexError(Exception):
	"""
	This exception should be raised by numeral classes that cannot handle
	complex numbers.  It should only be raised in the make() method.
	
	This should only be raised if it is a shortcoming of the numeral system,
	not your implementation of it - if it is the latter, use
	NotImplementedError.
	"""
	pass

class NumberTooLargeError(Exception):
	"""
	Many historical numeral systems only work sensibly below a certain
	size.  If the system should restrict working with numbers beyond a 
	certain size, this is the exception that should be raised if the user
	tries to make a numeral with this size or tries to parse a numeral
	to a number of this size.
	"""
	pass

class UnparseableNumeralError(Exception):
	"""
	This exception should be raised by numeral classes that cannot parse
	a given string.  It should only be raised in the parse() method.
	"""
	pass
