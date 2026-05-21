import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []

    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        return self._teams

    def creaGrafo(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams)

        # Per gli archi non scrivo una query perchè tanto mi serve un arco per ogni coppia,
        # il doppio for non è ideale
        # for u in self._grafo.nodes:
        #     for v in self._grafo.nodes:
        #         if u != v:
        #             self._grafo.add_edge(u, v)

        myedges = itertools.combinations(self._teams, 2) # mi prendo i team a due a due
        # Add edges from è un metodo che accetta solo tuple
        self._grafo.add_edges_from(myedges)

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)