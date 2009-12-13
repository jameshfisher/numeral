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

class RomanNumeral < Numeral
	class << self
		extend NumeralDecorators
		
		CHARS = {
			'M'=> 1000,
			'D'=> 500,
			'C'=> 100,
			'L'=> 50,
			'X'=> 10,
			'V'=> 5,
			'I'=> 1
			}
		
		def make(number, ordinal=false)
			# Note that roman ordinal numbers are represented in the same way as cardinal.
			return 'nulla' if number == 0
			
			thousands, hundreds, tens, ones = Utils.hierarchicize(number, [1000,100,10,1])
			return 'M' * thousands +
				['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'][hundreds] +
				['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][tens] +
				['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][ones]
			end
		deny_large(:make, 1000000)	# This is a bit hazy.
		deny(:make, :float, :complex, :negative)
		
		def parse(numeral, ordinal=false)
			
			return 0 if numeral == 'NULLA'
			
			n = 0
			(0..numeral.length-1).each do |i|
				glyph = numeral[i]
				val = CHARS[glyph]
				next_val = CHARS[numeral[i+1]]
				if next_val != nil and val < next_val
					n -= val
				else
					n += val
					end
				end
			
			return n
			end
		inversion_test(:parse)
		deny_glyphs(:parse, CHARS.keys + 'nulla'.split(""))
		
		end
	end

if __FILE__ == $0
	require 'test/unit'
	class TestRomanNumeral < Test::Unit::TestCase
		require 'test_numeral'
		include TestNumeral
		
		def setup
			@numeral_class = RomanNumeral
			
			@test_cases = [
				[1, 'I'],
				[1000, 'M'],
				[99, 'XCIX'],
				[2009, 'MMIX'],
				]
			
			@parse_fails = [
				['ABC', UnknownGlyphError],
				['XMX', FailedInversionTestError],
				['IIII', FailedInversionTestError]
				]
			
			@make_fails = [
				[-1, NumberIsNegativeError]
				]
			end
		
		end
	end
