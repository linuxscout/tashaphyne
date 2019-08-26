#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  lookup for root in dictionary

import pyarabic.araby as araby
from pyarabic import stack
from pyarabic.araby import FEH, LAM, AIN, HARAKAT
from pyarabic.arabrepr import arepr
import re
import roots_const        
class rootsDict:
    """ lookup for root list """
    def __init__(self,):
        pass
    @staticmethod
    def is_root(word):
        """ test if word is a root"""
        return word in roots_const.ROOTS
    @staticmethod
    def normalize_root(word):
        """ test if word is a root"""
        # change alef madda to hamza + ALEF
        word = word.replace(araby.ALEF_MADDA, araby.HAMZA+ araby.ALEF)
        word = word.replace(araby.TEH_MARBUTA, '')
        word = word.replace(araby.ALEF_MAKSURA, araby.YEH)
        return araby.normalize_hamza(word)

    @staticmethod
    def most_common(lst):
        triroots = [x for x in lst if len(x) == 3]
        if triroots:
            lst = triroots
        return max(set(lst), key=lst.count)

    @staticmethod
    def filter_root_length_valid(roots):
        
        return [x for x in roots if len(x) >= 3 and len(x)<=4 and araby.ALEF not in x]
    
    def lookup_roots(roots):
        """ lookup roots in dictionary"""
        set_roots = filter(self.is_root, set(roots))
        accepted = [x for x in roots if x in set_roots]
        return accepted        

    def choose_root(self, word, affixation_list, debug = False):
        """ test an algorithm to choose roots"""
        accepted = []
        all_accepted = []
        
        # if all algo, all algorithms will be tested over roots
        # we think to test all algorithms then get the most common root
        # the secnd way when all_algorithms is false, we use if else to get the given root, and stop when we can get one at least
        all_algo = True
        algos = self.algos
        #roots
        stems = [ self.normalize_root(d['stem']) for d in affixation_list]
        roots = [ self.normalize_root(d['root']) for d in affixation_list]
        prefixes = [ d['prefix'] for d in affixation_list]
        suffixes = [ d['suffix'] for d in affixation_list]
        #~ print("rootslibclass:", arepr(affixation_list))
     
        
        if all_algo or not accepted:

            # get uniq root
            #~ accepted = list(set(filter(.is_root, roots)))
            # avoid non 3-4 letters roots
            roots_tmp =  self.filter_root_length_valid(roots)
            # lookup for real roots
            accepted = filter(self.is_root, roots_tmp)
            self.debug_algo(debug, word, 1 , "default", roots, roots, roots_tmp, accepted)
            # to handle all accepted together
            all_accepted.extend(accepted)

        # Stems as roots
        #~ if not all_accepted :#all_algo or not accepted:
        if all_algo or not accepted:

            # avoid non 3-4 letters roots
            roots_tmp =  self.filter_root_length_valid(stems)
            # lookup for real roots
            accepted = filter( self.is_root, roots_tmp)
            all_accepted.extend(accepted)            
            self.debug_algo(debug, word, 2 , "default as stem", stems, stems, roots_tmp, accepted)
        # as stem_default and default are not exact method, we can reduce their effect
        # by reducing generated roots to a set
        #~ all_accepted = list(set(all_accepted))   
        if all_algo and all_accepted: 
            return  self.most_common(all_accepted)
        elif accepted:
            #select tri-letter before selecting 4 letters
            return  self.most_common(accepted)
        else:
            return ''
        
  
