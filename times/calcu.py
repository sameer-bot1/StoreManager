from datetime import datetime, timedelta
import pytz
from models.model import Store, BusinessHours, Timezone




# get timezone 
def get_store_timezone(store_id):
    timezone = Timezone.query.filter_by(store_id=store_id).first()
    if timezone is None:
        # Return a default timezone here, e.g. UTC
        return pytz.timezone('UTC')
    return pytz.timezone(timezone.timezone_str)


# get business hours
def get_store_business_hours(store_id):
    business_hours = BusinessHours.query.filter_by(store_id=store_id).all()
    return [(bh.day_of_week, bh.start_time_local, bh.end_time_local) for bh in business_hours]



# calculate uptime
def calculate_uptime(status_data, store_ids, date, default_start_times, default_end_times):
    uptime_results = {}
    
    for store_id in store_ids:
        # Initialize variables to track uptime and start time
        uptime = timedelta()
        start_time = default_start_times.get(store_id, {}).get(date, None)

        # Iterate through the status data
        for index, row in status_data.iterrows():
            timestamp = row['timestamp_utc']
            status = row['status']

            if timestamp >= default_start_times.get(store_id, {}).get(date, None) and timestamp < default_end_times.get(store_id, {}).get(date, None):
                if status == 'active':
                    # Found active status, update start_time
                    start_time = timestamp
                elif status == 'inactive':
                    # Found inactive status, calculate uptime and reset start_time
                    if start_time is not None:
                        uptime += timestamp - start_time
                    start_time = None

        # Check if there's an active status at the end of the time range
        if start_time is not None:
            uptime += default_end_times.get(store_id, {}).get(date, None) - start_time

        uptime_results[store_id] = uptime

    return uptime_results

