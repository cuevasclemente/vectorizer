import collections
import numpy as np
class Vectorizer(object):

    def __init__(self):
        self.mapping = {}
        self.inverse_mapping = {}
        self.embedding_size = 0

    def vectorize_string(self, s):
        vec = np.empty(len(s))
        for i in range(0,len(s)):
            char = s[i]
            if char in self.mapping:
                vec[i] = self.mapping[char]
            else:
                vec[i] = self.embedding_size
                self.mapping[char] = self.embedding_size
                self.inverse_mapping[self.embedding_size] = char
                self.embedding_size += 1
        return vec

    def devectorize(self, v):
        """
        Devectorizes a vector into a a string
        """
        s = ""
        for ident in v:
            s += self.inverse_mapping[ident]
        return s


def vectorize_corpus(corpus):
    """
    corpus: A list of strings we want to vectorize 

    -> 

    vectors: A list of lists that represent vectorized
    representations of the strings

    vectorizer: A vectorizer that can be used to vectorize and devectorize 
    the strings
    """
    vectorizer = Vectorizer()
    # vectors = np.array([])
    index = 1
    mapping = {}
    inverse_mapping = {}
    count = 0.0
    vectors = []
    for i in range(0,len(corpus)):
        s =  ""
        for char in corpus[i, :]:
            s += char
        vectorized = vectorizer.vectorize_string(corpus[i, :])
        # print(vectorized)
        vectors.append(vectorized)
    return np.array(vectors), vectorizer
