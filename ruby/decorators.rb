#! /usr/bin/env ruby
# -*- coding: utf-8 -*-

=begin
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
=end

require 'errors'

module NumeralDecorators
	def deny_float(func_name)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			raise NotIntegerError, "#{number} is not an integer" unless number.respond_to? "floor" and number.floor == number
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny_negative(func_name)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			raise NumberIsNegativeError, "#{number} is negative" if number < 0
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny_zero(func_name)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			raise NumberIsZeroError if number == 0
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny_complex(func_name)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			#raise NumberIsComplexError if ...
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny_ordinal(func_name)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			raise NumberIsOrdinalError if ordinal
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny_large(func_name, maximum)
		old_method = instance_method(func_name)
		define_method(func_name) { |number, ordinal=false|
			raise NumberIsTooLargeError if number > maximum
			old_method.bind(self).call(number, ordinal)
			}
		end
	
	def deny func_name, *args
		[:float, :negative, :zero, :complex, :ordinal].each { |arg|
			method(("deny_" + arg.to_s).to_sym).call(func_name) if args.include? arg
			}
		end
	
	def deny_glyphs func_name, glyphs
		# Pre-parsing sanity check: does the string lie outside the set of 
		# glyphs that this numeral system knows about?  Define them in a
		# class array called KNOWN_GLYPHS.
		old_method = instance_method(func_name)
		define_method(func_name) { |numeral, ordinal=false|
			numeral.split("").each { |glyph| raise UnknownGlyphError unless glyphs.include? glyph }
			old_method.bind(self).call(numeral, ordinal)
			}
		end
	
	def inversion_test func_name
		# Post-parsing sanity check: when re-making the numeral, it should
		# be the same as the passed numeral.  This acts as a convenient sanity
		# check.
		old_method = instance_method(func_name)
		define_method(func_name) { |numeral, ordinal=false|
			n = old_method.bind(self).call(numeral, ordinal)
			new = make(n)
			raise FailedInversionTestError, "The numeral failed the inversion test: #{numeral} -> #{n}, but #{n} -> #{new}" if new != numeral
			return n
			}
		end
	
	end
