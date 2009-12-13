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

ORDINAL_UNITS = {
	'fr': [],
	'en': ['zeroth', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth'],
	'es': []
	}

ORDINAL_TENS = {
	'fr': [],
	'en': ['zeroth', 'tenth', 'twentieth', 'thirtieth', 'fourtieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth'],
	'es': []
	}

UNITS = {
	'fr': ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"],
	'en': ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
	'es': ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
	}

TENS = {
	'fr': ["zéro", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"],
	'en': ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
	'es': ["cero", "diez", "viente", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
	}

BIG_NUMBERS = {
	100: {
		'singular': {
			'fr': 'cent',
			'en': 'hundred',
			'es': 'ciento'
			},
		'plural': {
			'fr': 'cents',
			'en': 'hundred',
			'es': ''
			}
		},
	1000: {
		'singular': {
			'fr': 'mille',
			'en': 'thousand',
			'es': 'mil'
			},
		'plural': {
			'fr': 'mille',
			'en': 'thousand',
			'es': 'mil'
			}
		},
	1000000: {
		'singular': {
			'fr': 'million',
			'en': 'million',
			'es': 'millón'
			},
		'plural': {
			'fr': 'millions',
			'en': 'million',
			'es': 'millónes'
			}
		},
	1000000000: {
		'singular': {
			'fr': 'milliard',
			'en': 'billion',
			'es': 'mil millones'
			},
		'plural': {
			'fr': 'milliards',
			'en': 'billion',
			'es': 'mil millones'
			}
		}
	}

INT_TO_TEXT_SEPARATOR = {
	'middle': {
		'fr': ' ',
		'en': ', ',
		'es': ' '
		},
	'end': {
		'fr': ' ',
		'en': ' and ',
		'es': ' '
		}
	}



ORDINAL, CARDINAL = range(2)
def int_to_text(num, lang='en', number_type=CARDINAL):	
	num = int(num)
	
	if(num<20):
		if number_type == ORDINAL:
			return ORDINAL_UNITS[lang][num]
		else:
			return UNITS[lang][num]

	texts = [] #here we add the 'bits' of the text which will later be concatenated in a list, e.g. 'one thousand', 'one hundred' and 'forty-four'

	others = BIG_NUMBERS.keys()
	others_amt = {}
	for i in range(len(others)):
		v = math.floor(num / others[i])
		others_amt[others[i]] = v
		num -= v * others[i]
		
		if v > 0:
			if others[i] == 100 and lang == 'es': #spanish has funny words for numbers of hundreds
				spanish_hundreds = {
					1: 'ciento',
					2: 'doscientos',
					3: 'trescientos',
					4: 'cuatrocientos',
					5: 'quinientos',
					6: 'seiscientos',
					7: 'setecientos',
					8: 'ochocientos',
					9: 'novecientos'
					}
				if num == 0:
					texts.append('cien')
				else:
					texts.append(spanish_hundreds[v])
			else:
				if v > 1:
					texts.append(int_to_text(v, lang) + ' ' + BIG_NUMBERS[others[i]]['plural'][lang])
				else:
					if lang == 'es' and others[i] == 1000: #spanish shouldn't be 'uno mil'; just 'mil'
						texts.append(BIG_NUMBERS[others[i]]['singular'][lang])
					else:					
						texts.append(int_to_text(v, lang) + ' ' + BIG_NUMBERS[others[i]]['singular'][lang])

	tens = math.floor(num / 10)
	num -= tens*10
	units = num
	
	if lang == 'es' and tens == 2 and units in [1,2,3]: #stupid spanish 21,22,23
		if units == 1:
			texts.append('veintiuno')
		elif units == 2:
			texts.append('veintidós')
		elif units == 3:
			texts.append('veintitres')
	else: #do things as normal
		if tens > 1:
			a = TENS[lang][int(tens)]
			if lang == 'fr':
				if tens == 7:
					a = t[lang][6]
				elif tens == 9:
					a =names.TENS[lang][8]
			if units > 0:
				if lang=='fr' and (tens == 7 or tens == 9): #if we're doing the weird french 'sixty-ten' or 'eighty-ten'
					if units == 1:
						a+= "et un"
					else:
						a+= "-"+u[lang][int(10+units)]
				else: #we're doing the english tens-units representation
					if lang == 'fr' and units == 1: #french demands extra 'et un', not just 'un'
						a+= " et un"
					elif lang == 'es' and units in [1,2,3]: #spanish demands 'treinta y uno', etc.
						a += " y " + names.UNITS[lang][int(units)]
					else:
						a+= "-"+names.UNITS[lang][int(units)]
			texts.append(a)
		elif units > 1:
			texts.append(names.UNITS[lang][int(units)])

	#concatenate the pieces
	s = ""
	for i in range(len(texts)):
		if i == 0:
			s += texts[i]
		elif i == len(texts) - 1:
			s += names.INT_TO_TEXT_SEPARATOR['end'][lang] + texts[i]
		else:
			s += names.INT_TO_TEXT_SEPARATOR['middle'][lang] + texts[i]
	return s
