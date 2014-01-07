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
        
    def check_type(self):
        if self == IsAVector:
            return IsAVector()
        elif self == HasPropertyVector:
            return HasPropertyVector()
        elif self == AtLocationVector:
            return AtLocationVector()
        else:
            return None
        
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
        
        
class ReceivesActionVector(RelationVector):
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
        
        
class LocatedNearVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '-', 
        'separable'        : '+', 
        'temporal'         : '0', 
        'connected'        : '0', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '+', 
        'indexed_temporal' : '0'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        
        
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
        
     
class HasFirstSubeventVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '+'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        
        
class HasLastSubeventVector(RelationVector):
    attributes = {
        'composable'       : '+', 
        'functional'       : '+', 
        'separable'        : '+', 
        'temporal'         : '+', 
        'connected'        : '+', 
        'intrinsic'        : '0', 
        'structural'       : '0', 
        'near'             : '0', 
        'indexed_temporal' : '-'
    }
    def __init__(self, attributes = attributes):
        RelationVector.__init__(self, attributes)
        
        
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