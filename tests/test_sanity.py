from composition.algebra import *
from composition.vectors import * 


def main():
    is_a = IsAVector()
    has_property = HasPropertyVector()
    at_location = AtLocationVector()
    u = is_a * has_property
    v = has_property * at_location 
    t = at_location * is_a
    print u
    print u.check_type()
    print v
    print v.check_type()
    print t 
    print t.check_type()
    
    

if __name__ == '__main__':
    main()
  



