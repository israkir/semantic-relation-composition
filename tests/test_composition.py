import unittest as ut
import itertools

from composition.vectors import *


class TestComposition(ut.TestCase):
    def setUp(self):
        self.is_a = IsAVector()
        self.has_property = HasPropertyVector()
        self.at_location = AtLocationVector()
        self.has_a = HasAVector()
        self.motivated_by_goal = MotivatedByGoalVector()
        self.causes_desire = CausesDesireVector()
        self.capable_of = CapableOfVector()
        self.has_prerequisite = HasPrerequisiteVector()

    
    def test_isa_hasproperty(self):
        u = self.is_a * self.has_property
        self.assertEqual(u, self.has_property, msg='%s' % u)
    
    
    def test_isa_isa(self):
        u = self.is_a * self.is_a
        self.assertEqual(u, self.is_a, msg='%s' % u)
        
        
    def test_hasproperty_atlocation(self):
        u = self.has_property * self.at_location
        self.assertEqual(u, self.at_location, msg='%s' % u)
        
    
    def test_isa_atlocation(self):
        u = self.is_a * self.at_location
        self.assertEqual(u, self.at_location, msg='%s' % u)
    

    def test_atlocation_atlocation(self):
        u = self.at_location * self.at_location
        self.assertEqual(u, self.at_location, msg='%s' % u)
    
    
    def test_isa_hasa(self):
        u = self.is_a * self.has_a
        self.assertEqual(u, self.has_a, msg='%s' % u)
    

    def test_hasa_hasa(self):
        u = self.has_a * self.has_a
        self.assertEqual(u, self.has_a, msg='%s' % u)
        
        
    def test_hasa_atlocation(self):
        u = self.has_a * self.at_location
        self.assertEqual(u, self.at_location, msg='%s' % u)
        
        
    def test_isa_capableof(self):
        u = self.is_a * self.capable_of
        self.assertEqual(u, self.capable_of, msg='%s' % u)
        
        
    def test_hasa_capableof(self):
        u = self.has_a * self.capable_of
        self.assertEqual(u, self.capable_of, msg='%s' % u)
    

    def test_hasprerequisite_hasprerequisite(self):
        u = self.has_prerequisite * self.has_prerequisite
        self.assertEqual(u, self.has_prerequisite, msg='%s' % u)
    
        
    def test_motivatedbygoal_causesdesire(self):
        u = self.motivated_by_goal * self.causes_desire
        self.assertEqual(u, self.motivated_by_goal, msg='%s' % u)
        

if __name__ == '__main__':
    ut.main()