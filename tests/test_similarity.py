import unittest as ut
import itertools

from pprint import pprint

from composition.vectors import *


class TestSimilarity(ut.TestCase):
    def setUp(self):
        self.vectors = [IsAVector(), HasPropertyVector(), AtLocationVector(), UsedForVector(), 
            CapableOfVector(), HasSubeventVector(), RelatedToVector(), HasPrerequisiteVector(), 
                HasAVector(), MotivatedByGoalVector(), CausesVector(), DefinedAsVector(), 
                    ReceivesActionVector(), PartOfVector(), DesiresVector(), CausesDesireVector(), 
                        LocatedNearVector(), ObstructedByVector(), HasFirstSubeventVector(), 
                            HasLastSubeventVector(), MadeOfVector(), SimilarSizeVector(),
                                InheritsFromVector(), InstanceOfVector()]
    
    def test_kothari_discriminator_coefficient(self):
        coefficients = {}
        similarities = {}
        for u, v in itertools.permutations(self.vectors, 2):
            # print '%s == %s' % (type(u), type(v))
            cof = 0
            for u_attr, v_attr in itertools.izip(u.attributes, v.attributes):
                #print u.attributes[u_attr], v.attributes[v_attr]
                if u.attributes[u_attr] == v.attributes[v_attr]:
                    cof += 0
                elif (u.attributes[u_attr] == '0' and v.attributes[v_attr] != '0') or (u.attributes[u_attr] != '0' and v.attributes[v_attr] == '0'):
                    cof += 1
                elif (u.attributes[u_attr] != v.attributes[v_attr]) and u.attributes[u_attr] != '0' and v.attributes[v_attr] != '0':
                    cof += 0.5
            cof_key = 'KothariCof(' + str(type(u).__name__) + ','  + str(type(v).__name__) + ')'
            sim_key = 'KothariSimilarityPercentage(' + str(type(u).__name__) + ','  + str(type(v).__name__) + ')'
            coefficients[cof_key] = cof
            similarities[sim_key] = (1 - (cof / float(9))) * 100
        pprint(coefficients)
        pprint(similarities)
        return coefficients, similarities
    
if __name__ == '__main__':
    ut.main()
