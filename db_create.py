import MySQLdb


from app import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


def create_schema():
    server_db = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
    )
    try:
        cursor = server_db.cursor()
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        finally:
            cursor.close()
    finally:
        server_db.close()

    db = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
    )
    try:
        cursor = db.cursor()
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS urls (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    short_code VARCHAR(10) NOT NULL UNIQUE,
                    long_url TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    click_count INT NOT NULL DEFAULT 0
                )
                """
            )
        finally:
            cursor.close()
    finally:
        db.close()

    print(f"Database '{DB_NAME}' and table 'urls' are ready.")


if __name__ == "__main__":
    create_schema()
