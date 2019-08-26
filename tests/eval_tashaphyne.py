#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testdom2.py
#  
#  

import sys
import xml.dom.minidom as minidom

sys.path.append('../')
#~ sys.path.append('../support")
from tashaphyne import stemming
import pyarabic.araby as ar
def display_word_seg(xmldoc, keep_tashkeel=False):
    """
    extract all possible segmentations
    return a dict of lists, the key is the word
    """
    word_dict = {}
    # get the annuaire list
    words = xmldoc.getElementsByTagName('w')
    #~ print words
    cpt = 0
    # display a word
    for word  in words:
        # every word contains choices
        word_value = word.getAttribute("rend")
        word_dict[word_value] = []
        choices = word.getElementsByTagName('choice')
        for choice in choices:
            #~ print choice.toxml()
            segs = choice.getElementsByTagName('seg')
            for seg in segs:
                #~ print seg.toxml()
                members = choice.getElementsByTagName('m')
                #~ segment={"word":word_value, }
                segment={}
                for mmbr in members:
                    mmbr_type = mmbr.getAttribute('type')
                    try:
                        mmbr_value = mmbr.firstChild.data
                    except:
                        mmbr_value = ""
                    if keep_tashkeel:
                        segment[mmbr_type] = mmbr_value
                    else:
                        segment[mmbr_type] = ar.strip_tashkeel(mmbr_value)

                word_dict[word_value].append(segment)
        # strip tashkeel generate duplicates segments
        if not keep_tashkeel:
            word_dict[word_value] = remove_duplicate(word_dict[word_value])
                #~ print (repr(segment)).decode('unicode-escape');
    return word_dict

def arepr(data):
    """ display a dict with arabic text properly """
    return repr(data).replace('}','}\n').decode('unicode-escape').encode('utf8')

def remove_duplicate(list_of_dict):
    """ remove duplicates dicts in a list """
    d = list_of_dict
    return [i for n, i in enumerate(d) if i not in d[n + 1:]]
    
def compare( list1, list2):
    """ compare two lists of dicts """
    pairs = zip(list1, list2)
    return len([(x, y) for x, y in pairs if x != y])
    
def included( list1, list2):
    """ if dict in the list """
    return list1[0] in list2

def main():
    """ Get Data Set"""
    DATA_FILE = 'samples/NAFIS_gold_standard.xml'
    try:
        xmldoc = open(DATA_FILE)
    except:
        print "Can't Open the file, first test", DATA_FILE
        sys.exit()
    try:
        xmldoc = minidom.parse(DATA_FILE)
    except:
        print "Can't Open the file", DATA_FILE
        sys.exit()
    word_dict = display_word_seg(xmldoc)
    #~ print repr(word_dict).replace('}','}\n').decode('unicode-escape')
    
    
    # test Tashaphyne
    stmer = stemming.ArabicLightStemmer()
    word_dict_tasha = {}
    total_score = 0
    total_seg_tasha = 0
    total_seg_nafis = 0

    scores = {}
    for word in word_dict.keys():
        stmer.segment(word)
        stmer.light_stem(word)
        segmentation = stmer.get_affix_list()
        word_dict_tasha[word] = segmentation
        print "*"*50
        print word.encode('utf8')
        print (arepr(word_dict[word]))
        print "-"*50
        print (arepr(segmentation))
        
        #~ score = compare(word_dict[word], segmentation)
        score = included(word_dict[word], segmentation)
        scores[word] = int(score)
        total_score += score
        total_seg_tasha += len(segmentation)
        total_seg_nafis += len(word_dict[word])
        print word.encode('utf8'), score
    print "-----scores --------"
    for k in scores:
        print k.encode('utf8'), scores[k]
    print "total_score", total_score
    print "total_seg_tasha", total_seg_tasha
    print "total_seg_nafis", total_seg_nafis       
        
    
if __name__ == '__main__':
    main()

