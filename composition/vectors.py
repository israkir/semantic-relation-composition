from composition.algebra import *


def compose(vector1, vector2):
    """
    Semantically compose two vectors based on their attributes composition.
    The results for each operation is implemented in algebra.py.
    """
    attributes = {}
    
    composable_algebra = ComposableAlgebra()
    attributes['composable'] = composable_algebra.do_operation(vector1.get_attr('composable'), 
        vector2.get_attr('composable'))
    functional_algebra = FunctionalAlgebra()
    attributes['functional'] = functional_algebra.do_operation(vector1.get_attr('functional'), 
        vector2.get_attr('functional'))
    separable_algebra = SeparableAlgebra()
    attributes['separable'] = separable_algebra.do_operation(vector1.get_attr('separable'), 
        vector2.get_attr('separable'))
    temporal_algebra = TemporalAlgebra()
    attributes['temporal'] = temporal_algebra.do_operation(vector1.get_attr('temporal'), 
        vector2.get_attr('temporal'))
    connected_algebra = ConnectedAlgebra()
    attributes['connected'] = connected_algebra.do_operation(vector1.get_attr('connected'), 
        vector2.get_attr('connected'))
    intrinsic_algebra = IntrinsicAlgebra()
    attributes['intrinsic'] = intrinsic_algebra.do_operation(vector1.get_attr('intrinsic'), 
        vector2.get_attr('intrinsic'))
    structural_algebra = StructuralAlgebra()
    attributes['structural'] = structural_algebra.do_operation(vector1.get_attr('structural'), 
        vector2.get_attr('structural'))
    near_algebra = NearAlgebra()
    attributes['near'] = near_algebra.do_operation(vector1.get_attr('near'), 
        vector2.get_attr('near'))
    indexed_temporal_algebra = IndexedTemporalAlgebra()
    attributes['indexed_temporal'] = indexed_temporal_algebra.do_operation(
        vector1.get_attr('indexed_temporal'), vector2.get_attr('indexed_temporal'))

    return RelationVector(attributes)


def find_vector_type(unknown_vector):
    vectors = [IsAVector(), HasPropertyVector(), AtLocationVector(), UsedForVector(), 
        CapableOfVector(), HasSubeventVector(), RelatedToVector(), HasPrerequisiteVector(), 
            HasAVector(), MotivatedByGoalVector(), CausesVector(), DefinedAsVector(), 
                ReceivesActionVector(), PartOfVector(), DesiresVector(), CausesDesireVector(), 
                    LocatedNearVector(), ObstructedByVector(), HasFirstSubeventVector(), 
                        HasLastSubeventVector(), MadeOfVector(), SimilarSizeVector(), 
                            InheritsFromVector(), InstanceOfVector()]
    for v in vectors:
        if cmp(v.attributes, unknown_vector.attributes) == 0:
            return v
    return None

    
class RelationVector(object):
    """
    Base class for relation vector objects such as IsA, HasProperty etc.
    """
    def __init__(self, attributes = None):
        self.attributes = attributes
        
    def get_attr(self, attr):
        """
        Return the value of 'attr' in 'self.attributes'.
        """
        return self.attributes[attr]
        
    def get_vector_type(self):
        """
        Return the vector type of this relation vector.
        """
        return find_vector_type(self)
    
    def __mul__(self, other_vector):
        """
        Override conventional dot product of 'this' vector and 'other_vector'.
        In our terms, vec1 * vec2 will return composition result of two semantic vectors
        based on our custom Algebra classes.
        """
        if isinstance(other_vector, RelationVector):
            return compose(self, other_vector)
        else:
            raise TypeError("Cannot do operation with type %s" % type(other_vector))
       
    def __eq__(self, other_vector):
        return True if cmp(self.attributes, other_vector.attributes) == 0 else False
        
    def __repr(self):
       return self.__class__ 
    
    def __str__(self):
        """
        String representation of object is list of primitive values specified in order of 
        class definition.
        """
        return '[' + ', '.join([self.get_attr('composable'), self.get_attr('functional'), 
            self.get_attr('separable'), self.get_attr('temporal'), self.get_attr('connected'), 
                self.get_attr('intrinsic'), self.get_attr('structural'), self.get_attr('near'), 
                    self.get_attr('indexed_temporal')]) + ']'
        

class IsAVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '+', 
        'structural'       : '-', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'a'
            
            
class HasPropertyVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'b'
        
        
class AtLocationVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '-', 
        'structural'       : '+', 
        'near'             : '-', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'c'

        
class UsedForVector(RelationVector):
    attributes = {
        'composable'       : '-', 
        'functional'       : '+', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '0', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'd'
        
        
class CapableOfVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'e'
        
      
class HasSubeventVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '+', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'f'
        
        
class RelatedToVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'g'
        
        
class HasPrerequisiteVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '+', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'h'
        
        
class HasAVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'i'
        
        
class MotivatedByGoalVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '-', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'j'
        
        
class CausesVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '-', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '-', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'k'
        
        
class DefinedAsVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'l'
        
        
class ReceivesActionVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'm'
        
        
class PartOfVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '-', 
        'near'             : '-', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'n'
        
        
class DesiresVector(RelationVector):
    attributes = {
        'composable'       : '-', 
        'functional'       : '-', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '-', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'o'
        
        
class CausesDesireVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '-', 
        'temporal'         : '+', 
        'connected'        : '-', 
        'intrinsic'        : '-', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'p'
        
        
class LocatedNearVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '-', 
        'structural'       : '+', 
        'near'             : '+', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'q'
        
        
class ObstructedByVector(RelationVector):
    attributes = {
        'composable'       : '-', 
        'functional'       : '0', 
        'separable'        : '0', 
        'temporal'         : '0', 
        'connected'        : '0', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'r'
        
     
class HasFirstSubeventVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '+', 
        'indexed_temporal' : '+'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 's'
        
        
class HasLastSubeventVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '0', 
        'near'             : '+', 
        'indexed_temporal' : '-'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 't'
        
        
class MadeOfVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '0', 
        'intrinsic'        : '+', 
        'structural'       : '-', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'u'
        
        
class SimilarSizeVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '0', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'v'


class InheritsFromVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '0', 
        'structural'       : '+', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'w'


class InstanceOfVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '+', 
        'intrinsic'        : '+', 
        'structural'       : '+', 
        'near'             : '0', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        self.name = 'x'
