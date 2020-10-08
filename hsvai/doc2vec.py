"""This module contains classes required to train and load
the Doc2Vec models.
"""

import re
from typing import List, Tuple
from gensim.models.doc2vec import Doc2Vec
import spacy
import pkg_resources

class Doc2VecRec:
    """Provides a wrapper around a Gensim Doc2Vec model"""

    nlp = spacy.load("en_core_web_sm")

#TODO - see if there is something to anchor the start of the exception to something other than checking everything
    exception_regex = \
        re.compile(r".+Exception[^\n].*\s+at", re.MULTILINE | re.IGNORECASE)
    greater_regex = \
        re.compile(r"^> .*$", re.MULTILINE | re.IGNORECASE)
    gerrit_created_regex = \
        re.compile(r"New Gerrit change created: [^\ ]+", re.MULTILINE | re.IGNORECASE)
    gerrit_merge_regex = \
        re.compile(r"Gerrit change [^\s]+ was merged to [^\.]+\.", re.MULTILINE | re.IGNORECASE)
    gerrit_commit_regex = \
        re.compile(r"Commit: [^\ ]+", re.MULTILINE | re.IGNORECASE)

    model = None

    lowest_score: float = 100.0
    highest_score: float = 0.0
    highest_text: str = None
    lowest_text: str = None

    def __init__(self, filename: str = None):
        if filename is not None:
            self.load(filename)
        else:
            filename = pkg_resources.resource_filename('hsvai','data/bugzilla.doc2vec')
            self.load(filename)

    def reset_metrics(self):
        """Resets the running metrics to their initial values"""
        self.lowest_score = 100.0
        self.highest_score = 0.0

    def get_highest(self):
        """Returns the highest recommended values"""
        return self.lowest_score, self.lowest_text

    def get_lowest(self):
        """Returns the lowest recommended values"""
        return self.lowest_score, self.lowest_text

    def load(self, filename: str):
        """Load a previously trained model"""
        self.model = Doc2Vec.load(filename)

#TODO - Figure out how to document the parameters here as well!!!
    def recommend_closest(self, text: str) -> List[Tuple[float, float]]:
        """Recomends the 'closest' bugs to the text string passed in.
        :raises:
            RuntimeError: if the Doc2Vec Model has not been loaded..
        """
        
        if self.model is None:
            raise RuntimeError("Doc2Vec Model has not been loaded.")

        tokens = self.tokenize(text)
        vector = self.model.infer_vector(tokens)

        similar = self.model.docvecs.most_similar([vector])

        if len(similar) > 0:
            current = similar[0][1]
            if current > self.highest_score:
                self.highest_score = current
                self.highest_text = text
            if current < self.lowest_score:
                self.lowest_score = current
                self.lowest_text = text
        return similar


    def tokenize(self, text: str) -> List[str]:
        """Returns a list of tokens created from the text."""

        text = self.greater_regex.sub("", text)
        text = self.exception_regex.sub("", text)
        text = self.gerrit_created_regex.sub("", text)
        text = self.gerrit_merge_regex.sub("", text)
        text = self.gerrit_commit_regex.sub("", text)
        filtered_tokens = []

        doc = self.nlp(text)
        for sent in doc.sents:
            for token in sent:
                if re.fullmatch('[a-zA-Z]+', token.text):
                    filtered_tokens.append(token.text)
        return filtered_tokens
