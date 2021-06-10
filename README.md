# german_general_entity_typing


This repository contains code for the following paper:
 - Weber, Sabine, and Mark Steedman. "Fine-grained General Entity Typing in German using GermaNet." Proceedings of the Fifteenth Workshop on Graph-Based Methods for Natural Language Processing (TextGraphs-15). 2021.

 ```bibtex
@inproceedings{weber2021fine,
  title={Fine-grained General Entity Typing in German using GermaNet},
  author={Weber, Sabine and Steedman, Mark},
  booktitle={Proceedings of the Fifteenth Workshop on Graph-Based Methods for Natural Language Processing (TextGraphs-15)},
  pages={138--143},
  year={2021}
}
 ```
 
# Setup
This code can be used to assign FIGER types to general entities in German. This can be used as a stand-alone solution to German entity typing, but we recommend to use the output as training data for Chen et al. (2020)'s hierarchical typing system. For more details, consult the paper.

1. Create a virtual environment using the requirements.txt file. The python version is 3.6.
2. Setup pygermanet (https://pypi.org/project/pygermanet/)
3. Your input file has to be sentence-split German text, one line per sentence.
4. Modify the input and output file name in preparing_german_silver_data.py 
5. Run preparing_german_silver_data.py. The output file contains your input sentences with the nouns in them annotated.
6. Modify the input and output file name in germanet_annotation.py. The input file should be the output from preparing_german_silver_data.py
7. Run preparing_german_silver_data.py. The output file contains your input sentences annotated with FIGER types. Ambiguous cases and cases that are not in GermaNet have been filtered out.

