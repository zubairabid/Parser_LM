import re
from collections import Counter, defaultdict
import math


def reg_tokenize(sent):
    fin = []
    for line in iter(sent.splitlines()):
        fin.append(' '.join(re.findall(r'[\U00010000-\U0010ffff]'\
                                       r'|[A-Z0-9a-z]+[A-Z0-9a-z._%+-]*@[A-Z0-9a-z]+(?:\.[A-Z0-9a-z]+)+'\
                                       r'|(?<= )[$€£¥₹]?[0-9]+(?:[,.][0-9]+)*[$€£¥₹]?'\
                                       r'|(?:(?:https?:\/\/(?:www.)?)|www.)[A-Z0-9a-z_-]+(?:\.[A-Z0-9a-z_\/-]+)+'\
                                       r'|(?:(?<=[^A-Za-z0-9])|^)@[A-Z0-9a-z._+]+[A-Za-z0-9_]'\
                                       r'|#[A-Za-z0-9]+(?:[\._-][A-Za-z0-9]+)*'\
                                       r'|\.{3,}'\
                                       r'|[!"#$%\&\'()*+,\-.:;<=>?@\[\\\/\]\^_`{\|}~]'\
                                       r'|[A-Z]\.'\
                                       r'|\w+', line)))
    return fin

def ngrams(sentence, n):    
    tokens = reg_tokenize(sentence)
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [ngram for ngram in ngrams]

cn = defaultdict(lambda: 0)
def create_model(file="../corpus3.txt", n=3):
    '''
    Takes a file to train on, an 'n'
    Returns predictive n-gram model
    '''
    global cn
    # Create a placeholder for model
    model = defaultdict(lambda: defaultdict(lambda: 0))
    incv = defaultdict(lambda: defaultdict(lambda: 0))
    invc = defaultdict(lambda: defaultdict(lambda: 0))

    with open(file, 'r') as f:
        linet = f.read()
    
#         for line in f:
        for i in range(1, n+1):
            for ngram in ngrams(linet, n=i):
                cn[i] += 1
                wprec = tuple(ngram[:i-1])
                waft = ngram[i-1]
                model[wprec][waft] += 1
                if i >= 2:
                    incv[waft][wprec] += 1
                    if incv[waft][wprec] == 1:
                        invc[waft][len(wprec)] += 1
        f.close()    
            
    return model, incv, invc


model, incv, invc = create_model(n=3)













def perplexity(file='../corpus3.txt', n=2):
    text = ''
    with open(file, 'r') as f:
        text = f.read()
    
    summed = 0
    
    seqs = ngrams(text, n=n)
    for seq in seqs:
        total_count = float(sum(model[seq[:-1]].values()))
        prob = model[seq[:-1]][seq[-1]]/total_count
        summed += math.log(prob, 2)
    summed = (summed*-1)/len(seqs)
    
    return pow(2, summed)

