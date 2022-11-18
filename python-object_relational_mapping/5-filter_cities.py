#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name=%s\
        ORDER BY cities.id ASC", (argv[4],)
    )
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
    