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

from utils import (
	int_to_base_array,
	split,
	hierarchicize
	)


# Test int_to_base_array()
for test in [
	(	(255,10),		[2,5,5]				),
	(	(256,10),		[2,5,6]				),
	(	(255,2),		[1,1,1,1,1,1,1,1]	),
	]:
	assert int_to_base_array(*test[0]) == test[1]


# Test split()
for test in [
	(	(1,1),			(1,0)		),
	(	(10,1),			(10,0)		),
	(	(0,1),			(0,0)		),
	(	(1.5,0.5),		(3,0)		),
	(	(1.5,1),		(1,0.5)		),
	(	(15,10),		(1,5)		),
	]:
	assert split(*test[0]) == test[1]

# Test hierarchicize()
for test in [
	(	(100,[1]),			[100]		),
	(	(100,[1,1]),		[100,0]		),
	(	(100,[100,1]),		[1,0]		),
	(	(1000,[360,12]),	[2,23]		),
	]:
	assert hierarchicize(*test[0]) == test[1]
