from attrdict import AttrDict

def as_attrdict(val):
    if not isinstance(val, AttrDict):
        raise TypeError('not AttrDict')
    return AttrDictForJson(val)


class AttrDictForJson(dict):

    def __init__(self, attrdict):
        super().__init__()
        self.items = attrdict.items
        self._len = attrdict.__len__
        # key creation necessary for json.dump to work with CPython 
        # This is because optimised json bypasses __len__ on CPython
        if self._len() != 0:
            self[None] = None

    def __len__(self):
        return self._len()