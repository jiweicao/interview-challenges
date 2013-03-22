"""
class Similarity : used to write similarity check function

similarity_eval_equal: 
    check whether one query is within related searches results from another query
    if yes, tow queries are synonyms
    if no, continue to use similarity_eval_cosine()

similarity_eval_cosine:
    reference: http://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-very-simple-graphical-way

    e.g. 
    query1: "ac adapter"
    related_searchs: ['ac adapter 12v', 'ac adapter 9v', 'universal ac adapter']
    dict1: {'ac': 3, 'universal': 1, 'adapter': 3, '12v': 1, '9v': 1}

    query2: "power adapter"
    related_searchs: ['power adapter europe', 'power adapter travel', 'universal power adapter']
    dict2: {'europe': 1, 'adapter': 3, 'universal': 1, 'travel': 1, 'power': 3}

    transform to vector space:
    _dict1: {'europe': 0, 'ac': 3, 'power': 0, 'adapter': 3, '12v': 1, 'travel': 0, 'universal': 1, '9v': 1}
    _dict2: {'europe': 1, 'ac': 0, 'power': 3, 'adapter': 3, '12v': 0, 'travel': 1, 'universal': 1, '9v': 0}
    
    Then use cosine method to calculate the similarity.
    Here I use 0.3 as a gap, according the performance.
    Also, for other similarity check method, could implemented inside the class.
    
"""
from Opener import Opener
from collections import OrderedDict
from math import  sqrt

class Similarity(object):
    @staticmethod
    def similarity_eval_equal(ob1, vec1, ob2, vec2):
        return ob1 in vec2 or ob2 in vec1

    @staticmethod
    def similarity_eval_cosine(d1, d2):
        if d1 and d2:
            p = Similarity.cosine_cal(d1,d2)
            print "similarity:", p # printing for debugging
            return p > 0.3 # parameter, generated by training
        return False

    @staticmethod 
    def cosine_cal(d1, d2):
        _d1 = {}
        _d2 = {}
        for key in d1:
            _d1[key] = d1[key]
            if d2.has_key(key):
                _d2[key] = d2[key]
            else:
                _d2[key] = 0
                
        for key in d2:
            _d2[key] = d2[key]
            if d1.has_key(key):
                _d1[key] = d1[key]
            else:
                _d1[key] = 0

        m1 = sum(x*x for x in _d1.values())
        m2 = sum(y*y for y in _d2.values())
        m1m2 = 0
        for i in xrange(len(_d1.values())):
            m1m2 += _d1.values()[i]*_d2.values()[i]
        return  m1m2/sqrt(m1)/sqrt(m2)

# Test
def main():
    opener1 = Opener("ac adapter")
    opener2 = Opener("power adapter")
    
    if Similarity.similarity_eval_equal(opener1.get_name(), opener1.get_related_searchs(), opener2.get_name(), opener2.get_related_searchs()):
        print "Yes"
    else:
        print "No"
    if Similarity.similarity_eval_cosine(opener1.get_dict(), opener2.get_dict()):
        print "Yes"
    else:
        print "No"

if __name__ == "__main__":
    main()
