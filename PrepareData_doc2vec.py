# coding:utf-8
import ProcessUseCase
import ProcessSourceCode
import ProcessOracle
import sys
import gensim
import numpy as np

from gensim.models.doc2vec import Doc2Vec, LabeledSentence

TaggededDocument = gensim.models.doc2vec.TaggedDocument


def generate_model():
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    sourcecode_dict_keys = list(sourcecode_dict.keys())

    class_name_documents = []
    class_comment_documents = []
    class_method_name_documents = []
    class_method_comment_documents = []
    class_method_parameter_documents = []
    class_method_return_documents = []
    for sourcecode_key in sourcecode_dict_keys:
        sourcecode = sourcecode_dict[sourcecode_key]
        sourcecode_classname_list = sourcecode["class name"]
        sourcecode_classcomment_list = sourcecode["class comment"]
        sourcecode_method_list = sourcecode["method"]
        class_name_documents.append(sourcecode_classname_list)
        class_comment_documents.append(sourcecode_classcomment_list)
        method_name = []
        method_comment = []
        method_parameter = []
        method_return = []
        for method in sourcecode_method_list:
            method_name.extend(method["method name"])
            method_comment.extend(method["method comment"])
            method_parameter.extend(method["method parameter"]["word"])
            method_return.extend(method["method return"]["word"])

        class_method_name_documents.append(method_name)
        class_method_comment_documents.append(method_comment)
        class_method_parameter_documents.append(method_parameter)
        class_method_return_documents.append(method_return)

    # get TaggededDocument
    class_name_traindata = get_TaggededDocument(class_name_documents)
    class_comment_traindata = get_TaggededDocument(class_comment_documents)
    class_method_name_traindata = get_TaggededDocument(class_method_name_documents)
    class_method_comment_traindata = get_TaggededDocument(class_method_comment_documents)
    class_method_parameter_traindata = get_TaggededDocument(class_method_parameter_documents)
    class_method_return_traindata = get_TaggededDocument(class_method_return_documents)

    # train and get the model
    class_name_model = train_model(class_name_traindata)
    class_comment_model = train_model(class_comment_traindata)
    class_method_name_model = train_model(class_method_name_traindata)
    class_method_comment_model = train_model(class_method_comment_traindata)
    class_method_parameter_model = train_model(class_method_parameter_traindata)
    class_method_return_model = train_model(class_method_return_traindata)

    # Save model
    class_name_model.save('../../output/eTour/model/class_name_model_doc2vec')
    class_comment_model.save('../../output/eTour/model/class_comment_model_doc2vec')
    class_method_name_model.save('../../output/eTour/model/class_method_name_model_doc2vec')
    class_method_comment_model.save('../../output/eTour/model/class_method_comment_model_doc2vec')
    class_method_parameter_model.save('../../output/eTour/model/class_method_parameter_model_doc2vec')
    class_method_return_model.save('../../output/eTour/model/class_method_return_model_doc2vec')

def get_TaggededDocument(document_list):
    train_data = []
    for i, word_list in enumerate(document_list):
        document = TaggededDocument(word_list, tags=[i])
        train_data.append(document)

    return train_data

def train_model(train_data, size=200, epoch_num=1):
    model_doc2vec = Doc2Vec(train_data, min_count=1, window=3, vector_size=size, sample=1e-3, negative=5, workers=4)
    model_doc2vec.train(train_data, total_examples=model_doc2vec.corpus_count, epochs=100)
    return model_doc2vec

