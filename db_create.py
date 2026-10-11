import MySQLdb

try:
    # Connect without specifying a database name
    db = MySQLdb.connect(
        host="url-shortner-db.c63qmyk8488n.us-east-1.rds.amazonaws.com",
        user="root",  # your RDS master username
        passwd="12345678"
    )
    cursor = db.cursor()

    # Create the database schema
    cursor.execute("CREATE DATABASE url_shortener_db;")
    print("Database 'url_shortener_db' created successfully!")

    db.close()
except Exception as e:
    print("Error:", e)
