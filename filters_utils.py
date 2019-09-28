import gensim
from data.constants import sexy_words_list, violent_words_list, non_prod_words_list
from scipy import spatial

path_to_gnews_model = "data/models/GoogleNews-vectors-negative300.bin"
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(path_to_gnews_model, binary=True)


def get_filter_value(text):
    global word2vec_model
    if word2vec_model is None:
        word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(path_to_gnews_model, binary=True)
    print("Model Ready.")

    count_good = 0
    count = 0

    for w in text.split(" "):
        if w in word2vec_model:
            for w_bad in (sexy_words_list + violent_words_list + non_prod_words_list):
                if w_bad in word2vec_model:
                    dist = spatial.distance.cosine(word2vec_model[w], word2vec_model[w_bad])
                    if dist < 0.6:
                        print(w, w_bad, dist)
                        count += dist
                    else:
                        count_good += dist

    if count == 0:
        belief = False
    elif count_good / count > 50 and count_good / count != np.inf:
        belief = True
    else:
        belief = False

    return belief



