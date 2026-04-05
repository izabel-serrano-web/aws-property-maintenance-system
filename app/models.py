from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MaintenanceRequest(db.Model):
    __tablename__ = "maintenance_requests"

    id = db.Column(db.Integer, primary_key=True)
    tenant_name = db.Column(db.String(100), nullable=False)
    unit_number = db.Column(db.String(20), nullable=False)
    building_name = db.Column(db.String(100), nullable=False)
    issue_category = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    preferred_visit_date = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Open")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
