from stemming import *
##token_pat=re.compile(u"[^\w\u064b-\u0652]+",re.U);
text=u"""
﴿وَأَنزَلْنَا إِلَيْكَ الْكِتَابَ بِالْحَقِّ مُصَدِّقاً لِّمَا بَيْنَ يَدَيْهِ مِنَ الْكِتَابِ وَمُهَيْمِناً عَلَيْهِ﴾[4]. كما يؤمن المسلمون بأن محمداً رسول من الله وخاتم للأنبياء والمرسلين وأن الله أرسله إلى الثقلين كافة
"""
tasha=ArabicLightStemmer();
word_list =tasha.tokenize(text);
##word_list=token_pat.split(text);
for word in word_list:
    print word.encode('utf8')