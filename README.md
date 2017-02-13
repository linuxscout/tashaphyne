# Tashaphyne
=======
Tashaphyne: Arabic Light Stemmer تاشفين: التجذيع الخفيف للنصوص العربية

[![downloads]( https://img.shields.io/pypi/dw/Tashaphyne.svg)](https://pypi.python.org/pypi/Tashaphyne)
[![downloads]( https://img.shields.io/pypi/dm/Tashaphyne.svg)](https://pypi.python.org/pypi/Tashaphyne)

  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com


Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/tashaphyne/master/AUTHORS.md)
Release  | 0.3 
License  |[GPL](https://github.com/linuxscout/tashaphyne/master/LICENSE)
Tracker  |[linuxscout/tashaphyne/Issues](https://github.com/linuxscout/tashaphyne/issues)
Website  |[https://pypi.python.org/pypi/Tashaphyne](https://pypi.python.org/pypi/Tashaphyne)
Doc  |[package Documentaion](http://pythonhosted.org/Tashaphyne/)
Source  |[Github](http://github.com/linuxscout/tashaphyne)
Download  |[sourceforge](http://tashaphyne.sourceforge.net)
Feedbacks  |[Comments](http://tahadz.com/tashaphyne/contact)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/tashaphyne/)


Usage
=====
```
pip install tashaphyne
```    
    
Usage
=====


Tahsphyne is a finite state automaton stemmed based, it extract affixes (prefixes and suffixes), with a predefined affixes list.

It extract all possible affixation from a word and cite all possible configuration stemming of a given word.

```python
%بالعربية 
%ب+ العربية
% بال+عربية
%بال+ عربي + ة
%بال + عرب+ية
```
```python
>>> ArListem=ArabicLightStemmer();
>>> word=u'فتضربين'>
>>> ArListem.segment(word);
>>> print ArListem.get_affix_list();
%[{'prefix': u'ف', 'root': u'ضرب', 'suffix': u'ين', 'stem': u'تضرب'}, 
%{'prefix': u'فت', 'root': u'ضرب', 'suffix': u'ين', 'stem': u'ضرب'}, 
%{'prefix': u'', 'root': u'فضربن', 'suffix': u'', 'stem': u'فتضربين'}]
```

The result is represented as a vector of segment

```python
>>> word=u'فتضربين'
>>> ArListem=ArabicLightStemmer();
>>> word=u'ftDrbin'
>>> ArListem.segment(word);
>>> print ArListem.get_segment_list();
set(([(1, 5), (2, 5), (0, 7)])
```


### Example 

To import Tashaphyne, we use
```python
>>>import tashaphyne.stemming 
```
Create an instance of stemmer class
```python
>>>mystemmer = ArabicLightStemmer() 
``` 

Give a word,
```python
>>> word=u'فتضربين'
>>> mystemmer.segment(word);
```

You can now get multiple informations extracted from the word:
 
Get all possible segmentation of a word
```python
>>> print ArListem.get_segment_list();
set(([(1, 5), (2, 5), (0, 7)])
```
You can now get multiple informations extracted from the word:

```python
>>> mystemmer.get_affix_list()
[{'prefix': u'ف', 'root': u'ضرب', 'suffix': u'ين', 'stem': u'تضرب'}, 
{'prefix': u'فت', 'root': u'ضرب', 'suffix': u'ين', 'stem': u'ضرب'}, 
{'prefix': u'', 'root': u'فضربن', 'suffix': u'', 'stem': u'فتضربين'}]
```
Or extract Root
```python
>>>mystemmer.get_root(); 
```

Or extract stemm
```python
>>>mystemmer.get_stem(); 
```

You can modify and customize  the default affixes list by

```python
>>>mystemmer.set_prefix_list(NEW_PREFIX_LIST); 
>>>mystemmer.set_suffix_list(NEW_SUFFIX_LIST); 
```
This command will rebuild the Finite state automaton to consider new affixes list.

Package Documentation
=====

Files
=====
* file/directory    category    description 

* [docs]
    docs/   docs    documentation

* [support]
    - pyarabic  : basic arabic library

* [test]
    - output/   test    test output
    - samples/  test    sample files
    - tools/    test    script to use tashaphyne


## Featured Posts
If you would cite it in academic work, can you use this citation
```
T. Zerrouki‏, Tashaphyne, Arabic light stemmer‏,  https://pypi.python.org/pypi/Tashaphyne/0.2
```
or in bibtex format
```bibtex
@misc{zerrouki2012tashaphyne,
  title={Tashaphyne, Arabic light stemmer},
  author={Zerrouki, Taha},
  url={https://pypi.python.org/pypi/Tashaphyne/0.2},
  year={2012}
}
```
