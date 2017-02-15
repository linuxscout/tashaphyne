from Tashaphyne.stemming import *
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
)
als=ArabicLightStemmer();
for word in word_list*10000:
    newword= als.lightStem(word);
    stem=als.get_stem()
    prefix=als.get_prefix()
    suffix=als.get_suffix()
    root=als.get_root();
    print word.encode("utf8"),":",newword.encode("utf8"),
    print (u'-'.join([prefix,stem,suffix])).encode('utf8'),"\t",root.encode('utf8');
