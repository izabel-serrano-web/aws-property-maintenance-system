#!/bin/bash
set -e

APP_DIR="/opt/pms"

dnf update -y || yum update -y
dnf install -y git python3 python3-pip || yum install -y git python3 python3-pip

mkdir -p $APP_DIR
cd $APP_DIR

# In real deployment, you would either git clone your repo
# or copy the application files here during provisioning.

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install Flask==3.0.2 Flask-SQLAlchemy==3.1.1 PyMySQL==1.1.0 cryptography==42.0.5 python-dotenv==1.0.1

cat > /etc/systemd/system/pms.service <<EOF
[Unit]
Description=Property Maintenance System
After=network.target

[Service]
User=root
WorkingDirectory=$APP_DIR/app
Environment="DATABASE_URL=REPLACE_WITH_DATABASE_URL"
Environment="SECRET_KEY=REPLACE_WITH_SECRET_KEY"
ExecStart=$APP_DIR/venv/bin/python $APP_DIR/app/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable pms.service
systemctl start pms.service