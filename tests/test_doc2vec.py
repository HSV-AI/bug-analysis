import unittest
from hsvai.doc2vec import Doc2VecRec

class TestDoc2Vec(unittest.TestCase):

    def test_load(self):
        rec = Doc2VecRec()
        self.assertIsNone(rec.model)
        rec.load('data/bugzilla.doc2vec')
        self.assertIsNotNone(rec.model)

    def test_constuctor(self):
        rec = Doc2VecRec('data/bugzilla.doc2vec')
        self.assertIsNotNone(rec.model)

    def test_recommender(self):
        rec = Doc2VecRec('data/bugzilla.doc2vec')
        result = rec.recommend_closest("The grammar rules have a problem with linking external files")
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
    
    @unittest.expectedFailure
    def test_recommender_failure(self):
        rec = Doc2VecRec()
        result = rec.recommend_closest("The grammar rules have a problem with linking external files")
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
