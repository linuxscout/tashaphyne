#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testdom2.py
#  
#  


import xml.dom.minidom as minidom

def display_word_seg(xmldoc):
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
                segment={"word":word_value, }
                for mmbr in members:
                    mmbr_type = mmbr.getAttribute('type')
                    try:
                        mmbr_value = mmbr.firstChild.data
                    except:
                        mmbr_value = ""
                    segment[mmbr_type] = mmbr_value
                word_dict[word_value].append(segment)
                #~ print (repr(segment)).decode('unicode-escape');
    return word_dict


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
    print repr(word_dict).replace('}','}\n').decode('unicode-escape')
    
    
    # test Tashaphyne
    
if __name__ == '__main__':
    main()

