#coding: utf-8

from BinaryRelation import BinaryRelation


class GreaterThanBinaryRelation(BinaryRelation):
    """A Binary Relation which elements in an ordered pair share the same first letter."""

    def contains_ordered_pair(self, x, y):
        """
        This method returns a boolean value indicating if the first element of a given ordered pair is greater than the second one.

        Arguments:
        x - The first element of the ordered pair.
        y - The second element of the ordered pair.

        Return True if the first element of the ordered pair is greater than the second element, otherwise, return False.
        """
        if x > y:
            return True
        return False

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        Arguments:
        S - The input set.
        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """
        tuplas = set([(x,y) for x in S for y in S])
        resultado = set()
        for tupla in tuplas:
            if self.contains_ordered_pair(tupla[0],tupla[1]):
                resultado.add(tupla)
        return resultado
