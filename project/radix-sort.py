import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    newdata = []
    max = len(data[0])
    for i in range(1, len(data)):
  	    if len(data[i]) > max:
  		    max = len(data[i])
    for x in data:
        l = list(x)
        for i in range(len(l)):
            y = l[i]
            l[i] = hex(ord(y))
        if len(l) < max:
            for j in range(max-len(l)):
                l.append('')
        newdata.append(l)
    for i in range(max,0,-1):
        buckets = {}
        for x in newdata:
            if x[i-1] not in buckets:
                buckets[x[i-1]] = 1
            else:
                buckets[x[i-1]] += 1
        sortdata = []
        for y in sorted(buckets):
            for z in newdata:
                if y == z[i-1]:
                    sortdata.append(z)
        del newdata
        del buckets
        newdata = sortdata
        del sortdata
    finaldata = []
    for x in newdata:
        newstr = ''
        for y in x:
            if y != '':
                s = y[2:]
                b = bytes.fromhex(s)
                a = b.decode("ASCII")
                newstr = newstr + a
        finaldata.append(newstr)
    return finaldata
