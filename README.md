
# URL Shortener - Flask Project

## Run with SQLite

SQLite is included with Python, so no separate database server is needed. The app creates `url_shortener.db` and its `urls` table automatically the first time it starts.
python 10
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start the SQLite version:
```
python appsqllite.py
```

Visit http://localhost:5000

## Deploy to an Ubuntu EC2 instance

The GitHub Actions workflow deploys the MySQL version when code is pushed to `main`. It updates the checkout, creates a Python virtual environment, installs dependencies, runs `db_create.py`, and restarts the app as a systemd service using Gunicorn.

### One-time EC2 setup

Connect to the Ubuntu instance and install the system packages needed by Python and the MySQL driver:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv python3-dev \
  default-libmysqlclient-dev build-essential pkg-config
```

The EC2 login user must be able to run `sudo systemctl` without an interactive password prompt (the default `ubuntu` user on standard Ubuntu EC2 images can do this).

In the EC2 security group, allow inbound TCP port `5000` from the addresses that should reach the app. The app will be available at `http://<EC2-public-IP>:5000`. For a public production website, put a reverse proxy such as Nginx with HTTPS in front of the app rather than exposing port `5000` directly.

Ensure the EC2 instance can connect to the MySQL server on port `3306`. Prefer allowing the EC2 security group in the database security group's inbound rules instead of exposing MySQL publicly.

### GitHub repository secrets

In **Settings → Secrets and variables → Actions**, add:

- `EC2_HOST`: the EC2 public DNS name or IP address.
- `EC2_USER`: the SSH login user (usually `ubuntu`).
- `EC2_SSH_KEY`: the private SSH key for that EC2 instance.
- `EC2_KNOWN_HOSTS`: the EC2 SSH host-key entry for `EC2_HOST`. Obtain it with `ssh-keyscan -H -t ed25519 <EC2_HOST>` and verify the fingerprint through a trusted channel before saving it.

After adding the secrets, push a commit to `main` or run **Deploy to EC2** from the GitHub Actions tab. The workflow creates the app directory under the SSH user's home directory and manages it with the `url-shortener` systemd service.

> The MySQL credentials in `app.py` must be valid on EC2. Rotate any password that has been committed or shared, and move database credentials into environment-based configuration before using this as a public production deployment.

## Run with MySQL

1. Configure the MySQL connection details in `app.py`.

2. Create the database and table if they do not already exist:
```
python db_create.py
```

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
