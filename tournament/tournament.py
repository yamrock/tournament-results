#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    #print "TEST"
    DB = connect()
    c = DB.cursor()
    c.execute('''UPDATE standings SET matches = NULL, wins = NULL ''')
    c.connection.commit()
    DB.close


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute('''DELETE from standings ''')
    c.connection.commit()
    DB.close


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute('''SELECT COUNT(name) from standings''')
    row = c.fetchall()
    count = int(row[0][0])
    DB.close()
    return count



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    #print name 
    DB = connect()
    c = DB.cursor()
    c.execute("""INSERT into standings (name, matches, wins) VALUES (%s, %s, %s);""" , (name, "0", "0"))
    c.connection.commit()
    DB.close


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute('''SELECT * from standings ORDER BY wins desc''')
    rows = c.fetchall()
    results = [row for row in rows]
    #for row in rows:
    return results
    DB.close()



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute('''SELECT id,matches,wins from standings WHERE id = %s OR id = %s''' % (winner, loser))
    rows = c.fetchall()
    #print rows
    winner_matches = rows[0][1] + 1 
    loser_matches = rows[1][1] + 1
    winner_wins = rows[0][2] + 1


    c.execute("""UPDATE standings SET matches = %s, wins = %s where id = %s""", (winner_matches, winner_wins, winner))
    c.execute("""UPDATE standings SET matches = %s where id = %s""", (loser_matches, loser))
    c.connection.commit()
    DB.close()

    #c.execute("""UPDATE standings SET matches = """
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    result = []
    DB = connect()
    c = DB.cursor()
    c.execute('''SELECT id, name from standings ORDER BY wins desc''')
    rows = c.fetchall()
    #results = [row for row in rows]
    #print rows
    ''' Since there are an even number of players, we can take pairs of them at a time 
        and append it to the results. This will always ensure that unique set of players 
        are returned in the result set.
    '''
    for i in range(0, len(rows), 2):
        result.append(rows[i] + rows[i + 1])

    return result
    DB.close()


