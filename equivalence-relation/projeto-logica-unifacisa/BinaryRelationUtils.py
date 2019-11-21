#coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        relacoes=binary_relation.relation(input_set)
	    reflexiva=True
		for i in relacoes:
			primeiro_elem=i[0]
            if (primeiro_elem,primeiro_elem) not in relacoes:
			    reflexiva = False
		return reflexiva

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
		relacoes = binary_relation.relation(input_set)
		simetrica = True
		for i in relacoes:
			primeiro_elem=i[0]
			segundo_elem=i[1]
            if (segundo_elem, primeiro_elem) not in relacoes:
				simetrica = False
		return simetrica

    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        relacoes = binary_relation.relation(input_set)
		transitiva = True
		for i in relacoes:
            primeiro_elem= i[0]
			segundo_elem=i[1]
            for j in relacoes:
                if j[0] == segundo_elem && (primeiro_elem,j[1]) not in relacoes:
                    transitiva = False
		return transitiva

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        antisymmetric or False if it is not.
        """
        relacoes = binary_relation.relation(input_set)
		anti_simetrica = True
		for i in relacoes:
			primeiro_elem=i[0]
			segundo_elem=i[1]
            if (segundo_elem, primeiro_elem) in relacoes and segundo_elem!=primeiro_elem:
				anti_simetrica = False
		return anti_simetrica

    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        an equivalence relation or False if it is not.
        """
        utils=BinaryRelationUtils()
        if(utils.verify_symmetry(binary_relation,input_set)
        and utils.verify_reflexivity(binary_relation,input_set)
        and utils.verify_transitivity(binary_relation,input_set)):
            return True
        else:
            return False


    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.

        Note: The partitioning of the set should be a list of subsets.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: [{1, 3, 5, ...}, {2, 4, 6, ...}]) if it is an equivalence relation.
        """
        utils=BinaryRelationUtils()
        particoes=[]
        if(utils.verify_equivalency(binary_relation, input_set)):
            relacoes = binary_relation.relation(input_set)
            for i in input_set:
                particao = set()
                for j in input_set:
                    if (i,j) in relacoes:
                        particao.add(j)
                if particao not in particoes:
                    particao.append(particao)
            return particao
        else:
            return None
