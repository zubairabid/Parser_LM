import re

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

    with open('../corpus3.txt', 'r') as f:
    l = ''
    for line in f:
        l = reg_tokenize(line)
    	print(l)

