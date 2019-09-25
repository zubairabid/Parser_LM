from collections import Counter, defaultdict

def new_reg_tokenize(sent):
    fin = re.findall(r'[\U00010000-\U0010ffff]'\
                     r'|[A-Z0-9a-z]+[A-Z0-9a-z._%+-]*@[A-Z0-9a-z]+(?:\.[A-Z0-9a-z]+)+'\
                     r'|(?<= )[$€£¥₹]?[0-9]+(?:[,.][0-9]+)*[$€£¥₹]?'\
                     r'|(?:(?:https?:\/\/(?:www.)?)|www.)[A-Z0-9a-z_-]+(?:\.[A-Z0-9a-z_\/-]+)+'\
                     r'|(?:(?<=[^A-Za-z0-9])|^)@[A-Z0-9a-z._+]+[A-Za-z0-9_]'\
                     r'|#[A-Za-z0-9]+(?:[\._-][A-Za-z0-9]+)*'\
                     r'|\.{3,}'\
                     r'|[!"#$%\&\'()*+,\-.:;<=>?@\[\\\/\]\^_`{\|}~]'\
                     r'|[A-Z]\.'\
                     r'|\w+', sent)
    return fin



import re
# from nltk.tokenize import word_tokenize

def ngrams(sentence, n):
    '''
    This currently does not accomodate for numbers with punctuation.
    '''
#     sentence = sentence.lower()
    
    tokens = new_reg_tokenize(sentence)
    
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [ngram for ngram in ngrams]


def create_model(file="../corpus1.txt", n=3):
    '''
    Takes a file to train on, an 'n'
    Returns predictive n-gram model
    '''
    
    # Create a placeholder for model
    model = defaultdict(lambda: defaultdict(lambda: 0))

    with open(file, 'r') as f:
#         for piece in read_in_chunks(f, chunk_size=2097152):
        
        for line in f:
            for i in range(1, n+1):
                for ngram in ngrams(line, n=i):
                    wprec = tuple(ngram[:i-1])
                    waft = ngram[i-1]
                    model[wprec][waft] += 1
        f.close()    

#     for wprec in model:
#         total_count = float(sum(model[wprec].values()))
#         for waft in model[wprec]:
#             model[wprec][waft] /= total_count
            
    return model

model = create_model(n=3)

for seq in model:
    total_count = float(sum(model[seq].values()))
    for predicted in model[seq]:
        print('For {0} predicted {1} with P={2}'.format(seq, predicted, model[seq][predicted]/total_count))





