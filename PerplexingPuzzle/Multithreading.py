"""
Jiwei                                                                                            
Perlexing Puzzle from: http://www.bloomreach.com/puzzles/

Main function to check each pair of synonyms
Please Check documents in Opener.py and Similarity.py first

Because it takes for web crawling, so I use 10 threads to do the same thing.
Because of multithreading, output is not the same order for input file, but could be easily sorted.

"""
import thread
from Opener import Opener
from Similarity import Similarity

f = open('output', 'wa', 0)
dict_opener = {}

def worker(line):
   line = line.strip().split(',')
   if not dict_opener.has_key(line[0]):
       opener1 = Opener(line[0])
       dict_opener[line[0]] = opener1
   else:
       opener1 = dict_opener[line[0]]

   if not dict_opener.has_key(line[1]):
       opener2 = Opener(line[1])
       dict_opener[line[1]] = opener2
   else:
       opener2 = dict_opener[line[1]]

   if Similarity.similarity_eval_equal(line[0], opener1.get_related_searchs(),
                                       line[1], opener2.get_related_searchs()):
       f.write(line[0] + ";" + line[1] + ";" + "true\n")
   elif Similarity.similarity_eval_cosine(opener1.get_dict(), opener2.get_dict()):
       f.write(line[0] + ";" + line[1] + ";" + "true\n")
   else:
       f.write(line[0] + ";" + line[1] + ";" + "false\n")

def main():
   filename = "candidate_synonyms.txt"
   file = open(filename)
   from multiprocessing import Pool
   p = Pool(10)
   p.map(worker, file)

if __name__ == "__main__":
   main()
