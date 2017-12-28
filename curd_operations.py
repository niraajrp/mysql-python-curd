from mysql.connector import MySQLConnection, Error
import database_config

db_config = database_config.read_db_config()


def view():
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tweets_table")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def insert_tweets(tweets):
    query = "INSERT INTO tweets_table(username,tweet,date_created) " \
            "VALUES(%s,%s,%s)"

    try:
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, (tweets,))

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as e:
        print('Error:', e)


def update_tweets(username, tweets, date_created, id):
    query = """ UPDATE tweets_table
                SET username=%s, tweet=%s, date_created=%s
                WHERE id=%s """
    data = (username, tweets, date_created, id)
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
    except Error as error:
        print(error)


def delete_tweets(id_no):
    query = "DELETE FROM tweets_table WHERE id = %s"
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (id_no,))
        conn.commit()
    except Error as error:
        print(error)


if __name__ == '__main__':
    view()

    add = input("Do you want to Add new entries? Press y for YES and any other key for NO \n")
    if (add == 'y'):
        username = input("Enter username \n")
        tweet = input("Enter correspondig tweet \n")
        date_created = input("Enter the date when the tweet was created \n")
        tweets = [username, tweet, date_created]
        insert_tweets(tweets)

    val = input("Do you want to update? Press y for YES and any other key for NO \n")
    if (val == 'y'):
        id_no = input("Enter id number that you want to update \n")
        username = input("Enter the new username \n")
        tweet = input("Enter new edited tweet \n")
        date_created = input("Enter the date when the tweet was created \n")
        update_tweets(username, tweet, date_created, id_no)

    temp = input("Do you want to delete any entry? Press y for YES and any other key for NO \n")
    if (temp == 'y'):
        id = input("Enter the id number of entry that you want to delete \n")
        delete_tweets(id)

    view()

