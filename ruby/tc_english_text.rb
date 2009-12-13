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

require 'test/unit'
class TC_EnglishText < Test::Unit::TestCase
    require 'test_numeral'
    include TestNumeral
    
    def setup
        require 'english_text'
        @numeral_class = EnglishText
        
        @test_cases = [
            [0, 'zero'],
            [1, 'one'],
            [9, 'nine'],
            [10, 'ten'],
            [13, 'thirteen'],
            [20, 'twenty'],
            [21, 'twenty-one'],
            [100, 'one hundred'],
            [101, 'one hundred and one'],
            [500_000, 'five hundred thousand']
            ]
        
        @parse_fails = [
            ['one', NotImplementedError]
            ]
        
        @make_fails = [
            [-1, NumberIsNegativeError]
            ]
        end
    
    end

