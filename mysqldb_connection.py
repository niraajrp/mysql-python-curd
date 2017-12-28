from mysql.connector import MySQLConnection, Error
import database_config


def connect():
    """ Connect to MySQL database """

    db_config = database_config.read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')
        pass
    return conn


if __name__ == '__main__':
    connect()
    pass