def get_meta_doc2vec_linklist():
    # Load model
    class_name_model = Doc2Vec.load('../../output/eTour/model/class_name_model_doc2vec')
    class_comment_model = Doc2Vec.load('../../output/eTour/model/class_comment_model_doc2vec')
    class_method_name_model = Doc2Vec.load('../../output/eTour/model/class_method_name_model_doc2vec')
    class_method_comment_model = Doc2Vec.load('../../output/eTour/model/class_method_comment_model_doc2vec')
    class_method_parameter_model = Doc2Vec.load('../../output/eTour/model/class_method_parameter_model_doc2vec')
    class_method_return_model = Doc2Vec.load('../../output/eTour/model/class_method_return_model_doc2vec')

    usecase_dict = ProcessUseCase.get_usecase_infomation()
    usecase_dict_keys = list(usecase_dict.keys())

    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    sourcecode_dict_keys = list(sourcecode_dict.keys())

    oracle_list = ProcessOracle.get_oracle_list()

    link_list = []
    for usecase_key in usecase_dict_keys:
        usecase = usecase_dict[usecase_key]
        usecase_filename = usecase["file name"]
        usecase_name_list = usecase["name"]
        usecase_description_list = usecase["description"]

        usecase_name_vector = class_name_model.infer_vector(usecase_name_list)
        sims_usecasename_classname = class_name_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_name_model.infer_vector(usecase_description_list)
        sims_usecasedescription_classname = class_name_model.docvecs.most_similar([usecase_description_vector], topn=None)

        usecase_name_vector = class_comment_model.infer_vector(usecase_name_list)
        sims_usecasename_classcomment = class_comment_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_comment_model.infer_vector(usecase_description_list)
        sims_usecasedescription_classcomment = class_comment_model.docvecs.most_similar([usecase_description_vector], topn=None)

        usecase_name_vector = class_method_name_model.infer_vector(usecase_name_list)
        sims_usecasename_methodname = class_method_name_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_method_name_model.infer_vector(usecase_description_list)
        sims_usecasedescription_methodname = class_method_name_model.docvecs.most_similar([usecase_description_vector], topn=None)

        usecase_name_vector = class_method_comment_model.infer_vector(usecase_name_list)
        sims_usecasename_methodcomment = class_method_comment_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_method_comment_model.infer_vector(usecase_description_list)
        sims_usecasedescription_methodcomment = class_method_comment_model.docvecs.most_similar([usecase_description_vector], topn=None)

        usecase_name_vector = class_method_parameter_model.infer_vector(usecase_name_list)
        sims_usecasename_methodparameter = class_method_parameter_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_method_parameter_model.infer_vector(usecase_description_list)
        sims_usecasedescription_methodparameter = class_method_parameter_model.docvecs.most_similar([usecase_description_vector], topn=None)

        usecase_name_vector = class_method_return_model.infer_vector(usecase_name_list)
        sims_usecasename_methodreturn = class_method_return_model.docvecs.most_similar([usecase_name_vector], topn=None)

        usecase_description_vector = class_method_return_model.infer_vector(usecase_description_list)
        sims_usecasedescription_methodreturn = class_method_return_model.docvecs.most_similar([usecase_description_vector], topn=None)

        for index in range(len(sourcecode_dict_keys)):
            link = {}
            sourcecode_filename = sourcecode_dict_keys[index]
            link["link name"] = [usecase_filename, sourcecode_filename]

            dimension1 = sims_usecasename_classname[index]
            dimension2 = sims_usecasedescription_classname[index]
            dimension3 = sims_usecasename_classcomment[index]
            dimension4 = sims_usecasedescription_classcomment[index]
            dimension5 = sims_usecasename_methodname[index]
            dimension6 = sims_usecasedescription_methodname[index]
            dimension7 = sims_usecasename_methodcomment[index]
            dimension8 = sims_usecasedescription_methodcomment[index]
            dimension9 = sims_usecasename_methodparameter[index]
            dimension10 = sims_usecasedescription_methodparameter[index]
            dimension11 = sims_usecasename_methodreturn[index]
            dimension12 = sims_usecasedescription_methodreturn[index]

            vector = [dimension1, dimension2, dimension3, dimension4]
            vector.extend([dimension5, dimension6, dimension7, dimension8])
            vector.extend([dimension9, dimension10, dimension11, dimension12])

            link["link vector"] = vector
            if link["link name"] in oracle_list:
                link["link flag"] = True
            else:
                link["link flag"] = False
            link_list.append(link)

    # print("link_list =", len(link_list), link_list[:100])
    return link_list


train_begin_index = 0
train_end_index = 2000
test_begin_index = 3500
test_end_index = 4000


def get_train_meta_data():
    link_list = get_meta_doc2vec_linklist()
    train_data = link_list[train_begin_index:train_end_index]
    return train_data


def get_test_meta_data():
    link_list = get_meta_doc2vec_linklist()
    test_data = link_list[test_begin_index:test_end_index]
    return test_data


def get_ml_data(meta_link_list, x_data, y_data):
    # print("meta_link_list =", len(meta_link_list), meta_link_list)
    for link in meta_link_list:
        link_vector = link["link vector"]

        link_flag = link["link flag"]
        if link_flag is True:
            link_tag = 1
        if link_flag is False:
            link_tag = 0
        x_data.append(link_vector)
        y_data.append(link_tag)
    # print("train_x[20] =", train_x[20])
    # print("train_y[20] =", train_y[20])

def get_oracle_data():
    oracle_data = []
    link_list = get_meta_doc2vec_linklist()
    for link in link_list:
        if link["link flag"] is True:
            oracle_data.append(link["link vector"])
            print(link["link name"], "=", link["link vector"])

    return oracle_data

def get_nonlink_data():
    nonlink_data = []
    link_list = get_meta_doc2vec_linklist()
    for link in link_list:
        if link["link flag"] is False:
            nonlink_data.append(link["link vector"])
            print(link["link name"], "=", link["link vector"])

    return nonlink_data

if __name__ == '__main__':
    # train_meta_data = get_train_meta_data()
    # test_metadata = get_test_meta_data()
    # print("train_meta_data =", len(train_meta_data), train_meta_data)
    # print("test_metadata =", len(test_metadata), test_metadata)

    print()