def test1(args):
    word = u"لعلهم"
    print(is_root(word))
    word = u"علم"
    print(is_root(word))
    
    #test with tashaphyne
    from tashaphyne.stemming import ArabicLightStemmer
    asl = ArabicLightStemmer()        
    words = [u'أفتضاربانني',
    u'بأبأ',
    u'يريدون',
    u'يستطعن',
    u'كتاب',
    u"بالميدان",
    u"بالأسيهم",
    
    ]
    ext = extend_root(u"رم")
    print ("extende")
    print(repr(ext).decode('unicode-escape').encode('utf8'))

    for word in words:
        print(u"**********%s*********"%word)
        asl.light_stem(word)
        asl.segment(word)
        print(asl.get_segment_list())  
        seg_list = asl.get_segment_list()  
        starstem_list =[]
        for seg in seg_list:
            left, right = seg
            starstem_list.append(asl.get_starstem(left, right))
        print("star stems")
        
        print (u"\t".join(starstem_list)).encode('utf8')
        filtered_starstem_list =filter(valid_starstem, starstem_list)
        print("filtred star stem")
        print (u"\t".join(filtered_starstem_list)).encode('utf8')
        for st in starstem_list:
            print(st, u"\t".join(valid_starstem(st)).encode('utf8'))
        affixation_list= asl.get_affix_list()
        stems = [d['stem'] for d in affixation_list]
        print ("Candidats stems%s"%u'\t'.join(stems))
        for st in stems:
            print( st, u"\t".join(valid_starstem(st)).encode('utf8') )       
        
        print( repr(affixation_list).replace('},','},\n').decode('unicode-escape').encode('utf8'))
        print("reduce")
        #~ affixation_list = filter(verify_affix, affixation_list)
        print(repr(affixation_list).replace('},','},\n').decode('unicode-escape').encode('utf8'))

        roots = [normalize_root(d['root']) for d in affixation_list]
        print ("Candidats %s"%u'\t'.join(roots))
        # get uniq root
        accepted = set(filter(is_root, roots))
        print ("accepted %s"%u'\t'.join(accepted))
        if not accepted:
            # try to extend roots
            
            extended_roots = []
            for x in roots:
                extended_roots.extend(extend_root(x))
            print ("Candidats extended %s"%u'\t'.join(extended_roots))
            accepted = set(filter(is_root, extended_roots ))
            print ("accepted level2 %s"%u'\t'.join(accepted))            
        print('root %s'%asl.get_root())
    #~ print repr(STAMP_DICT).replace('},','},\n').decode('unicode-escape').encode('utf8')
    return 0

def test2():
    #test with tashaphyne
    from tashaphyne.stemming import ArabicLightStemmer
    asl = ArabicLightStemmer()        
    words = [(u'أفتضاربانني',u'ضرب'),
    (u'بأبأ',u'بءبء'),
    (u'يريدون',u'ريد'),
    (u'يستطعن', u'ريد'),
    (u'كتاب',u'كتب'),
    (u"بالميدان",u'ميد'),
    (u"بالأسيهم",u'سهم'),
    (u"آخرين",u'ءخر'),
    (u"بالأخرة",u'ءخر'),
    
    ]
    for word, root in words:
        print(u"**********%s*********"%word)
        asl.light_stem(word)
        asl.segment(word)
        print(asl.get_segment_list())  
        seg_list = asl.get_segment_list()  
        seg_list = asl.get_segment_list()  
        starstem_list =[]
        affixa_list = asl.get_affix_list()
        #~ root_result = choose_root(affixa_list, debug=True)
        root_result = choose_root(word, affixa_list, debug=True)
        print(root_result, root_result == root)
    return 0

def diff(first, second):
    """
    """
    second = set(second)
    return [item for item in first if item not in second]
    
