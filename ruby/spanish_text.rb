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

class SpanishText < IndoEuropeanText
	class << self
		extend NumeralDecorators
        
        UNITS = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
        TENS = ["cero", "diez", "viente", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        
        HUNDRED = Noun.new 'ciento'
        THOUSAND = Noun.new 'mil'
        MILLION = Noun.new 'millón', 'millónes'
        BILLION = Noun.new 'mil millones'
        
        CUSTOM_HUNDREDS = {
            0 => 'cien',
            1 => 'ciento',
            2 => 'doscientos',
            3 => 'trescientos',
            4 => 'cuatrocientos',
            5 => 'quinientos',
            6 => 'seiscientos',
            7 => 'setecientos',
            8 => 'ochocientos',
            9 => 'novecientos'
            }
        
        SPECIAL_CASES = {
            21 => 'veintiuno',
            22 => 'veintidós',
            23 => 'veintitres'
            }
        
        JOINER_UNITS = {
            1 => ' y ',
            2 => ' y ',
            3 => ' y ',
            4 => '-',
            5 => '-',
            6 => '-',
            7 => '-',
            8 => '-',
            9 => '-',
            }
        
        end
    end
        
