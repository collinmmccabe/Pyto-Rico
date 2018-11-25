# From PEP 351
class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear       = _immutable
    update      = _immutable
    setdefault  = _immutable
    pop         = _immutable
    popitem     = _immutable

d = {'small_indigo_plant': {
        'name': 'small_indigo_plant', 
        'good_processed': 'indigo',
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': (production, purple),
        'perk_description': str,
        'base_cost': 3,
        'quarries_allowed': 1,
        'vp_value': 2
        }
    }

building_lookup = imdict(d)
