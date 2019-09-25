import pickle
from collections import Counter, defaultdict

def reg_tokenize(sent):
    return re.findall(r'[A-Z0-9a-z]+[A-Z0-9a-z._%+-]*@[A-Z0-9a-z]+(?:\.[A-Z0-9a-z]+)+|(?<= )[$€£¥₹]?[0-9]+(?:[,.][0-9]+)*[$€£¥₹]?|(?:(?:https?:\/\/(?:www.)?)|www.)[A-Z0-9a-z_-]+(?:\.[A-Z0-9a-z_\/-]+)+|(?<= )@[A-Z0-9a-z._%+]+|#[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*|\.{3,}|[!"#$%&\'()*+,\-./:;<=>?@\[\\\]\^_`{\|}~]|\w+', sent)

def ngrams(sentence, n):
    '''
    This currently does not accomodate for numbers with punctuation.
    '''
    print("Getting ngrams for n = {0}, sentence = {1}".format(n, sentence))
    sentence = sentence.lower()
    tokens = reg_tokenize(sentence)
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
    print("counted")
    for wprec in model:
        total_count = float(sum(model[wprec].values()))
        for waft in model[wprec]:
            model[wprec][waft] /= total_count
            
    return model
    print("probabilitied")

model = create_model(n=3)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(model, handle)
