import math
from nlp.BM25 import BM25



def get_similarity(jd,corpus):
    stopwords = set(['for', 'a', 'of', 'the', 'and', 'to', 'in'])
    texts = [
    [word for word in document.lower().split() if word not in stopwords]
    for document,link in corpus
    ]

    # build a word count dictionary so we can remove words that appear only once
    word_count_dict = {}
    for text in texts:
        for token in text:
            word_count = word_count_dict.get(token, 0) + 1
            word_count_dict[token] = word_count

    texts = [[token for token in text if word_count_dict[token] > 1] for text in texts]
    query = jd
    query = [word for word in query.lower().split() if word not in stopwords]

    bm25 = BM25()
    bm25.fit(texts)
    scores = bm25.search(query)
    ret=[]
    i=0
    for score, doc in zip(scores, corpus):
        score = round(score, 3)
        # print(str(score) + '\t' + doc)
        ret.append((str(score),doc[1]))
        i+=1
    return ret