def test3():
    from pyarabic.arabrepr import arepr
    #test with tashaphyne
    from tashaphyne.stemming import ArabicLightStemmer
    asl = ArabicLightStemmer() 
    rooter = rootDict()       
    words = [(u'أفتضاربانني',u'ضرب'),
    #~ (u'بأبأ',u'بءبء'),
    #~ (u'يسعى',u'سعى'),
    #~ (u'يريدون',u'ريد'),
    #~ (u'يستطعن', u'ريد'),
    #~ (u'كتاب',u'كتب'),
    #~ (u"بالميدان",u'ميد'),
    #~ (u"بالأسيهم",u'سهم'),
    #~ (u"آخرين",u'ءخر'),
    #~ (u"بالأخرة",u'ءخر'),
    #~ ('ويرمي',u'رمي'),
#~ (u'ويرمي',u'رمي'),
#~ (u'يرمون',u'رمي'),
#~ (u'راميات',u'رمي'),
#~ (u'وترمون',u'رمي'),
#~ (u'ويرمين',u'رمي'),
#~ (u'وترميان',u'رمي'),
#~ (u'ورامون',u'رمي'),
#~ (u'وليرميان',u'رمي'),
#~ (u'لترميان',u'رمي'),
#~ (u'لترمين',u'رمي'),
#~ (u'رامي',u'رمي'),
#~ (u'ورامي',u'رمي'),
#~ (u'رماية',u'رمي'),
#~ (u'رمايه',u'رمي'),
#~ (u'الراميات',u'رمي'),
#~ (u'المرميات',u'رمي'),
#~ (u'المتراميات',u'رمي'),
#~ (u'مترامية',u'رمي'),
#~ (u'مترامي',u'رمي'),
#~ (u'الرامون',u'رمي'),
#~ (u'والراميات',u'رمي'),
#~ (u'وسيقولون',u'قول'),
#~ (u'وسيقال',u'قول'),
#~ (u'وسيقيلوهم',u'قول'),
#~ (u'وتقال',u'قول'),
#~ (u'وتقولوا',u'قول'),
#~ (u'وتقول',u'قول'),
#~ (u'ومقاول',u'قول'),
#~ (u'وقالوا',u'قول'),
#~ (u'ومقال',u'قول'),

(u'وتقل', u'قول'),
(u'وتقلن', u'قول'),
(u'وليقل', u'قول'),
(u'ولتقلنا', u'قول'),
(u'لتقل', u'قول'),
(u'تقل', u'قول'),
(u'ونقل', u'قول'),
(u'ولنقل', u'قول'),
(u'فتقل', u'قول'),
(u'ستقل', u'قول'),
(u'ستقلن', u'قول'),
(u'وستقلن', u'قول'),
(u'فستقل', u'قول'),

(u'وقالوا', u'قول'),
(u'قالوا', u'قول'),
(u'وقالا', u'قول'),
(u'قالا', u'قول'),
(u'وقالت', u'قول'),
(u'قالت', u'قول'),
(u'ويقال', u'قول'),
(u'يقال', u'قول'),
(u'وسيقال', u'قول'),
(u'سيقال', u'قول'),
(u'ويقلن', u'قول'),
(u'يقلن', u'قول'),
(u'ويقلنا', u'قول'),
(u'يقلنا', u'قول'),
(u'وتقال', u'قول'),
(u'تقال', u'قول'),
(u'وقال', u'قول'),
(u'قال', u'قول'),
(u'وسأقول', u'قول'),
(u'سأقول', u'قول'),
(u'وقائل', u'قول'),
(u'قائل', u'قول'),
(u'وقائلان', u'قول'),
(u'قائلان', u'قول'),
(u'وقائلون', u'قول'),
(u'قائلون', u'قول'),
(u'وقائلا', u'قول'),
(u'قائلا', u'قول'),
(u'ومقال', u'قول'),
(u'مقال', u'قول'),
(u'وقائلتان', u'قول'),
(u'قائلتان', u'قول'),
(u'يعد', u'وعد'),
(u'تعد', u'عدد'),
(u'نعدهم', u'عدد'),
(u'وتعدهم',u'وعد'),
(u'تعدهم',u'وعد'),
(u'وستعدهم',u'وعد'),
(u'ستعدهم',u'وعد'),
(u'وتعدهما',u'وعد'),
(u'تعدهما',u'وعد'),
(u'ويعدهم',u'وعد'),
(u'يعدهم',u'وعد'),
(u'ويعدهما',u'وعد'),
(u'يعدهما',u'وعد'),
(u'وسيعدهم',u'وعد'),
(u'سيعدهم',u'وعد'),
(u'وسيعدهما',u'وعد'),
(u'سيعدهما',u'وعد'),
(u'ولنعدهم',u'وعد'),
(u'لنعدهم',u'وعد'),
(u'ولنعدهما',u'وعد'),
(u'لنعدهما',u'وعد'),
(u'ولتعدهم',u'وعد'),
(u'لتعدهم',u'وعد'),
(u'ولتعدهما',u'وعد'),
(u'لتعدهما',u'وعد'),
(u'ولتعدها',u'وعد'),
(u'لتعدها',u'وعد'),
(u'وستعدها',u'وعد'),
(u'ستعدها',u'وعد'),
(u'ووعدها',u'وعد'),
(u'وعدها',u'وعد'),
(u'ووعدهم',u'وعد'),
(u'وعدهم',u'وعد'),
(u'ووعدهما',u'وعد'),
(u'وعدهما',u'وعد'),
(u'وتعد',u'وعد'),
(u'تعد',u'وعد'),
(u'وتعدني',u'وعد'),
(u'تعدني',u'وعد'),
(u'وتعدنا',u'وعد'),
(u'تعدنا',u'وعد'),
(u'وتعده',u'وعد'),
(u'تعده',u'وعد'),
(u'وواعدناهم',u'وعد'),
(u'واعدناهم',u'وعد'),
(u'ووعدناهم',u'وعد'),
(u'وعدناهم',u'وعد'),
(u'وتعدوهم',u'وعد'),
(u'تعدوهم',u'وعد'),
(u'يعتاد',u'عود'),
(u'أحست',u'حسس'),
(u'يحسون',u'حسس'),
(u'ثقة',u'وثق'),
(u'ثقات',u'وثق'),
(u'بثقات',u'وثق'),
(u'صفات',u'وصف'),
(u'صلاته',u'وصل'),

    ]
    for word, root in words:
        print((u"**********%s*********"%word).encode('utf8'))
        asl.light_stem(word)
        asl.segment(word)
        print(asl.get_segment_list()  )
        seg_list = asl.get_segment_list()  
        starstem_list =[]
        affixa_list = asl.get_affix_list()
        stems = [ d['stem'] for d in affixa_list]
        print(u' '.join(stems).encode('utf8'))
        #~ root_result = rooter.choose_wazn_root(affixa_list, debug=True)
        root_result = rooter.choose_root(word, affixa_list, debug=True)
        print("Test root",root_result.encode('utf8'), "found root",root_result.encode('utf8'), root_result == root)
    # test root_extension
    roots=[u"قل",
    u"دع",
    ]
    for rt in roots:
        extended = rooter.extend_root(rt)
        print(u"\t".join([rt, u";".join(extended)]).encode('utf8'))
    print('stamped roots', len(rooter.STAMP_DICT ))
    print('stamped roots diff new', len(diff(rooter.STAMP_DICT,roots_const.ROOTS )))
    print('stamped roots removed', len(diff(roots_const.ROOTS, rooter.STAMP_DICT )))
    print('stamped roots max length', max((len(v), k, v) for k,v in rooter.STAMP_DICT.iteritems()))
    print('virtual roots', len(rooter.VIRTUAL_DICT))
    print('virtual roots diff', len(diff(rooter.VIRTUAL_DICT,roots_const.ROOTS )))
    print('virtual roots removed ', len(diff(roots_const.ROOTS, rooter.VIRTUAL_DICT )))
    print('virtual roots max length', max((len(v),k, v) for k,v in rooter.VIRTUAL_DICT.iteritems()))
    
    print('all roots', len(roots_const.ROOTS))

        
    return 0
if __name__ == '__main__':
    test3()
