#!/usr/bin/python
# -*- coding=utf-8 -*-
#-----------------------------------------------------------------------
# Name:        light stemmer
# Purpose:     build an advanced stemmer for Information retreival 
#  
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     2016-06-14
# Copyright:   (c) Taha Zerrouki 2016
# Licence:     GPL
#-----------------------------------------------------------------------
"""
    Arabic text stemmer.
    Provides routins  to analyze text.
    Can treat text as verbs or as nouns.
"""

if __name__ == "__main__":
    import sys
    sys.path.append('../support')
    sys.path.append('../')

import re
import string
import datetime
import getopt
import os
import pyarabic.araby as araby
import tashaphyne.stemming



scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"
def usage():
# "Display usage options"
    print "(C) CopyLeft 2012, %s"%AuthorName
    print "Usage: %s -f filename [OPTIONS]" % scriptname
    print (u"       %s 'السلام عليكم' [OPTIONS]\n" % scriptname).encode('utf8');
#"Display usage options"
    print "\t[-f | --file= filename]input file to %s"%scriptname
    print "\t[-h | --help]     outputs this usage message"
    print "\t[-v | --version]  program version"
    print "\t[-l | --limit]    treat only a limited number of line"
    print "\t[-t | --stat]     enable statistics display"
    print "\r\nThis program is licensed under the GPL License\n"

def grabargs():
#  "Grab command-line arguments"
    fname = ''
    options={
    'strip':False,
    'full':False,
    'limit':False,
    'stat':False,
    'reduce':False,
}
    if not sys.argv[1:]:
        usage()
        sys.exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hVtlv:f:l:",
                               ["help", "version","stat", "limit=", "file="],)
    except getopt.GetoptError:
        usage()
        sys.exit(0)
    for o, val in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-V", "--version"):
            print scriptversion
            sys.exit(0)
        if o in ("-t", "--stat"):
            options['stat'] = True;
        if o in ("-l", "--limit"):
            try: options['limit'] = int(val);
            except: options['limit']=0;

        if o in ("-f", "--file"):
            fname = val
    utfargs=[]
    for a in args:
        utfargs.append( a.decode('utf8'));
    text= u' '.join(utfargs);

    #if text: print text.encode('utf8');
    return (fname, options)

            

    
if __name__ == '__main__':
    
    filename, options =grabargs()
    
    if not filename:
        usage()
        sys.exit(0)     

    try:
        myfile=open(filename)
    except:
        print " Can't Open the given File ", filename;
        sys.exit();
    counter = 1;
    if not options['limit'] : 
        limit =  100000000
    else: limit =0;

    # prepare stemmers
    # default stemmer
    dstemmer = tashaphyne.stemming.ArabicLightStemmer()
    
    nolimit = False;
    line = (myfile.readline()).decode('utf8');
    
    
    while line and (nolimit or counter<=limit):
        line = line.strip('\n')
        # the line contains the word and its stem
        fields = line.split('\t')
        if len(fields) >= 2:
            word = fields[0]
            stem = fields[1]
            dstemmer.light_stem(word)
            print (u"\t".join([word, stem, dstemmer.get_stem()])).encode('utf8')
            
        print line.encode('utf8')
        line=(myfile.readline()).decode('utf8');
