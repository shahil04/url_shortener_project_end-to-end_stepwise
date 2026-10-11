
# URL Shortener - Flask Project

## Run with SQLite

SQLite is included with Python, so no separate database server is needed. The app creates `url_shortener.db` and its `urls` table automatically the first time it starts.

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start the SQLite version:
```
python appsqllite.py
```

Visit http://localhost:5000

## Run with MySQL

1. Create a MySQL database and table:
```sql
CREATE DATABASE url_db;
USE url_db;
CREATE TABLE urls (
  id INT AUTO_INCREMENT PRIMARY KEY,
  short_code VARCHAR(10) UNIQUE,
  long_url TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  click_count INT DEFAULT 0
);
```

2. Set the MySQL connection details in `app.py`.

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Start the MySQL version:
```
python app.py
```

Visit http://localhost:5000
"# url_shortener_project_end-to-end_stepwise" 
