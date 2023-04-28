---
title: >-
    Tashaphyne: A Python package for Arabic Light Stemming
tags:
    Python
    Arabic Language
    Natural Language Processing
    Text Preprocessing
    Light Stemming
authors:
  - name: Taha Zerrouki
    email: t.zerrouki@univ-bouira.dz
    affiliation: "1"
    orcid: 0000-0001-9960-5533
    corresponding: true
affiliations:
  - name: Bouira University, Bouira, Algeria
    index: 1
date: 20 September 2022
bibliography: paper.bib
---
# Summary

Stemming is an important task in natural language processing that involves reducing a word to its root form, or stem. In many cases, stemming can significantly improve the accuracy and efficiency of text analysis tasks such as information retrieval, text classification, and sentiment analysis. For the Arabic language, which has a rich morphology with a large number of prefixes and suffixes, stemming is particularly challenging. Tashaphyne provides an effective solution to this challenge, making it a valuable tool for researchers and practitioners working with Arabic text data.

Tashaphyne is a Python package that provides a comprehensive light stemmer and segmentor for the Arabic language. It stands out among other stemmers for its ability to perform stemming and root extraction simultaneously, unlike the Khoja stemmer, ISRI stemmer, Assem stemmer, and Farasa stemmer. Tashaphyne uses a modified finite state automaton that generates all possible segmentations, making it an extremely flexible tool for customizing stemmers without changing the code. Furthermore, Tashaphyne comes with default prefixes and suffixes, and allows for the use of customized lists to handle more complex aspects of stemming.  Overall, Tashaphyne is an important contribution to the open-source community for Arabic language processing.

# Statement of need

The Arabic language has a complex morphology with a rich system of prefixes, suffixes, and infixes. As a result, stemming Arabic text is a challenging task that requires specialized tools. While there are several Arabic stemmers available, they often have limitations in terms of accuracy and flexibility. Tashaphyne addresses these limitations by providing a comprehensive light stemmer and segmentor that performs stemming and root extraction simultaneously, generating all possible segmentations. 

Tashaphyne is a light stemmer and segmentor in Arabic. It mostly supports light stemming (the removal of prefixes and suffixes) and provides all conceivable segmentations. Tahsphyne is a stem-based finite state automaton that extracts affixes (prefixes and suffixes) from a predefined list. It extracts and provides all possible affixations and configurations that result from a given word. Unlike the Khoja stemmer [@khoja1999stemming] ISRI stemmer [@taghva2005arabic], Assem stemmer [@assemstem2018], and Farasa stemmer [@darwish2016farasa], it can do both stemming and root extraction.

Tashaphyne also supports modifiable prefixes and suffixes, making it a highly adaptable tool for building customized stemmers without altering the code in any way.

Tashaphyne can be found at [PyPi.org index](https://pypi.org/project/tashaphyne/) \footnote{\url{https://pypi.org/project/tashaphyne/}}., it’s available as [demo on Mishkal](http://tahadz.com/mishkal), choose Tools/Analysis and as source code on [Github](http://github.com/linuxscout/tashaphyne).


Tashaphyne contains two important submodules: stemming and normalizing. Normalizing text is an important preprocessing step in natural language processing that involves transforming text data into a standardized format. Normalization of Arabic text involves several sub-tasks, including removing diacritics [@Zerrouki2023], normalizing characters, and removing ligatures. These sub-tasks are essential for improving the accuracy of downstream tasks such as text classification, named entity recognition, and sentiment analysis. Tashaphyne, with its ability to perform light stemming and segmenting, can also assist in normalizing Arabic text, further highlighting its importance in Arabic language processing


Tashaphyne has been developed within "Adawat", an open-source framework for processing Arabic texts developed as part of a PhD research project [@zerrouki2020towards:2020]. Adawat includes several tools, including Mishkal [@mishkal] for restoring Arabic text diacritics and Qalsadi [@qalsadi] for Arabic morphology analysis, both of which rely on Tashaphyne's functionalities.


Another framework that has incorporated Tashaphyne is the Classical Language Toolkit (CLTK \footnote{\url{http://cltk.org}} [@johnson2014:2014]), which provides natural language processing support for ancient, classical, and medieval Eurasian languages. CLTK uses Tashaphyne for several tasks, including corpus importer, tokenization, text conversion, and transliteration for classical Arabic [@johnson2014:2014]  (like the orthography of the Quran).

The SAFAR framework, a comprehensive toolkit for Arabic natural language processing, has also incorporated Tashaphyne as part of its stemmers. However, as SAFAR [@jaafar2015]  is written in Java, Tashaphyne was translated to the Java programming language to enable its integration into the framework.


Tashaphyne is a powerful Python package designed to facilitate natural language processing tasks, with a particular focus on Arabic text preprocessing. Its numerous features make it a valuable tool for researchers and developers alike. Tashaphyne provides support for light stemming of Arabic words, root extraction, and word segmentation. It also includes a default list of Arabic affixes and allows users to customize their own stemmer options and data. Furthermore, Tashaphyne supports data-independent stemming, making it highly versatile and adaptable to a wide range of use cases.

In terms of applications, Tashaphyne is ideal for stemming Arabic text, which is a crucial step in many natural language processing tasks. It is also useful for text classification and categorization, sentiment analysis, and named entity recognition. Tashaphyne has already been used in numerous scientific publications, demonstrating its reliability and effectiveness in a variety of real-world applications. With its comprehensive set of features and wide range of potential applications, Tashaphyne is an indispensable tool for anyone working with Arabic text data.

# Mention

Tashaphyne has been widely used as a tool in various natural language processing tasks by researchers. Stemming development and evaluation have been explored by [@atoumsentiment2019; @jaafar2017enhancing; @jaafar2015; @el2016rule; @dahab2015comparative; @el2015cbas]. Root extraction and evaluation were studied by [@el2015enhancing; @el2017efficient]. Tashaphyne has been utilized for text categorization [@sallam2016improving; @hussein2016arabic], classification [@gharbat2019discovering; @naji2017new; @el2016arabic; @alhaj2019study], topic segmentation [@naili2018contribution], and summarization [@al2019wajeez]. It has been applied to social media analysis [@almuqhim2016; @bulbul2018social; @kumar2013; @kumar2015social], sentiment analysis [@oussous2019impact; @oussous2020asa; @al2019improving; @alotaibi2016; @alotaibi2015sentiment; @al2014subjectivity; @oraby2013exploring; @shoukry2012preprocessing; @shoukry2013; @al2018comprehensive], and tweet classification [@abozinadah2016improved; @abozinadah2017detecting; @brahimi2016data; @mourad2017language]. Tashaphyne has also been utilized for building resources such as corpora [@van2018bridging] and ontologies [@albukhitan2017arabic], question answering [@ezzeldin2015exploring; @ezzeldin2014answer], and information retrieval [@mortaja2017developing].



# Acknowledgements

We gratefully acknowledge the contributions of Tashaphyne light stemmer, and Arabeyes.org during the project's inception.



# References

