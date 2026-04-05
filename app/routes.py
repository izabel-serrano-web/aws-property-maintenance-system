from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, MaintenanceRequest
from datetime import datetime

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_request = MaintenanceRequest(
            tenant_name=request.form.get("tenant_name"),
            unit_number=request.form.get("unit_number"),
            building_name=request.form.get("building_name"),
            issue_category=request.form.get("issue_category"),
            priority=request.form.get("priority"),
            description=request.form.get("description"),
            preferred_visit_date=request.form.get("preferred_visit_date"),
            status="Open",
            created_at=datetime.utcnow()
        )

        db.session.add(new_request)
        db.session.commit()

        return redirect(url_for("main.dashboard"))

    return render_template("index.html")


@main.route("/dashboard")
def dashboard():
    requests_data = MaintenanceRequest.query.order_by(
        MaintenanceRequest.created_at.desc()
    ).all()

    return render_template("dashboard.html", requests=requests_data)
