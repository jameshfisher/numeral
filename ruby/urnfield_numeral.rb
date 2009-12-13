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


require 'utils'
require 'numeral'
require 'errors'
require 'decorators'

class UrnfieldNumeral < Numeral
	class << self
		extend NumeralDecorators
		
		private
		GLYPHS = {
			'/' => 1,
			"\\" => 5
			}
		INVERSE_MAPPING = GLYPHS.invert
		
		public
		
		def make(number, ordinal=false)
			fives, ones = Utils.split(number, 5)
			return INVERSE_MAPPING[1] * ones + INVERSE_MAPPING[5] * fives
			end
		deny_large(:make, 20)
		deny(:make, :float, :complex, :negative, :zero)
		
		def parse(numeral, ordinal=false)
			numeral.split("").map { |glyph| GLYPHS[glyph] }.sum
			end
		inversion_test(:parse)
		deny_glyphs(:parse, GLYPHS.keys)
		
		end
	end
