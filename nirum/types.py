import collections

__all__ = 'ImmutableList',


class ImmutableList(collections.Sequence):

    def __init__(self, l):
        self.l = l

    def __getitem__(self, index):
        return self.l[index]

    def __len__(self):
        return len(self.l)

    def __contains__(self, item):
        return item in self.l

    def __iter__(self):
        return iter(self.l)

    def index(self, item):
        return self.l.index(item)

    def count(self):
        return self.l.count()
