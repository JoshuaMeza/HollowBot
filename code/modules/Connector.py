"""
Author Joshua Meza
Date 03/01/2021
Version 1.0.0
Class that makes a connection with a mysql database.
"""
import mysql.connector
import os
from dotenv import load_dotenv


class Connector:
    def __init__(self):
        """
        This function is a constructor
        Args:
            self (object): Represents the own object
        Returns:
            Nothing
        """
        # Load enviroment variables
        load_dotenv()

        self.mydb = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('MYSQLUS'),
            password=os.getenv('PASSWD'),
            database=os.getenv('DB')
        )

    def findUser(self, userId, mycursor):
        """
        This method searches if a user exists in the database
        Args:
            self (object): Represents the own object
            userId (str): User id
            mycursor (object): Instantiates objects that can execute operations
            flag (bool): True if added successfully, False if not
            sql (str): A sql scrypt
            myresult (tuple): Data extracted from the database
        Returns:
            True if the user was found or added successfully
        """
        # Load enviroment variables
        load_dotenv()
        flag = True

        sql = "SELECT \
            idUsers \
            FROM `{}`.`Users` \
            WHERE idUsers = {};".format(str(os.getenv('DB')), str(userId))

        try:
            # This method executes the given database operation (query or command).
            mycursor.execute(sql)

            # This method retrieves the next row of a query result set and returns a single sequence,
            # or None if no more rows are available.
            myresult = mycursor.fetchone()

            if myresult == None:
                flag = self.addUser(userId, mycursor)
                mycursor.execute(sql)
                myresult = mycursor.fetchone()
        except Exception as e:
            flag = False

        return flag

    def addUser(self, userId, mycursor):
        """
        This method adds a user into the database
        Args:
            self (object): Represents the own object
            userId (str): User id
            mycursor (object): Instantiates objects that can execute operations
            flag (bool): True if added successfully, False if not
            sql (str): A sql scrypt
        Returns:
            A flag
        """
        # Load enviroment variables
        load_dotenv()
        flag = True

        sql = "INSERT INTO \
            `{}`.`Users` \
            (`idUsers`,`globalWins`) \
            VALUES ('{}','0');".format(str(os.getenv('DB')), str(userId))

        try:
            # This method executes the given database operation (query or command).
            mycursor.execute(sql)
            # This method sends a COMMIT statement to the MySQL server, committing the current transaction.
            self.mydb.commit()
        except Exception as e:
            flag = False

        return flag

    def updateScore(self, userId):
        """
        This method updates the score of a user
        Args:
            self (object): Represents the own object
            userId (str): User id
            mycursor (object): Instantiates objects that can execute operations
            flag (bool): True if added successfully, False if not
            sql (str): A sql scrypt
            myresult (tuple): Data extracted from the database
        Returns:
            True if success, False if not
        """
        # The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
        # Cursor objects interact with the MySQL server using a MySQLConnection object.
        mycursor = self.mydb.cursor()
        flag = True
        # Load enviroment variables
        load_dotenv()

        if (self.findUser(str(userId), mycursor)):
            sql = "SELECT \
                globalWins \
                FROM `{}`.`Users` \
                WHERE idUsers = {}".format(str(os.getenv('DB')), str(userId))

            # This method executes the given database operation (query or command).
            mycursor.execute(sql)

            # This method retrieves the next row of a query result set and returns a single sequence,
            # or None if no more rows are available.
            myresult = mycursor.fetchone()

            newScore = int(myresult[0])
            newScore += 1

            sql = "UPDATE \
                `{}`.`Users` \
                SET `globalWins` = '{}' \
                WHERE (`idUsers` = '{}');".format(str(os.getenv('DB')), str(newScore), str(userId))

            try:
                # This method executes the given database operation (query or command).
                mycursor.execute(sql)
                # This method sends a COMMIT statement to the MySQL server, committing the current transaction.
                self.mydb.commit()
            except Exception as e:
                flag = False
        else:
            flag = False

        return flag

    def getWins(self, userId):
        """
        This method gets the global wins amount of a user
        Args:
            self (object): Represents the own object
            userId (str): User id
            mycursor (object): Instantiates objects that can execute operations
            score (int): Amount of wins
            sql (str): A sql scrypt
            myresult (tuple): Data extracted from the database
        Returns:
            Wins amount
        """
        # The MySQLCursor class instantiates objects that can execute operations such as SQL statements.
        # Cursor objects interact with the MySQL server using a MySQLConnection object.
        mycursor = self.mydb.cursor()
        # Load enviroment variables
        load_dotenv()
        score = -1

        if (self.findUser(str(userId), mycursor)):
            sql = "SELECT \
                globalWins \
                FROM `{}`.`Users` \
                WHERE idUsers = {}".format(str(os.getenv('DB')), str(userId))

            # This method executes the given database operation (query or command).
            mycursor.execute(sql)

            # This method retrieves the next row of a query result set and returns a single sequence,
            # or None if no more rows are available.
            myresult = mycursor.fetchone()

            score = int(myresult[0])

        return score
