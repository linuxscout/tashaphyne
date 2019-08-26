#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testdom2.py
#  
#  


import xml.dom.minidom as minidom
#~ import xml.dom  as minidom
import sys
def display_personnes(xmldoc):
    #get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print personnes
    cpt = 0
    # display personne by personne
    for personne  in personnes:
        print "-"*40
        print "Personne n°", cpt
        print personne.toxml()
        cpt += 1
def display_tel(xmldoc):
    # display only telephones
     # get the tel list
    telephones = xmldoc.getElementsByTagName('telephone')
    print telephones
    cpt = 0
    # display tel by tel
    for tel  in telephones:
        print "-"*40
        print "Tel n°", cpt
        print tel.toxml()
        print "N°:",tel.firstChild.data
        print "Type:",tel.getAttribute("type")
        cpt += 1
        
def display_tel_personne(xmldoc):
    #get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print personnes
    cpt = 0
    # display telephone by personne
    for personne  in personnes:
        print "-"*40
        print "Personne n°", cpt
        nom    = personne.getElementsByTagName('nom')[0]
        prenom = personne.getElementsByTagName('prenom')[0]
        tels   = personne.getElementsByTagName('telephone')
        print "*"*20
        print "Nom:\t",nom.firstChild.data
        print "Prénom:\t",prenom.firstChild.data
        for tel in tels:
            print "-"*20
            print "N°:",tel.firstChild.data
            print "Type:",tel.getAttribute("type")
        cpt += 1
def add_id_personne(xmldoc):
    #get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print personnes
    cpt = 0
    # display personne by personne
    for personne  in personnes:
        print "-"*40
        print "Personne n°", cpt, personne.nodeValue, personne.nodeType,
        personne.setAttribute('id', str(cpt))
        cpt += 1 
        print personne.toxml()
def add_child_personne(xmldoc):
    #get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print personnes
    cpt = 0
  
    # display personne by personne
    for personne  in personnes:
        print "-"*40
        print "Personne n°", cpt, personne.nodeValue, personne.nodeType,
        personne.setAttribute('id', str(cpt))
        cpt += 1 
        fils = xmldoc.createElement("age") 
        #~ fils_text = xmldoc.createTextNode("24") 
        #~ fils.appendChild(fils_text)
        fils.insertData("TAHAHAAHAHA")
        personne.appendChild(fils)      
        print personne.toxml()
        f = personne.getElementsByTagName('nom')[0]
        personne.removeChild(f) 
        #~ personne.removeChild("age") 
        print personne.toxml()          

def lookup_for_tel(xmldoc, tel_num):
    #get the personnes list
    tels = xmldoc.getElementsByTagName('telephone')
    print tels
    # display tel
    for tel in tels:
        tel_type = tel.getAttribute('type')
        tel_number     = tel.firstChild.data
        if tel_number == tel_num:
            adresse  = tel.parentNode
            identite = adresse.parentNode
            print "owner", identite.toxml()
            for elem in identite.childNodes:
                print "---- element----"
                print elem.toxml()
            nom      = identite.childNodes[1].firstChild.data
            print "owner", nom#.toxml()
        print tel_type, tel_number
def display_node(node, level):
    print "  "*level, "Type", node.nodeType, "Name:", node.nodeName , "nodevalue", node.nodeValue, 
    #~ print node.toxml()
    if node.nodeType == node.TEXT_NODE:
        #~ print node.toxml()
        print  "Value:",node.data, "nodevalue", node.nodeValue
    else :
        print ;

                  

def display_word_seg(xmldoc):
    # get the annuaire list
    words = xmldoc.getElementsByTagName('w')
    #~ print words
    cpt = 0
    # display a word
    for word  in words:
        # every word contains choices
        word_value = word.getAttribute("rend")
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
                print (repr(segment)).decode('unicode-escape');

def display_word(xmldoc):
    # get the annuaire list
    words = xmldoc.getElementsByTagName('w')
    #~ print words
    cpt = 0
    # display a word
    for word  in words:
        # every word contains choices
        word_value = word.getAttribute("rend")
        print word_value.encode('utf-8');
                    
        cpt += 1

def treat_doc(xmldoc):
    # get the annuaire list
    text = xmldoc.getElementsByTagName('text')[0]
    print text
    cpt = 0
    # display phrase
    for phrase  in text.childNodes:
        print "-"*40
        print "Phrase", cpt
        print "'%s'"%phrase.toxml()
        cpt += 1

def main():
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
    #~ treat_doc(xmldoc)
    display_word(xmldoc)
    display_word_seg(xmldoc)
    
    #~ treat_doc(xmldoc)
    #~ display_tel_personne(xmldoc)
    #~ add_id_personne(xmldoc)
    #~ lookup_for_tel(xmldoc, "071002500")
    #~ display_tree(xmldoc)
    #~ display_personnes(xmldoc)
    add_child_personne(xmldoc)
    return 0
if __name__ == '__main__':
    main()

