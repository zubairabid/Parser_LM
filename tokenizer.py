import re
import sys
import pickle
from collections import defaultdict

print()

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

with open(sys.argv[1], 'r') as f:
    lines = f.read()
    toks = []
    l = reg_tokenize(lines)
    for line in l:
        for k in line.split(' '):
            toks.append(k)
        print(line)

    with open('tokens_'+str(sys.argv[1]), 'wb+') as f:
        pickle.dump(toks, f)



# with open('tokens_'+str(sys.argv[1]), 'rb') as f:
# 	tks = pickle.load(f)

# counter = defaultdict(lambda: 0)
# for tok in tks:
#     counter[tok] += 1

# sortdict = sorted(counter.items(), key=lambda v: v[1], reverse=True)

