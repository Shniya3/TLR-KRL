# TLR-KRL
#A traceability link recovery based on knowledge representation learning
#Paper Phase1 preprocess(Windows)：
#Phase1.1 Create software artifacts KG Flow:
#section 1: Create KG
#Fisrt/ We use https://github.com/yeweimian21/AST_JDT in order to get class - member variable - member method xml
#Second/ “xmlparser.py” is used to get Triple from all code cases.
#Third/ "eTour_convertClass.py" is used to translate entity name(such as class, member variable, member method) // Italian->English
#Fourth/ "eTourUCLinkAndDes.py" is used to get uc2ucTriple from use cases and remove character in use cases.
#1st~4th we get software artifacts kg with out traceablity link in eTour
#section2: entity description obtaining
#First/ "eTour_code_comment_extract.py" is used to get the comment in code case.
#Second/ "eTour_entityWordsGenerate.py" is used to generate entityWords.txt(save entity description)
#section3/ "eTourTrainGenerate.py" is used to Combine the above output with the traceability link to output the training set and test #set.
#           traceablitry link triple 4/7 in train set, 3/7 in test set.
#          "TrainTestGenerateForCrossValidation.py" is used to generate Cross validation train and test set. We use three fold cross #validation.
#Phase2: Knowledge representation learning(Linux):
#We use DKRL and its extension model. 
#DKRL: "https://github.com/thunlp/DKRL"
#Extended DKRL: ""
#
#Phase3: Recovery Traceablity link(Windows):
#"eTour_experiment.py" is used to test our approach. 
#We use numpy, sklearn, math 
