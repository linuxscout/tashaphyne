# -*- coding: UTF-8 -*-
"""
Arabic Light Stemmer
A class which provides a configurable stemmer
and segmentor for arabic text.

Features:
=========

    - Arabic word Light Stemming.
    - Root Extraction.
    - Word Segmentation
    - Word normalization
    - Default Arabic Affixes list.
    - An customizable Light stemmer: possibility of change
    stemmer options and data.
    - Data independent stemmer


@author: Taha Zerrouki <taha_zerrouki at gmail dot com>
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies,  Arabeyes,   Taha Zerrouki
@license: GPL
@date:2017/02/15
@version:0.3
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import  re
import sys
sys.path.append('../support/')
import pyarabic.araby as araby
if __name__ == "__main__":
    sys.path.append('../')
    import normalize
    import stem_const
    import affix_const
    import roots_const 
    import verb_stamp_const 
    import arabicstopwords      
else:
    from . import normalize
    from . import stem_const
    from . import affix_const
    from . import roots_const  
    from . import verb_stamp_const  
    from . import arabicstopwords
class ArabicLightStemmer:
    """
    ArabicLightStemmer: a class which proved a configurable stemmer
    and segmentor for arabic text.

    Features:
    =========

        - Arabic word Light Stemming.
        - Root Extraction.
        - Word Segmentation
        - Word normalization
        - Default Arabic Affixes list.
        - An customizable Light stemmer: possibility of change
        stemmer options and data.
        - Data independent stemmer


    @author: Taha Zerrouki <taha_zerrouki at gmail dot com>
    @author: Taha Zerrouki
    @contact: taha dot zerrouki at gmail dot com
    @copyright: Arabtechies,  Arabeyes,   Taha Zerrouki
    @license: GPL
    @date:2017/02/15
    @version:0.3
    """
    def __init__(self):
        #load affix information
        # pass
        self.prefix_letters = stem_const.DEFAULT_PREFIX_LETTERS
        self.suffix_letters = stem_const.DEFAULT_SUFFIX_LETTERS
        self.infix_letters = stem_const.DEFAULT_INFIX_LETTERS
        self.max_prefix_length = stem_const.DEFAULT_MAX_PREFIX
        self.max_suffix_length = stem_const.DEFAULT_MAX_SUFFIX
        self.min_stem_length = stem_const.DEFAULT_MIN_STEM
        self.joker = stem_const.DEFAULT_JOKER
        self.prefix_list = stem_const.DEFAULT_PREFIX_LIST
        self.suffix_list = stem_const.DEFAULT_SUFFIX_LIST
        # root dictionary
        self.root_list = roots_const.ROOTS 
        # lists used to validate affixation
        #~ self.valid_affixes_list = []
        self.valid_affixes_list = set(list(affix_const.VERB_AFFIX_LIST) + list(affix_const.NOUN_AFFIX_LIST))
        self.word = u""
        self.unvocalized = u""
        self.normalized = u""
        self.starword = u""
        self.root = u""
        self.left = 0
        self.right = 0
        self.segment_list = []
        #token pattern
        # letters and harakat
        self.token_pat = re.compile(u"[^\w\u064b-\u0652']+", re.UNICODE)
        self.prefixes_tree = self._create_prefix_tree(self.prefix_list)
        self.suffixes_tree = self._create_suffix_tree(self.suffix_list)
    ######################################################################
    #{ Attribut Functions
    ######################################################################
    def get_prefix_letters(self, ):
        """ return the prefixation letters.
        This constant take DEFAULT_PREFIX_LETTERS by default.
        @return: return a letters.
        @rtype: unicode.
        """
        return self.prefix_letters

    def set_prefix_letters(self, new_prefix_letters):
        """ set the prefixation letters.
        This constant take DEFAULT_PREFIX_LETTERS by default.
        @param new_prefix_letters: letters to be striped from a word,
        e.g.new_prefix_letters = u"وف":.
        @type new_prefix_letters: unicode.
        """
        self.prefix_letters = new_prefix_letters

    def get_suffix_letters(self, ):
        """ return the suffixation letters.
        This constant take DEFAULT_SUFFIX_LETTERS by default.
        @return: return a letters.
        @rtype: unicode.
        """
        return self.suffix_letters

    def set_suffix_letters(self, new_suffix_letters):
        """ set the suffixation letters.
        This constant take DEFAULT_SUFFIX_LETTERS by default.
        @param new_suffix_letters: letters to be striped from the end of a word,
        e.g.new_suffix_letters = u"ةون":.
        @type new_suffix_letters: unicode.
        """
        self.suffix_letters = new_suffix_letters

    def get_infix_letters(self, ):
        """ get the inffixation letters.
        This constant take DEFAULT_INFIX_LETTERS by default.
        @return: infixes letters.
        @rtype: unicode.
        """
        return self.infix_letters

    def set_infix_letters(self, new_infix_letters):
        """ set the inffixation letters.
        This constant take DEFAULT_INFIX_LETTERS by default.
        @param new_infix_letters: letters to be striped from the middle
        of a word, e.g.new_infix_letters = u"أوي":.
        @type new_infix_letters: unicode.
        """
        self.infix_letters = new_infix_letters


    def get_joker(self, ):
        """ get the joker letter.
        This constant take DEFAULT_JOKER by default.
        @return: joker letter.
        @rtype: unicode.
        """
        return self.joker

    def set_joker(self, new_joker):
        """ set the joker letter.
        This constant take DEFAULT_JOKER by default.
        @param new_joker: joker letter.
        @type new_joker: unicode.
        """
        if len(new_joker) > 1:
            new_joker = new_joker[0]
        self.joker = new_joker

    def get_max_prefix_length(self, ):
        """ return the constant of max length of the prefix used by the stemmer.
        This constant take DEFAULT_MAX_PREFIX_LENGTH by default.
        @return: return a number.
        @rtype: integer.
        """
        return self.max_prefix_length

    def set_max_prefix_length(self, new_max_prefix_length):
        """ Set the constant of max length of the prefix used by the stemmer.
        This constant take DEFAULT_MAX_PREFIX_LENGTH by default.
        @param new_max_prefix_length: the new max prefix length constant.
        @type new_max_prefix_length: integer.
        """
        self.max_prefix_length = new_max_prefix_length

    def get_max_suffix_length(self, ):
        """ return the constant of max length of the suffix used by the stemmer.
        This constant take DEFAULT_MAX_SUFFIX_LENGTH by default.
        @return: return a number.
        @rtype: integer.
        """
        return self.max_suffix_length

    def set_max_suffix_length(self, new_max_suffix_length):
        """ Set the constant of max length of the suffix used by the stemmer.
        This constant take DEFAULT_MAX_SUFFIX_LENGTH by default.
        @param new_max_suffix_length: the new max suffix length constant.
        @type new_max_suffix_length: integer.
        """
        self.max_suffix_length = new_max_suffix_length

    def get_min_stem_length(self, ):
        """ return the constant of min length of the stem used by the stemmer.
        This constant take DEFAULT_MIN_STEM_LENGTH by default.
        @return: return a number.
        @rtype: integer.
        """
        return self.min_stem_length

    def set_min_stem_length(self, new_min_stem_length):
        """ Set the constant of min length of the stem used by the stemmer.
        This constant take DEFAULT_MIN_STEM_LENGTH by default.
        @param new_min_stem_length: the min stem length constant.
        @type new_min_stem_length: integer.
        """
        self.min_stem_length = new_min_stem_length

    def get_prefix_list(self, ):
        """ return the prefixes list used by the stemmer.
        This constant take DEFAULT_PREFIX_LIST by default.
        @return: prefixes list.
        @rtype: set().
        """
        return self.prefix_list
    def set_prefix_list(self, new_prefix_list):
        """ Set  prefixes list used by the stemmer.
        This constant take DEFAULT_PREFIX_LIST by default.
        @param new_prefix_list: a set of prefixes.
        @type new_prefix_list: set of unicode string.
        """
        self.prefix_list = new_prefix_list
        self._create_prefix_tree(self.prefix_list)

    def get_suffix_list(self, ):
        """ return the suffixes list used by the stemmer.
        This constant take DEFAULT_SUFFIX_LIST by default.
        @return: suffixes list.
        @rtype: set().
        """
        return self.suffix_list

    def set_suffix_list(self, new_suffix_list):
        """ Set  suffixes list used by the stemmer.
        This constant take DEFAULT_SUFFIX_LIST by default.
        @param new_suffix_list: a set of suffixes.
        @type new_suffix_list: set of unicode string.
        """
        self.suffix_list = new_suffix_list
        self._create_suffix_tree(self.suffix_list)
        
    def get_roots_list(self, ):
        """ return the roots list used by the stemmer to validate roots.
        This constant take roots_const.ROOTS by default.
        @return: roots list.
        @rtype: set().
        """
        return self.roots_list
    def set_roots_list(self, new_roots_list):
        """ Set  roots list used by the stemmer to validate roots..
        This constant take roots_const.ROOTS by default.
        @param new_roots_list: a set of roots.
        @type new_roots_list: set of unicode string.
        """
        self.roots_list = new_roots_list
    def get_valid_affixes_list(self, ):
        """ return the valid_affixes list used by the stemmer to validate affixes.
        This constant take valid_affixes_const.ROOTS by default.
        @return: valid_affixes list.
        @rtype: set().
        """
        return self.valid_affixes_list
    def set_valid_affixes_list(self, new_valid_affixes_list):
        """ Set  valid_affixes list used by the stemmer to validate affixes..
        This constant take valid_affixes_const.ROOTS by default.
        @param new_valid_affixes_list: a set of valid_affixes.
        @type new_valid_affixes_list: set of unicode string.
        """
        self.valid_affixes_list = new_valid_affixes_list
    def set_word(self, new_word):
        """ Set the word to treat by the stemmer.
        @param new_word: the new word.
        @type new_word: unicode.
        """
        self.word = new_word

    def get_word(self):
        """ return the last word treated by the stemmer.
        @return: word.
        @rtype: unicode.
        """
        return self.word
    #########################################################
    #{ Calculated Attribut Functions
    #########################################################

    def get_starword(self):
        """ return the starlike word treated by the stemmer.
        All non affix letters are converted to a joker.
        The joker take by default DEFAULT_JOKER = "*".

        Exmaple:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتصربونني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_starword()
            أفت***ونني

        @return: word.
        @rtype: unicode.
        """
        return self.starword

    def get_root(self, prefix_index=-1, suffix_index=-1):
        """ return the root of the treated word by the stemmer.
        All non affix letters are converted to a joker.
        All letters in the joker places are part of root.
        The joker take by default DEFAULT_JOKER = "*".

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتصربونني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_starword()
            أفت***ونني
            >>> print ArListem.get_root()
            ضرب

        @param prefix_index: indicate the left stemming position
        if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
        if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return: root.
        @rtype: unicode.
        """
        # extract a root for a specific stem
        if prefix_index >= 0 or suffix_index >= 0:
            self.extract_root(prefix_index, suffix_index)
        else:
            self.root = self._choose_root()
        return self.root

    def _choose_root(self,):
        """ choose a root for the given word """
        if arabicstopwords.is_stop(self.word):
            return arabicstopwords.stop_root(self.word)
        
        if not self.segment_list:
            self.segment(self.word)
        affix_list = self.get_affix_list()
        roots = [d['root'] for d in affix_list]
        # filter by length
        roots_tmp = roots
        accepted = list(filter(self.is_root_length_valid, roots_tmp))
        if accepted: # avoid empty list
           roots_tmp = accepted
        # filter by dictionary
        accepted = list(filter(self.is_root, roots_tmp)        )
        if accepted: # avoid empty list
           roots_tmp = accepted
        # choose the most frequent root
        accepted_root = self.most_common(roots_tmp)
        
        return accepted_root
        
    def _choose_stem(self,):
        """ choose a stem for the given word """
        # if word is stop word
        if arabicstopwords.is_stop(self.word):
            return arabicstopwords.stop_stem(self.word)
        
        if not self.segment_list:
            self.segment(self.word)
        seg_list = self.segment_list
        # verify affix against an affix list
        seg_list = [(x,y) for (x,y) in seg_list if self._verify_affix(x,y)]
        
        # choose the shortest stem
        if not seg_list: # if empty
            left = 0
            right = len(self.word)
        else:
            left, right = self.get_left_right(seg_list)
        
        return self.unvocalized[left:right]
        
      
    def get_normalized(self):
        """ return the normalized form of the treated word by the stemmer.
        Some letters are converted into normal form like Hamzat.

        Example:
            >>> word = u"استؤجرُ"
            >>> ArListem = ArabicLightStemmer()
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_normalized()
            استءجر

        @return: normalized word.
        @rtype: unicode.
        """
        return self.normalized

    def get_unvocalized(self):
        """ return the unvocalized form of the treated word by the stemmer.
        Harakat are striped.

        Example:
            >>> word = u"الْعَرَبِيّةُ"
            >>> ArListem = ArabicLightStemmer()
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_unvocalized()
            العربية

        @return: unvocalized word.
        @rtype: unicode.
        """
        return self.unvocalized

    def get_left(self):
        """ return the the left position of stemming
        (prefixe end position )in the word treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتصربونني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_starword()
            أفت***ونني
            >>> print ArListem.get_left()
            3

        @return: the left position of stemming.
        @rtype: integer.
        """
        return self.left

    def get_right(self):
        """ return the the right position of stemming
        (suffixe start position )in the word treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتصربونني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_starword()
            أفت***ونني
            >>> print ArListem.get_right()
            6

        @return: the right position of stemming.
        @rtype: integer.
        """

        return self.right

    def get_stem(self, prefix_index=-1, suffix_index=-1):
        """ return the stem of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتكاتبانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_stem()
            كاتب

        @param prefix_index: indicate the left stemming position
        if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
        if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return: stem.
        @rtype: unicode.
        """
        #~ # ask for default stem
        #~ if prefix_index < 0 and suffix_index < 0:
            #~ return self._choose_stem()
        if prefix_index >= 0 or suffix_index >= 0:
            if prefix_index < 0:
                left = self.stem_left
                #~ left = self.left
            else:
                left = prefix_index
            if suffix_index < 0:
                right = self.stem_right
                #~ right = self.right
            else:
                right = suffix_index
            return self.unvocalized[left:right]
        else:
            stem = self._choose_stem()
        return stem           

    def _handle_teh_infix(self, starword, left, right):
        """
        Handle case of Teh as infix.
        The Teh can be Dal after Zain, and Tah after Dhad
        """
        newstarstem = starword
        # case of Teh marbuta
        key_stem = newstarstem.replace(araby.TEH_MARBUTA,'')
        if len(key_stem) != 4:
            # apply teh and variants only one stem has 4 letters
            newstarstem = re.sub(u"[%s%s%s]"%(araby.TEH, araby.TAH, araby.DAL), self.joker, newstarstem)
            return newstarstem
        # substitube teh in infixes the teh mst be in the first
        # or second place, all others, are converted
        newstarstem = newstarstem[:2]+re.sub(araby.TEH, self.joker, newstarstem[2:])
        # Tah طاء is infix if it's preceded by DHAD only
        if self.word[left:right].startswith(u"ضط"):
            newstarstem = newstarstem[:2]+re.sub(araby.TAH, self.joker, newstarstem[2:])
        else:
            newstarstem = re.sub(araby.TAH, self.joker, newstarstem)
        # DAL دال  is infix if it's preceded by زاي only
        if  self.word[left:right].startswith(u"زد"):
            newstarstem = newstarstem[:2]+re.sub(araby.DAL, self.joker, newstarstem[2:])
        else:
            newstarstem = re.sub(araby.DAL, self.joker, newstarstem)
        return newstarstem
        
    def get_starstem(self, prefix_index=-1, suffix_index=-1):
        """ return the star form stem of the treated word by the stemmer.
        All non affix letters are converted to a joker.
        The joker take by default DEFAULT_JOKER = "*".

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتكاتبانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_stem()
            كاتب
            >>> print ArListem.get_starstem()
            *ات*

        @param prefix_index: indicate the left stemming position
        if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
        if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return: stared form of stem.
        @rtype: unicode.
        """
        #~ starword = self.starword
        starword = self.word
        if prefix_index < 0 and suffix_index < 0:
            return starword[self.left:self.right]
        else:
            left = self.left
            right = self.right
            if prefix_index >= 0:
                left = prefix_index
            if suffix_index >= 0:
                right = suffix_index
            if self.infix_letters != "":
                newstarstem = re.sub(u"[^%s%s]"%(self.infix_letters, araby.TEH_MARBUTA), \
                   self.joker, starword[left:right])
                # substitube teh in infixes the teh mst be in the first
                # or second place, all others, are converted
                newstarstem = self._handle_teh_infix(newstarstem, left, right)
            else:
                newstarstem = self.joker*len(starword[left:right])
            #~ print("star word", starword, newstarstem)
            return newstarstem

    def get_prefix(self, prefix_index=-1):
        """ return the prefix of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتكاتبانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_prefix()
            أفت

        @param prefix_index: indicate the left stemming position
        if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @return:  prefixe.
        @rtype: unicode.
        """
        if prefix_index < 0:
            return self.unvocalized[:self.left]
        else:
            return self.unvocalized[:prefix_index]


    def get_suffix(self, suffix_index=-1):
        """ return the suffix of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتكاتبانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_suffix()
            انني

        @param suffix_index:indicate the right stemming position.
        if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return:  suffixe.
        @rtype: unicode.
        """
        if suffix_index < 0:
            return self.unvocalized[self.right:]
        else:
            return self.unvocalized[suffix_index:]

    def get_affix(self, prefix_index=-1, suffix_index=-1):
        """ return the affix of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتكاتبانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_affix()
            أفت-انني

        @param prefix_index: indicate the left stemming position
            if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
            if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: in4teger.
        @return:  suffixe.
        @rtype: unicode.
        """
        return u"-".join([self.get_prefix(prefix_index), \
        self.get_suffix(suffix_index)])

    def get_affix_tuple(self, prefix_index=-1, suffix_index=0):
        """ return the affix tuple of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتضاربانني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_affix_tuple()
            {'prefix': u'أفت', 'root': u'ضرب', 'suffix': u'انني', 'stem': u'ضارب'}

        @param prefix_index: indicate the left stemming position
            if = -1: not cosidered, and take the default word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
            if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return: affix tuple.
        @rtype: dict.
        """
        return {
            'prefix':self.get_prefix(prefix_index),
            'suffix':self.get_suffix(suffix_index),
            'stem':self.get_stem(prefix_index, suffix_index),
            'starstem':self.get_starstem(prefix_index, suffix_index),
            'root':self.get_root(prefix_index, suffix_index),
        }
    #########################################################
    #{ Stemming Functions
    #########################################################
    def light_stem(self, word):
        u"""
        Stemming function, stem an arabic word, and return a stem.
        This function store in the instance the stemming positions
        (left, right), then it's possible to get other calculted
        attributs like: stem, prefixe, suffixe, root.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتضاربانني'
            >>> stem = ArListem.light_stem(word)
            >>> print ArListem.get_stem()
            ضارب
            >>> print ArListem.get_starstem()
            *ا**
            >>> print ArListem.get_left()
            3
            >>> print ArListem.get_right()
            6
            >>> print ArListem.get_root()
            ضرب

        @param word: the input word.
        @type word: unicode.
        @return: stem.
        @rtype: unicode.
        """
        if word == u'':
            return u''
        #~ starword, left, right = self.transform2stars(word)
        self.transform2stars(word)
        # segment
        self.segment(word)
        #constitute the root
        #~ self.extract_root()
        return self.get_stem()

    def transform2stars(self, word):
        """
        Transform all non affixation letters into a star.
        the star is a joker(by default '*').
        which indicates that the correspandent letter is an original.
        this function is used by the stmmer to identify original letters.
        and return a stared form and stemming positions (left, right)

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتضاربانني'
            >>> starword, left, right = ArListem.transformToStrars(word)
            (أفت*ا**انني, 3, 6)

        @param word: the input word.
        @type word: unicode
        @return: (starword, left, right):
            - starword: all original letters converted into a star
            - left: the greater possible left stemming position.
            - right: the greater possible right stemming position.
        @rtype: tuple.
        """
        self.word = word
        word = araby.strip_tashkeel(word)
        # word, harakat = araby.separate(word)
        self.unvocalized = word
        word = re.sub(u"[%s]"%(araby.ALEF_MADDA), araby.HAMZA+araby.ALEF, word)
        #~ word = re.sub(u"[^%s%s%s]"%(self.prefix_letters, self.suffix_letters, self.infix_letters), \
        word = re.sub(u"[^%s%s]"%(self.prefix_letters, self.suffix_letters), \
         self.joker, word)
        #~ ln = len(word)
        left = word.find(self.joker)
        right = word.rfind(self.joker)
        if left >= 0:
            left = min(left, self.max_prefix_length-1)
            right = max(right+1, len(word)-self.max_suffix_length)
            prefix = word[:left]
            #stem get the original word and make all letters as jokers except infixes
            stem = self.word[left:right]
            suffix = word[right:]
            prefix = re.sub(u"[^%s]"%self.prefix_letters, self.joker, prefix)
            # avoid null infixes
            if self.infix_letters:
                stem = re.sub(u"[^%s]"%self.infix_letters, self.joker, stem)
            suffix = re.sub(u"[^%s]"%self.suffix_letters, self.joker, suffix)
            word = prefix+stem+suffix

        left = word.find(self.joker)
        right = word.rfind(self.joker)
        # prefix_list = self.PREFIX_LIST
        # suffix_list = self.SUFFIX_LIST

        if left < 0:
            left = min(self.max_prefix_length, len(word)-2)
        if left >= 0:
            prefix = word[:left]
            while prefix != "" and prefix not in self.prefix_list:
                prefix = prefix[:-1]
            if right < 0:
                right = max(len(prefix), len(word)-self.max_suffix_length)
            suffix = word[right:]

            while suffix and suffix not in self.suffix_list:
                suffix = suffix[1:]
            left = len(prefix)
            right = len(word)-len(suffix)
            #stem get the original word and make all letters as jokers except infixes
            stem = self.word[left:right]
            # convert stem into  stars.
            # a stem must starts with alef, or end with alef.
            # any other infixes letter isnt infixe at
            #the border of the stem.
            #substitute all non infixes letters
            if self.infix_letters:
                stem = re.sub(u"[^%s]"%self.infix_letters, self.joker, stem)
            word = prefix+stem+suffix
        # store result
        self.stem_left = left
        self.stem_right = right
        self.starword = word
        #~ self.extract_root()
        # return starword, left, right position of stem
        return (word, left, right)

    def extract_root(self, prefix_index=-1, suffix_index=-1):
        """ return the root of the treated word by the stemmer.
        All non affix letters are converted to a joker.
        All letters in the joker places are part of root.
        The joker take by default DEFAULT_JOKER = "*".

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'أفتصربونني'
            >>> stem = ArListem .light_stem(word)
            >>> print ArListem.get_starword()
            أفت***ونني
            >>> print ArListem.get_root()
            ضرب

        @param prefix_index: indicate the left stemming position
            if = -1: not cosidered, and take the default
            word prefix lentgh.
        @type prefix_index:integer.
        @param suffix_index:indicate the right stemming position.
            if = -1: not cosidered, and take the default word suffix position.
        @type suffix_index: integer.
        @return: root.
        @rtype: unicode.
        """
        stem = self.get_stem(prefix_index, suffix_index)
        root = u""
        # if the stem has 3 letters it can be the root directly
        if len(stem) == 3:
            self.root = self._ajust_root(root, stem)
            return self.root
        starstem = self.get_starstem(prefix_index, suffix_index)
        root = u""
        if len(starstem) == len(stem):
            for i, char in enumerate(stem):
                if starstem[i] == self.joker:
                    root += char
        else:
            root = stem
        # normalize root
        root = self.normalize_root(root)
        #controls on root letters and length
        #~ if not self.is_root_length_valid(root):
            #~ root = ""
        if len(root) == 2:
            root = self._ajust_root(root, starstem)
        self.root = root
        return root

    def _ajust_root(self, root, starstem):
        """
        If the root has only three or two letters, we complete it by another letter
        """
        if not starstem:
            return root
        if len(starstem) == 3:
            starstem = starstem.replace(araby.ALEF, araby.WAW)
            starstem = starstem.replace(araby.ALEF_MAKSURA, araby.YEH)
            return starstem
        # The starstem can starts with a joker (*) or a infix letter
        # add a letter at the begining
        first = starstem[0]
        last = starstem[-1:]
        if first in (araby.ALEF, araby.WAW):
            root = araby.WAW + root
        elif first == araby.YEH:
            root = araby.YEH + root
        elif first == self.joker and last in (araby.ALEF, araby.WAW):
            root += araby.WAW
        elif first == self.joker and last in (araby.ALEF_MAKSURA, araby.YEH):
            root += araby.WAW
        elif first == self.joker and last == self.joker:
            # if lenght == 2, is doubled verb
            if len(starstem) == 2:
                root += root[-1]
            else:
                # I choose WAW because it's frequent
                root = root[0]+ araby.WAW+ root[1]
        return root
        
        
    def _create_prefix_tree(self, prefixes):
        """
        Create a prefixes tree from given prefixes list
        @param prefixes: list of prefixes
        @type prefixes: list of unicode
        @return: prefixes tree
        @rtype: Tree stucture
        """
        prefixestree = {}
        for prefix in prefixes:
            # print prefix.encode('utf8')
            branch = prefixestree
            for char in prefix:
                if char not in branch:
                    branch[char] = {}
                branch = branch[char]
            # branch['#'] = '#' # the hash # as an end postion
            if '#' in branch:
                branch['#'][prefix] = "#"
            else:
                branch['#'] = {prefix:"#", }
        self.prefixes_tree = prefixestree
        return self.prefixes_tree
    def _create_suffix_tree(self, suffixes):
        """
        Create a suffixes tree from given suffixes list
        @param suffixes: list of suffixes
        @type suffixes: list of unicode
        @return: suffixes tree
        @rtype: Tree stucture
        """
        suffixestree = {}
        for suffix in suffixes:
            # print (u"'%s'"%suffix).encode('utf8')
            branch = suffixestree
            #reverse a string
            for char in suffix[::-1]:
                if char not in branch:
                    branch[char] = {}
                branch = branch[char]
            # branch['#'] = '#' # the hash # as an end postion
            if "#" in branch:
                branch['#'][suffix] = "#"
            else:
                branch['#'] = {suffix:"#", }
        self.suffixes_tree = suffixestree
        return self.suffixes_tree

    def lookup_prefixes(self, word):
        """
        lookup for prefixes in the word
        @param word: the given word
        @type word: unicode
        @return: list of prefixes starts positions
        @rtype: list of int
        """
        branch = self.prefixes_tree
        lefts = [0, ]
        i = 0
        while i < len(word) and word[i] in branch:
            if "#" in branch:
                # if branch['#'].has_key(word[:i]):
                lefts.append(i)
            if word[i] in branch:
                branch = branch[word[i]]
            else:
                # i += 1
                break
            i += 1
        if i < len(word) and "#" in branch:
            lefts.append(i)
        return lefts


    def lookup_suffixes(self, word):
        """
        lookup for suffixes in the word
        @param word: the given word
        @type word: unicode
        @return: list of suffixes starts positions
        @rtype: list of int
        """
        branch = self.suffixes_tree
        suffix = ''
        # rights = [len(word)-1, ]
        rights = []
        i = len(word)-1
        while i >= 0 and word[i] in branch:
            suffix = word[i]+suffix
            if '#' in branch:
                # if branch['#'].has_key(word[i:]):
                    # rights.append(i)
                rights.append(i+1)
            if word[i] in branch:
                branch = branch[word[i]]
            else:
                # i -= 1
                break
            i -= 1
        if i >= 0 and "#" in branch:#and branch['#'].has_key(word[i+1:]):
            rights.append(i+1)
        return rights
    #########################################################
    #{ Segmentation Functions
    #########################################################

    def segment(self, word):
        """ generate  a list of  all possible segmentation positions
        (lef, right)  of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'فتضربين'
            >>> print ArListem.segment(word)
            set(([(1, 5), (2, 5), (0, 7)])

        @return: List of segmentation
        @rtype: set of tuple of integer.
        """
        self.word = word
        self.unvocalized = araby.strip_tashkeel(word)
        # word, harakat = araby.separate(word)
        word = re.sub(u"[%s]"%(araby.ALEF_MADDA), araby.HAMZA+araby.ALEF, word)

        # get all lefts position of prefixes
        lefts = self.lookup_prefixes(word)
        # get all rights position of suffixes
        rights = self.lookup_suffixes(word)
        if lefts:
            self.left = max(lefts)
        else:
            self.left = -1
        if rights:
            self.right = min(rights)
        else:
            self.right = -1
        #~ ln = len(word)
        self.segment_list = set([(0, len(word))])
        # print lefts, rights
        for i in lefts:
            for j in rights:
                if j >= i+2 :
                    self.segment_list.add((i, j))
        # filter segment according to valid affixes list
        
        self.left, self.right = self.get_left_right(self.segment_list)
        return self.segment_list


    # #########################################################
    # #{ Segmentation Functions
    # #########################################################
    def get_segment_list(self):
        """ return   a list of segmentation positions (left, right)
        of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'فتضربين'
            >>> ArListem.segment(word)
            >>> print ArListem.get_segment_list()
            set(([(1, 5), (2, 5), (0, 7)])

        @return: List of segmentation
        @rtype: set of tuple of integer.
        """
        return self.segment_list


    def get_affix_list(self, seg_list=[]):
        u""" return   a list of affix tuple of the treated word by the stemmer.

        Example:
            >>> ArListem = ArabicLightStemmer()
            >>> word = u'فتضربين'
            >>> ArListem.segment(word)
            >>> print ArListem.get_affix_list()
            [{'prefix': u'ف', 'root': u'ضرب', 'suffix': u'\u064aن', 'stem': u'تضرب'},
            {'prefix': u'فت', 'root': u'ضرب', 'suffix': u'\u064aن', 'stem': u'ضرب'},
            {'prefix': u'', 'root': u'فضربن', 'suffix': u'', 'stem': u'فتضرب\u064aن'}]

        @return: List of Affixes tuple
        @rtype: list of dict.
        """
        if not seg_list:
            seg_list = self.segment_list
        affix_list = []
        for  left,right in seg_list:
            affix_list.append(self.get_affix_tuple(left, right))
        return affix_list
    def _valid_stem(self, stem, tag="noun", prefix=""):
        """ Test if the stem is accepted"""
        if not stem:
            return False
        # valid stems for verbs
        if tag == "verb":
            # verb has length <= 6
            if len(stem) > 6 or len(stem) < 2:
                return False
            # forbidden letters in verbs like Teh Marbuta
            elif araby.TEH_MARBUTA in stem:
                return False
            # 6 letters stem must starts with ALEF
            elif len(stem) == 6 and not stem.startswith(araby.ALEF):
                return False
            # 5 letters stem must starts with ALEF/TEH or SEEN (a 6 letters verbs striped from Alef)
            # قد يكون الجذع الخماسي فعلا خماسيا
            # لذا يجب أن يبدأ  بالتاء أو الألف
            # أما إذا كن منقلبنا عن فعل سداسي، 
            # مثل استغفر، افرنقع، 
            # فيجب أن يكون مسبوقا بحرف يحذف ألف الوصل
            elif len(stem) == 5 and not stem[0] in (araby.ALEF, araby.TEH):
                if prefix[-1:] in (araby.YEH, araby.TEH, araby.NOON, araby.ALEF_HAMZA_ABOVE):
                    return False
            # لا يقبل ألف بعد حرف مضارعة
            elif stem.startswith(araby.ALEF) and  prefix[-1:] in (araby.YEH, araby.NOON, araby.TEH, araby.ALEF_HAMZA_ABOVE, araby.ALEF):
                return False
            ## lookup for stamp
            if  not verb_stamp_const.is_verb_stamp(stem):
                return False
        elif tag == "noun":
            if len(stem) >= 8 :
                return False
            return True
        return True

                
    def _verify_affix(self, prefix_index=-1, suffix_index=-1):
        """
        validate affixes against a list of valid affixes
        """
        prefix = self.get_prefix(prefix_index)
        suffix = self.get_suffix(suffix_index)

        TAG = True
        if TAG:
            affix = prefix+'-'+suffix            
            stem   = self.get_stem(prefix_index, suffix_index)
            if affix in affix_const.VERB_AFFIX_LIST and self._valid_stem(stem,"verb", prefix):
                # is a valid verb stem
                if affix in affix_const.NOUN_AFFIX_LIST and self._valid_stem(stem,"noun"):                      
                # is also a noun stem
                    return True # TAG VN
                else:
                    return True # TAG V
            else:
                if affix in affix_const.NOUN_AFFIX_LIST and self._valid_stem(stem,"noun"):
                    return True # TAG N
                else:
                    return False # not a valid verb or not a noun
        return True
        
        if self.valid_affixes_list :
            affix = prefix+'-'+suffix
            return affix in self.valid_affixes_list
        else:
            #مراجعة مبسطة
            # أل التعريف مع ضمير متصل
            if ((u"ال" in prefix or u"لل" in prefix) and 
                (u'ه' in suffix or u'ك' in suffix)
                ):
                return False
            # التاء المربوطة مع حروف المضارعة

            if ((u"ي" in prefix or u"يس" in prefix or u"نس" in prefix 
            or u"تس" in prefix or u"سي" in prefix or u"سأ" in prefix) and 
                (u'ة' in suffix)
                ):
                return False
            # التاء المتحركة مع حروف المضارعة

            if ((u"ي" in prefix or u"يس" in prefix or u"نس" in prefix 
            or u"تس" in prefix or u"سي" in prefix or u"سأ" in prefix) and 
                (u'تم' in suffix or u'تن' in suffix )
                ):
                return False
            # حروف الجر مع واو جمع مذكر سالم
            #ولمثنى المرفوع
            if ((u"ك" in prefix or u"ب" in prefix or u"لل" in prefix) and 
                (u'و' in suffix or u'ان' in suffix)
                ):
                return False
        return True
    ###############################################################
    #{ General Functions
    ###############################################################

    def normalize(self, word=u""):
        """
        Normalize a word.
        Convert some leters forms into unified form.
        @param word: the input word, if word is empty,
        the word member of the class is normalized.
        @type word: unicode.
        @return: normalized word.
        @rtype: unicode.
        """

        if word == u'' and self.word == u"":
            return u""
        elif word != u'':
            self.word = word
        else:
            word = self.word
        self.normalized = normalize.normalize_searchtext(word)
        return self.normalized

    def tokenize(self, text=u""):
        """
        Tokenize text into words
        @param text: the input text.
        @type text: unicode.
        @return: list of words.
        @rtype: list.
        """
        if not text:
            return []
        else:
            mylist = self.token_pat.split(text)
            if u'' in mylist:
                mylist.remove(u'')
            return mylist

    @staticmethod
    def normalize_root(word):
        """ test if word is a root"""
        # change alef madda to hamza + ALEF
        word = word.replace(araby.ALEF_MADDA, araby.HAMZA+ araby.ALEF)
        word = word.replace(araby.TEH_MARBUTA, '')
        word = word.replace(araby.ALEF_MAKSURA, araby.YEH)
        return araby.normalize_hamza(word)

    @staticmethod
    def is_root_length_valid(root):
        
        return (len(root) >= 2 and len(root)<=4)
    
    @staticmethod
    def most_common(lst):
        triroots = [x for x in lst if len(x) == 3]
        if triroots:
            lst = triroots
        return max(set(lst), key=lst.count)

    def is_root(self, word):
        """ test if word is a root"""
        return word in self.root_list
    @staticmethod
    def get_left_right(ls):
        """
        get the max left and the min right
        """
        if not ls:
            return -1,-1
        l,_= max(ls)
        r = min([y for (x,y) in ls if x==l])
        return l, r


if __name__ == "__main__":
    #~ from pyarabic.arabrepr import arepr as repr
    ARLISTEM = ArabicLightStemmer()
    wordlist =[u'أفتضاربانني',
    u'بالمكتبة',
    u'مزدهرة', 
    u'كاتب', 
    u'مضروب',
    u'مضارب',
    u"مردود",
    u"مطلوب",
    u"مشتت",
        u'مزتهرة',
    u'مضطرب',
    u'بالمكتبة',
    u'مالبدرسمه',
    u"مكتوب", 
    u"الآجال", 
    u"بالبلدان", 
    u"وفيهما", 
    u"1245", 
    u"Taha", 
    u"@", 
    ]
    for word in wordlist:
        # stemming word
        ARLISTEM.light_stem(word)
        # extract stem
        print("stem", ARLISTEM.get_stem())
        print(ARLISTEM.infix_letters)
        # extract root
        print("root:", ARLISTEM.get_root())

        # get prefix position index
        print("left",ARLISTEM.get_left())
        print("left stem",ARLISTEM.stem_left)
        # get prefix
        print(ARLISTEM.get_prefix())
        # get prefix with a specific index
        print(ARLISTEM.get_prefix(2))

        # get suffix position index
        print("right",ARLISTEM.get_right())
        print("right_stem",ARLISTEM.stem_right)
        # get suffix
        print("suffix", ARLISTEM.get_suffix())
        # get suffix with a specific index
        print(ARLISTEM.get_suffix(10))
        # get affix tuple
        print(ARLISTEM.get_affix_tuple())


        # star words
        print("starword", ARLISTEM.get_starword())
        # get star stem
        print("starstem",ARLISTEM.get_starstem())

        #  get normalized word
        print("normalize", ARLISTEM.get_normalized())
        #  get unvocalized word
        print("unvocalized",ARLISTEM.get_unvocalized())

        # Detect all possible segmentation
        print(ARLISTEM.segment(word))
        print(ARLISTEM.get_segment_list())
        # get affix list
        print(repr(ARLISTEM.get_affix_list()))



