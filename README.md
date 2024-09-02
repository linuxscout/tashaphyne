# Tashaphyne
![downloads](https://img.shields.io/pypi/dm/tashaphyne?style=plastic)


**Tashaphyne**: Arabic Light Stemmer تاشفين: التجذيع الخفيف للنصوص العربية

[تاشفين](https://github.com/linuxscout/tashaphyne) برنامج تجذيع عربي خفيف ومقطع للكلمات. يدعم بشكل أساسي التجذيع الخفيف (إزالة السوابق واللواحق) ويعطي الجذوع  الممكنة. يستخدم ألة ذات وضعيات محدودة معدّلة، مما يسمح له باستخلاص كل الجذوع الممكنة.

يوفر تاشفين استخلاص الجذع والجذر من الكلمة في نفس الوقت، على عكس برامج التجذيع مثل Khoja وISRI وAssem وFarasa.

**تاشفين** يأتي بقائمة افتراضية للسوابق واللواحق، ويقبل استخدام قوائم مخصصة للزوائد، مما يسمح له بالتعامل مع المزيد من الجوانب الصرفية، وإنشاء زوائد مخصصة دون تغيير الكود.

**تاشفين** هي مكتبة بايثون، وهي متاحة للتجربة في برنامج مشكال على [Mishkal](http://tahadz.com/mishkal)، اختر أدوات/تحليل والمصدر مفتوح على [Github](http://github.com/linuxscout/tashaphyne)
**Tashaphyne** is an Arabic light stemmer and segmentor. It mainly supports light stemming (removing prefixes and suffixes) and gives all possible segmentations. It uses a modified finite state automaton, which allows it to generate all segmentations.

It offers stemming and root extraction at the same time, unlike the Khoja stemmer, ISRI stemmer, Assem stemmer, and Farasa stemmer.

**Tashaphyne** comes with default prefixes and suffixes, and accepts the use of customized prefixes and suffixes lists, which allow it to handle more aspects and make customized stemmers without changing code.

**Tashaphyne** is a python library, it's available as a demo on  [Mishkal](http://tahadz.com/mishkal), choose Tools/Analysis and as source code on [Github](http://github.com/linuxscout/tashaphyne) 

  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

---------|---------------------------------------------------------------------------------
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/tashaphyne/master/AUTHORS.md)
Release  | 0.3.7 
License  |[GPL](https://github.com/linuxscout/tashaphyne/master/LICENSE)
Tracker  |[linuxscout/tashaphyne/Issues](https://github.com/linuxscout/tashaphyne/issues)
Website  |[https://pypi.python.org/pypi/Tashaphyne](https://pypi.python.org/pypi/Tashaphyne)
Doc      |[package Documentaion](https://tashaphyne.readthedocs.io/)
Source  |[Github](http://github.com/linuxscout/tashaphyne)
Download  |[sourceforge](http://tashaphyne.sourceforge.net)
Feedbacks  |[Comments](http://tahadz.com/contact.html)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/tashaphyne/)



## Citation
If you would cite it in academic work, can you use this citation

* T. Zerrouki‏, **Tashaphyne, Arabic light stemmer**‏,  https://pypi.python.org/pypi/Tashaphyne/0.2
* Zerrouki, T. (2024). **Tashaphyne: A python package for arabic light stemming**. Journal of Open Source
Software, 9(93), 6063.  doi: http://doi.org/10.21105/joss.06063
*  Alkhatib, R. M., Zerrouki, T., Shquier, M. M. A., & Balla, A. (2023). **Tashaphyne0.4: A new arabic light
stemmer based on rhyzome modeling approach**. Information Retrieval Journa, 26(14). doi: https://doi.org/10.1007/s10791-023-09429-y
* Alkhatib, R. M., Zerrouki, T., Shquier, M. M. A., Balla, A., & Al-Khateeb, A. (2021). **A new enhanced arabic light stemmer for ir in medical documents**. CMC-COMPUTERS MATERIALS & CONTINUA, 68(1), 1255–1269. 

or in bibtex format
```bibtex
@misc{zerrouki2012tashaphyne,
title={Tashaphyne, Arabic light stemmer},
author={Zerrouki, Taha},
url={https://pypi.python.org/pypi/Tashaphyne/0.2},
year={2012}
}
```

** bibtex
```bibtex
@article{Zerrouki2024,
	title        = {Tashaphyne: A Python package for Arabic Light Stemming},
	author       = {Taha Zerrouki},
	year         = 2024,
	journal      = {Journal of Open Source Software},
	publisher    = {The Open Journal},
	volume       = 9,
	number       = 93,
	pages        = 6063,
	doi          = {10.21105/joss.06063},
	url          = {https://doi.org/10.21105/joss.06063}
}
```

```bibtex
@article{raed20223,
  title={Tashaphyne0.4: a new arabic light stemmer based  on rhyzome modeling approach},
  author={Alkhatib, Read M and Zerrouki, Taha and Shquier, Mohammed M Abu and Balla, Amar},
  journal={Information Retrieval Journa},
  year={2023},
  pages={},
  volume={26},
  number={14}, 
  doi={https://doi.org/10.1007/s10791-023-09429-y}
}

@article{raed2021,
  title={A New Enhanced Arabic Light Stemmer for IR in Medical Documents},
  author={Alkhatib, Read M and Zerrouki, Taha and Shquier, Mohammed M Abu and Balla, Amar and Al-Khateeb, Asef},
  journal={CMC-COMPUTERS MATERIALS \& CONTINUA},
  year={2021},
  pages={1255-1269},
  volume={68},
  number={1}
}
```


##   مزايا
 - تجذيع الكلمة العربية إلى أبسط جذع ممكن
 - إمكانية استخراج الجذر
 - تقطيع الكلمة إلى جميع الحالات الممكنة.
 - تنميط الكلمة ( توحيد الحروف ذات الأشكال المختلفة.
 - قائمة مسبقة للزوائد العربية، وحروف الزيادة
 - إمكانية ضبط إعدادات المجذع والمقطع، من خلال تعديل قوائم الزوائد.
 
## Features
 - Arabic word Light Stemming.
 - Root Extraction.
 - Word Segmentation 
 - Word normalization
 - Default Arabic Affixes list.
 - An customizable Light stemmer: possibility of change stemmer options and data.
 - Data independent stemmer.


## Applications
* Stemming texts
* Text Classification and categorization
* Sentiment Analysis
* Named Entities Recognition

## Installation

```
pip install tashaphyne
```    
    
Usage
=====


Tahsphyne is a finite state automaton stem-based; it extracts affixes (prefixes and suffixes) from a predefined affix list.

It extracts all possible affixations from a word and cites all possible configurations stemming from a given word.



### Functions الدوال 


* تجذيع الكلمة

تجذيع الكلمة واستخلاص كل المعلومات منها بواسطة الدوال المناسبة

Stemming function: stem an Arabic word and return a stem. This function stores in the instance the stemming positions (left, right), and then it's possible to get other calculated attributes like stem, prefix, suffix, and root.

```python
>>> from tashaphyne.stemming import ArabicLightStemmer
>>> ArListem = ArabicLightStemmer()
>>> word = 'أفتضاربانني'
>>> # stemming word
... stem = ArListem.light_stem(word)
>>> # extract stem
... print(ArListem.get_stem())
ضارب
>>> # extract root
... print(ArListem.get_root())
ضرب
>>> 
>>> # get prefix position index
... print(ArListem.get_left())
3
>>> # get prefix 
... print(ArListem.get_prefix())
أفت
>>> # get prefix with a specific index
... print(ArListem.get_prefix(2))    
أف
>>> 
>>> # get suffix position index
... print(ArListem.get_right())
7
>>> # get suffix 
... print(ArListem.get_suffix())   
انني
>>> # get suffix with a specific index
... print(ArListem.get_suffix(10))    
ي
>>> # get affix
>>> print(ArListem.get_affix())
أفت-انني
>>> # get affix tuple
... print(ArListem.get_affix_tuple())
{'prefix': 'أفت', 'root': '', 'stem': '', 'suffix': 'أفتضاربانني'}
>>> # star words
... print(ArListem.get_starword())
أفت*ا**انني
>>> # get star stem
... print(ArListem.get_starstem())
*ا**
>>> 
>>> #  get unvocalized word
... print(ArListem.get_unvocalized())
أفتضاربانني
```

function | Description | وصف|
---------|-------------|----|
get_root()|Get the root of the treated word by the stemmer. |استخلاص الجذر|
get_stem()|Get the stem of the treated word by the stemmer.|استخلاص الجذع يمكن استخلاص الجذع التلقائي مباشرة، عند الرغبة في الحصول على جذع معين، نحدد دليل السابق، ودليل اللاحق.|
get_left()| Get the prefix end position | موضع نهاية السابقة|
get_right()|Get the suffix start position| موضع بداية اللاحقة |
get_prefix()|return the prefix/suffix of the treated word by the stemmer.|استرجاع السابقة التلقائية أو سابقة معينة بموضع|
get_suffix()| Get default suffix, or suffix by suffix index| استرجاع اللاحقة التلقائية أو بواسطة دليل اللاحقة
get_affix()|Get default Affix or specific by left and right indexes|استرجاع الزائدة التلقائية أو المعينة بدليلي السابق واللاحق|
get_affix_tuple()|Get affixe tuple | استرجاع الزائدة بتفاصيلها
get_starword()|Get starred word, radical letters replaced by "*"|استرجاع الكلمة المنجمة، الحروف الأصلية مخفية بنجوم
get_starstem()|Get starred stem, radical letters replaced by "*"|استرجاع الجذع المنجم، الحروف الأصلية مخفية بنجوم
get_unvocalized()|return the unvocalized form of the treated word by the stemmer. Harakat are striped.| استرجاع الكلمة غير مشكولة|


* استخلاص كل التقسيمات المحتملة
* تقسيم الكلمة إلى كل الزوائد المحتملة

Generate a list of all possible segmentation positions (left, right) of the treated word by the stemmer.

```python

>>> word = 'أفتضاربانني'

>>> # Detect all possible segmentation
... print(ArListem.segment(word))
set([(2, 7), (3, 8), (0, 8), (2, 9), (2, 8), (3, 10), (2, 11), (1, 8), (0, 7), (2, 10), (3, 11), (1, 10), (0, 11), (3, 9), (0, 10), (1, 7), (0, 9), (3, 7), (1, 11), (1, 9)])

>>># Get all segment 
>>>print(ArListem.get_segment_list())
set([(2, 7), (3, 8), (0, 8), (2, 9), (2, 8), (3, 10), (2, 11), (1, 8), (0, 7), (2, 10), (3, 11), (1, 10), (0, 11), (3, 9), (0, 10), (1, 7), (0, 9), (3, 7), (1, 11), (1, 9)])

>>> # get affix list
... print(ArListem.get_affix_list())
[{'prefix': 'أف', 'root': 'ضرب', 'stem': 'تضارب', 'suffix': 'انني'},
 {'prefix': 'أفت', 'root': 'ضرب', 'stem': 'ضاربا', 'suffix': 'نني'},
 {'prefix': '', 'root': 'أفضرب', 'stem': 'أفتضاربا', 'suffix': 'نني'}, 
 {'prefix': 'أف', 'root': 'ضربن', 'stem': 'تضاربان', 'suffix': 'ني'}, 
 {'prefix': 'أف', 'root': 'ضرب', 'stem': 'تضاربا', 'suffix': 'نني'}, 
 {'prefix': 'أفت', 'root': 'ضربنن', 'stem': 'ضاربانن', 'suffix': 'ي'}, ...]
>>> 
```
* segment() / get_segment_list()
استخلاص قائمة مواضع كل التقسيمات المحتملة على شكل أعداد
return a list of segmentation positions (left, right) of the treated word by the stemmer.

* get_affix_list

 استخلاص قائمة كل الزوائد المحتملة

return a list of affix tuple of the treated word by the stemmer.

### Customized Affix list
تخصيص قوائم الزوائد
يمكنن تخصيص قوائم السوابق واللواحق للحصول على نتائج افضل حسب السياق

في المثال الموالي، سنستعمل مجذع تاشفين حسب قوائمه التلقائية، ثم نصنع مجذعا آخر يعطي نتائج مختلفة بتخصيص قوائم السوابق واللواحق

You can modify and customize  the default affixes list by

```python
>>> import tashaphyne.stemming

>>> CUSTOM_PREFIX_LIST = [u'كال', 'أفبال', 'أفك', 'فك', 'أولل', '', 'أف', 'ول', 'أوال', 'ف', 'و', 'أو', 'ولل', 'فب', 'أول', 'ألل', 'لل', 'ب', 'وكال', 'أوب', 'بال', 'أكال', 'ال', 'أب', 'وب', 'أوبال', 'أ', 'وبال', 'أك', 'فكال', 'أوك', 'فلل', 'وك', 'ك', 'أل', 'فال', 'وال', 'أوكال', 'أفلل', 'أفل', 'فل', 'أال', 'أفكال', 'ل', 'أبال', 'أفال', 'أفب', 'فبال']
>>> CUSTOM_SUFFIX_LIST = [u'كما', 'ك', 'هن', 'ي', 'ها', '', 'ه', 'كم', 'كن', 'هم', 'هما', 'نا']

>>> # simple stemmer with default affixes list
... simple_stemmer = tashaphyne.stemming.ArabicLightStemmer()

>>> # create a cعstomized stemmer object for stemming enclitics and procletics
... custom_stemmer = tashaphyne.stemming.ArabicLightStemmer()
>>> # configure the stemmer object
... custom_stemmer.set_prefix_list(CUSTOM_PREFIX_LIST)
>>> custom_stemmer.set_suffix_list(CUSTOM_SUFFIX_LIST)
>>> 
>>> word = "بالمدرستين"
>>> # segment word as 
... simple_stemmer.segment(word)
set([(4, 10), (4, 7), (4, 9), (4, 8), (3, 10), (0, 7), (3, 8), (1, 10), (1, 8), (3, 9), (0, 10), (1, 7), (0, 9), (3, 7), (0, 8), (1, 9)])
>>> print(simple_stemmer.get_affix_list())
[{'prefix': 'بالم', 'root': 'درستين', 'stem': 'درستين', 'suffix': ''}, {'prefix': 'بالم', 'root': 'درس', 'stem': 'درس', 'suffix': 'تين'}, {'prefix': 'بالم', 'root': 'درستي', 'stem': 'درستي', 'suffix': 'ن'}, {'prefix': 'بالم', 'root': 'درست', 'stem': 'درست', 'suffix': 'ين'}, {'prefix': 'بال', 'root': 'مدرستين', 'stem': 'مدرستين', 'suffix': ''}, {'prefix': '', 'root': 'بالمدرس', 'stem': 'بالمدرس', 'suffix': 'تين'}, ...]
>>> 
>>> custom_stemmer.segment(word)
set([(1, 10), (3, 10), (0, 10)])
>>> 
>>> print(custom_stemmer.get_affix_list())
[{'prefix': 'ب', 'root': 'المدرستين', 'stem': 'المدرستين', 'suffix': ''}, {'prefix': 'بال', 'root': 'مدرستين', 'stem': 'مدرستين', 'suffix': ''}, {'prefix': '', 'root': 'بالمدرستين', 'stem': 'بالمدرستين', 'suffix': ''}]
>>> 

```

This command *set_prefix_list*  and  *set_suffix_list" will rebuild the Finite state automaton to consider new affixes list.

### Stemming a text

To stem all words in a text, we use tokenization preprocessing:
```
>>> import pyarabic.araby as araby
>>> from tashaphyne.stemming import ArabicLightStemmer
>>> stemmer  = ArabicLightStemmer()
>>> text = "الأطفال يستريحون في المكتبة للمطالعة"
>>> tokens = araby.tokenize(text)
>>> tokens
['الأطفال', 'يستريحون', 'في', 'المكتبة', 'للمطالعة']
>>> for tok in tokens:
...     stem = stemmer.light_stem(tok)
...     print(tok, stem)
... 
الأطفال أطفال
يستريحون يستريح
في في
المكتبة مكتب
للمطالعة مطالع
>>> 

```
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
