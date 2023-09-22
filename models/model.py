from typing import List
from pydantic import BaseModel

# class Store(BaseModel):
#     store_id: str
#     timestamp_utc: int
#     status: str

class BusinessHours(BaseModel):
    store_id: str
    day_of_week: int
    start_time_local: str
    end_time_local: str

class Timezone(BaseModel):
    store_id: str
    timezone_str: str


class Report(BaseModel):
    report_id: str
    business_hours: List[BusinessHours]
    # store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours)
    
    def to_dict(self):
        return {
            'id': self.id,
            'report_id': self.report_id,
            'status': self.status,
            'created_at': self.created_at.isoformat() + 'Z',
            'completed_at': self.completed_at.isoformat() + 'Z' if self.completed_at else None
        }
    
