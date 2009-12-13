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

class Noun
    def initialize singular, plural=nil
        @singular = singular
        @plural = (plural ? plural : singular)
        end
    def get qty
        return @singular if qty == 1
        return @plural
        end
    end

module IndoEuropeanText
    extend NumeralDecorators
    
    def make(number, ordinal=false)
        return self::SPECIAL_CASES[number] if self::SPECIAL_CASES.include? number
        
        return {false => self::UNITS, true: self::ORDINAL_UNITS}[ordinal][number] if number < 20
        
        texts = [] #here we add the 'bits' of the text which will later be concatenated in a list, e.g. 'one thousand', 'one hundred' and 'forty-four'
        
        billions, millions, thousands, hundreds, tens, units = Utils.hierarchicize(number, [1_000_000_000, 1_000_000, 1000, 100, 10, 1])
        
        # First, get the big amounts out of the way.
        [
            [1_000_000_000, billions, self::BILLION],
            [1_000_000, millions, self::MILLION],
            [1000, thousands, self::THOUSAND],
            [100, hundreds, self::HUNDRED],
        ].each do |unit, quantity, name|
            if quantity == 0
                texts.push(self::CUSTOM_HUNDREDS[0]) if self::CUSTOM_HUNDREDS
                next
                end
            if unit == 100 and self::CUSTOM_HUNDREDS; texts.push(self::CUSTOM_HUNDREDS[quantity]); next; end    # Stupid case for spanish
            texts.push(( (unit == 1000 and quantity == 1 and self::DROP_ONE_THOUSAND) ? name.get(quantity) : make(quantity) + ' ' + name.get(quantity) ))   # Note the recursive call
            end
        
        # Now add the bits below one hundred.
        
        if units > 0 and self::IGNORE_TENS and self::IGNORE_TENS.include? tens
            tens -= 1
            units += 10
            end
        
        if tens > 0 or units > 0    # there's something to append
            last_bit = ''
            if tens > 0
                last_bit = self::TENS[tens]
                last_bit += self::JOINER_UNITS[units] if units > 0 #spanish demands 'treinta y uno', etc.
                end
            last_bit += self::UNITS[units] if units > 0
            texts.push(last_bit)
            end
        
        #Finally, just concatenate the pieces.
        last = texts.pop
        return (texts.length > 0 ? texts.join(self::MIDDLE_SEPARATOR) + self::END_SEPARATOR : '') + last
        end
    deny(:make, :float, :complex, :negative)
    
    end
	

