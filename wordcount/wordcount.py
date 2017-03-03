import sys
import re

def words_dict(filename):
    f = open(filename, 'r')
    s = f.read().lower()
    l = re.split("\n|--| ||! |\? |. |;", s)
    d = dict()
    for i in range(len(l)):
        if not l[i] in d:
            d[l[i]] = 1
        else:
            d[l[i]]+=1
    del d['']
    return d

def print_words(filename):
    d=words_dict(filename)
    for i, j in d.items():
        print(i, j)
    return None

def print_top(filename):
    d = words_dict(filename)
    a=sorted(d.items(), key=lambda x:x[1], reverse=True)
    if len(a)>20:
        print(a[0:20])
    else:
        print(a)
    return None

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
  main()