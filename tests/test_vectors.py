import unittest as ut
import itertools

from composition.vectors import *


class TestVectors(ut.TestCase):
    def setUp(self):
        self.vectors = [IsAVector(), HasPropertyVector(), AtLocationVector(), UsedForVector(), 
            CapableOfVector(), HasSubeventVector(), RelatedToVector(), HasPrerequisiteVector(), 
                HasAVector(), MotivatedByGoalVector(), CausesVector(), DefinedAsVector(), 
                    ReceivesActionVector(), PartOfVector(), DesiresVector(), CausesDesireVector(), 
                        LocatedNearVector(), ObstructedByVector(), HasFirstSubeventVector(), 
                            HasLastSubeventVector(), MadeOfVector(), SimilarSizeVector()]
    
    def test_similarity_of_vectors(self):
        for u, v in itertools.permutations(self.vectors, 2):
            if u == v:
                print type(u), type(v)
                
    
if __name__ == '__main__':
    ut.main()