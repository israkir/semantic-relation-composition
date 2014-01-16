
class Algebra(object):
    def __init__(self, definition = None):
        self.definition = definition
        
    def do_operation(self, value1, value2):
        return self.definition[value1 + value2]
        
        
class ComposableAlgebra(Algebra):
    definition = {
        '--': 'P',
        '-0': '0',
        '-+': 'P',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': 'P',
        '+0': '0',
        '++': '+', 
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)
        
        
class FunctionalAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': '+',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': '+',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)
        
        
class SeparableAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': '+',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': '+',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)

        
class TemporalAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': 'P',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': 'P',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)
       

class ConnectedAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '-',
        '-+': '+',
        '0-': '-',
        '00': '0',
        '0+': '+',
        '+-': '+',
        '+0': '+',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)


class IntrinsicAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': '+',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': '-',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)    
        
        
class StructuralAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': '+',
        '0-': '-',
        '00': '0',
        '0+': '+',
        '+-': '+',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)
        
        
class NearAlgebra(ConnectedAlgebra):
    def __init__(self):
        ConnectedAlgebra.__init__(self)
        

class IndexedTemporalAlgebra(Algebra):
    definition = {
        '--': '-',
        '-0': '0',
        '-+': '0',
        '0-': '0',
        '00': '0',
        '0+': '0',
        '+-': '0',
        '+0': '0',
        '++': '+',
    }
    def __init__(self, definition = definition):
        Algebra.__init__(self, definition)     
        
