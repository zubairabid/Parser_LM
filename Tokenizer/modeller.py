from nltk.tokenize import word_tokenize
import pickle

def ngrams(sentence, n):
    '''
    This currently does not accomodate for numbers with punctuation.
    '''
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [ngram for ngram in ngrams]

def create_model(file="corpus2.txt", n=3):
    '''
    Takes a file to train on, an 'n'
    Returns predictive n-gram model
    '''
    # Create a placeholder for model
    model = defaultdict(lambda: defaultdict(lambda: 0))

    with open(file, 'r') as f:
        for line in f:
            for ngram in ngrams(line, n=n):
                wprec = tuple(ngram[:n-1])
                waft = ngram[n-1]
                model[wprec][waft] += 1
        f.close()    

    for wprec in model:
        total_count = float(sum(model[wprec].values()))
        for waft in model[wprec]:
            model[wprec][waft] /= total_count
            
    return model

model = create_model(n=3)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(model, handle)
