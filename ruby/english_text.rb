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
require 'errors'
require 'decorators'

require 'numeral'
class EnglishText < Numeral
    require 'indoeuropean_text'
    extend IndoEuropeanText
    
    SPECIAL_CASES = {}
    
    ORDINAL_UNITS = ['zeroth', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
    ORDINAL_TENS = ['zeroth', 'tenth', 'twentieth', 'thirtieth', 'fourtieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth']
    UNITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    TENS = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    CUSTOM_HUNDREDS = nil
    IGNORE_TENS = nil
    
    HUNDRED = Noun.new 'hundred'
    THOUSAND = Noun.new 'thousand'
    MILLION = Noun.new 'million'
    BILLION = Noun.new 'billion'
    
    MIDDLE_SEPARATOR = ', '
    END_SEPARATOR = ' and '
    
    JOINER_UNITS = ['-'] * 10
    end
