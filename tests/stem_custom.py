#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------
# Name:        stem_costumize
# Purpose:     Arabic lexical analyser, provides feature for 
#~stemming arabic word as noun
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     2017-02-15
# Copyright:   (c) Taha Zerrouki 2017
# Licence:     GPL
#-------------------------------------------------------------------------
"""
    Arabic noun stemmer
"""

import tashaphyne.stemming
import pyarabic.arabrepr
arepr = pyarabic.arabrepr.ArabicRepr()
repr = arepr.repr

CUSTOM_PREFIX_LIST = [u'كال', u'أفبال', u'أفك', u'فك', u'أولل', u'', u'أف', u'ول', u'أوال', u'ف', u'و', u'أو', u'ولل', u'فب', u'أول', u'ألل', u'لل', u'ب', u'وكال', u'أوب', u'بال', u'أكال', u'ال', u'أب', u'وب', u'أوبال', u'أ', u'وبال', u'أك', u'فكال', u'أوك', u'فلل', u'وك', u'ك', u'أل', u'فال', u'وال', u'أوكال', u'أفلل', u'أفل', u'فل', u'أال', u'أفكال', u'ل', u'أبال', u'أفال', u'أفب', u'فبال']
CUSTOM_SUFFIX_LIST = [u'كما', u'ك', u'هن', u'ي', u'ها', u'', u'ه', u'كم', u'كن', u'هم', u'هما', u'نا']

# simple stemmer with default affixes list
simple_stemmer = tashaphyne.stemming.ArabicLightStemmer()

# create a costomized stemmer object for stemming enclitics and procletics
custom_stemmer = tashaphyne.stemming.ArabicLightStemmer()
# configure the stemmer object
custom_stemmer.set_prefix_list(CUSTOM_PREFIX_LIST)
custom_stemmer.set_suffix_list(CUSTOM_SUFFIX_LIST)

word = u"بالمدرستين"
# segment word as 
simple_stemmer.segment(word)
print  repr(simple_stemmer.get_affix_list())

custom_stemmer.segment(word)

print  repr(custom_stemmer.get_affix_list())






