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


module TestNumeral
	def test_parse
		@test_cases.each { |number, numeral|
			
			# I'm not sure all of the following are really positively necessary...
			#parsed = @numeral_class.parse(numeral)
			made = @numeral_class.make(number)
			
			#assert_equal parsed, number
			assert_equal made, numeral
			
			#reparsed = @numeral_class.parse(made)
			#remade = @numeral_class.make(parsed)
			
			#assert_equal reparsed, number
			#assert_equal remade, numeral
			}
		end

	def test_fail_parse
		@parse_fails.each { |nonsense, error|
			assert_raise(error) { @numeral_class.parse(nonsense) }
			}
		end
	
	def test_fail_make
		@make_fails.each { |nonsense, error|
			assert_raise(error) { @numeral_class.make(nonsense) }
			}
		end
	
	end
