from database.DB_connect import DBConnect
from model.team import Team


#Non serve il costruttore


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT t.`year`  
                    from teams t 
                    where t.`year` >= 1980 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"]) #Non serve oggetto

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeamsOfYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM teams t
                    WHERE t.`year` = %s """

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Team(**row)) # Se mi arriva tutto metto **row

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalariesTeam(year, idMapTeams):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.ID , t.teamCode , sum(s.salary) as totSalary 
                    FROM salaries s , teams t , appearances a 
                    WHERE s.`year` = t.`year` and t.`year` = a.`year` and a.`year` = %s
                    and t.ID = a.teamID and a.playerID = s.playerID 
                    group by t.ID , t.teamCode """

        cursor.execute(query, (year,))

        mapSalary = {} # vuoto che conterrà i salari e decido che avrà come chiave il team e come valore il salario
        # il team viene da un'altra mappa chiamata idMapTeams
        # L'output è un dizionario che avrà come chiave oggetti di tipo team e valore salary
        for row in cursor:
            mapSalary[idMapTeams[row["ID"]]] = row["totSalary"] # qui non prendo tutto, quindi sistemo con mappa

        cursor.close()
        conn.close()
        return mapSalary
