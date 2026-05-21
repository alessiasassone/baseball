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
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result
