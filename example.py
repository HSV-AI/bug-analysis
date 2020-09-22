#! /usr/bin/env python
 
from hsvai.doc2vec import Doc2VecRec

rec = Doc2VecRec('data/bugzilla.doc2vec')

# rec.load('data/bugzilla.doc2vec')
results = rec.recommend_closest("The grammar rules have a problem with linking external files")
print(results)

print(rec.get_highest())
print(rec.get_lowest())

print(rec.recommend_closest("Sally sells seashells by the seashore"))

print(rec.get_highest())
print(rec.get_lowest())
