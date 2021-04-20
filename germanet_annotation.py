# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:58:06 2021

@author: Sabine
"""

from pygermanet import load_germanet
gn = load_germanet()

f = open("ontology_full.txt")
word_type_dict = {}

for line in f:
    l = line.strip().split("\t")
    words = l[1].split(",")

    for word in words:
        word_type_dict[word] = l[0]
        
test = open("third_slice_of_500K_combined_wiki_post_spacy.tsv")
out_file = open("third_slice_of_500K_combined_wiki_post_spacy_typed.tsv","w",encoding="utf8")

for line in test:
    out_types = set()
    out_l1 = set()
    out_l2 = set()
    l = line.strip().split("\t")
    sentence = l[0].split(" ")
    index = l[1].split(":")[0]

    word = sentence[int(index)]
    #get hypernym path for word
    wordnet_input = gn.lemmatise(word)
    synsets = gn.synsets(wordnet_input[0])
    hyp_paths_list = []
    
    for syn in synsets:
        try:
            hyp_paths_list.append(syn.hypernym_paths)
        except AttributeError:
            continue

        for hyp_paths in hyp_paths_list:
            for hyp_list in hyp_paths:
                for syn_set in hyp_list:
                    string_rep = str(syn_set)
                    remove_front = string_rep[7:]
                    wd = remove_front[:-5]
                    #for each word in hypernym path check if it is in the word list
                    if wd in word_type_dict.keys():
                        out_types.add(word_type_dict[wd])
    for e in out_types:
        if e.count("/") == 2:
            supertype = "/"+e.split("/")[1]
            out_l2.add(e)
            out_l1.add(supertype)
        else:
            out_l1.add(e)
    out_types = out_l1.union(out_l2)
    
        #if counrty, exclude finance
    if "/location/country" in out_types and "/finance" in out_types:
        out_types.remove("/finance")
    #if city, exclude county
    if "/location/city" in out_types and "/location/county" in out_types:
        out_types.remove("/location/county")
    #if country not county
    if "/location/country" in out_types and "/location/county" in out_types:
        out_types.remove("/location/county")
    #if person, not written_work
    if "/person" in out_types and "/written_work" in out_types:
        out_types.remove("/written_work")
    if "/person" in out_types and "/game" in out_types:
        out_types.remove("/game")

    if len(out_l1)<3 and len (out_l2)<3 and len(out_l2)!=0 and len(out_types)!=0:
        out_string = ' '.join(str(e) for e in out_types)
        out_file.write(line.strip()+"\t"+out_string+"\n")
        
out_file.close()

