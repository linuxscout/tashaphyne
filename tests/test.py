#!/usr/bin/python
# -*- coding=utf-8 -*-
from tashaphyne.stemming import *
word=u"أفتضربونها"
word=u'‫أإنكم'
word_list =(
u'أأنت',
u'كالألبسة',
u'ألبسة',
u'الورد',
u'ورد',
u'فالورد',
u'بادية',
u'بدوية',
u'فيزياء',
u'والإنسان',
u'فكر',
u'‫تفكر',
u'‫ففكر',
u'الفكر',
u'فسوق',
u'الله',
u'لهن',
u'بسم',
u'فضَرَبْتُموهنَ',
u'فسيستعملونهما',
)
als=ArabicLightStemmer();
for word in word_list:
    newword= als.light_stem(word);
    stem=als.get_stem()
    prefix=als.get_prefix()
    suffix=als.get_suffix()
    root=als.get_root();
    print word.encode("utf8"),":",newword.encode("utf8"),
    print (u'-'.join([prefix,stem,suffix])).encode('utf8'),"\t",root.encode('utf8');

for word in word_list:
    listseg= als.segment(word);
    print word.encode("utf8"),listseg
    affix_list=als.get_affix_list();
    for affix in affix_list:
##        prefix=affix[0];
##        suffix=affix[0];
##        stem=affix[3];
        print als.get_word().encode('utf8'),(u'-'.join([affix['prefix'],affix['stem'],affix['suffix']])).encode('utf8'),"\t",affix['root'].encode('utf8'),als.normalize().encode("utf8");

