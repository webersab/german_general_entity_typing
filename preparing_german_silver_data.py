# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:50:11 2021

@author: Sabine
"""

import spacy
nlp = spacy.load("de_core_news_sm")

in_file = open("third_slice_of_500K_combined_wiki.tsv","r",encoding="utf8")
out_file = open("third_slice_of_500K_combined_wiki.tsv_post_spacy.tsv","w",encoding="utf8")

for line in in_file:
    if "%" in line:
        continue

    doc = nlp(line)
    
    tokenized_string = ""
    for token in doc:
        tokenized_string += token.text+" "

    token_num = 0
    for token in doc:
        if token.pos_ == "NOUN":
            second_token_num = str(int(token_num)+1)
            out_file.write(tokenized_string.strip()+"\t"+str(token_num)+":"+second_token_num+"\n")
        token_num += 1
out_file.close()    
