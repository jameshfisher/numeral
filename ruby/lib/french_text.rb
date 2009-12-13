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
require 'numeral_base'
require 'errors'
require 'decorators'

class FrenchText < NumeralBase
    require 'indoeuropean_text'
    extend IndoEuropeanText
	
    SPECIAL_CASES = {}
    
    ORDINAL_UNITS = []
    ORDINAL_TENS = []
    UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    TENS = ["zéro", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]
    
    IGNORE_TENS = [7, 9]
    
    CUSTOM_HUNDREDS = nil
    
    HUNDRED = Noun.new 'cent', 'cents'
    THOUSAND = Noun.new 'mille'
    MILLION = Noun.new 'million', 'millions'
    BILLION = Noun.new 'milliard', 'milliards'
    
    MIDDLE_SEPARATOR = ' '
    END_SEPARATOR = ' '
    
    JOINER_UNITS = ['-'] * 20
    JOINER_UNITS[1] = ' et '
    
    end
        
