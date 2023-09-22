from config.database import db
from models.model import Store, Report
from times.calcu import compute_uptime

def generate_report(report_id):
    # Create new report object and add it to the database
    report = Report(report_id=report_id, status='Running', data='')
    db.session.add(report)
    db.session.commit()

    # Generate report data
    report_data = []
    stores = Store.query.all()
    for store in stores:
        uptime, downtime = compute_uptime(store.id)
        report_data.append({
            'store_id': store.id,
            'status': store.status,
            'uptime': round(uptime, 2),
            'downtime': round(downtime, 2)
        })