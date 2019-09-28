import gensim

path_to_gnews_model = "data/model/GoogleNews-vectors-negative300.bin"
# word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(path_to_gnews_model, binary=True)



def get_filter_value(filter_name, m):
    # if m is None:
    #     m = gensim.models.KeyedVectors.load_word2vec_format(path_to_gnews_model, binary=True)
    # print("Model Ready.")
    #
    # def apply_fct(m, *x):
    #     tot = np.ones(300)
    #     for a in x[0].split(" "):
    #         if a in m:
    #             tot += m[a]
    #     return tot
    return (filter_name-m)




