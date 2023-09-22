from datetime import datetime, timedelta

status_data = [
    {"store_id": 7359316090119129836, "status": "inactive", "timestamp_utc": "2023-09-21 15:02:18.388606 UTC"},
    {"store_id": 7359316090119129836, "status": "active", "timestamp_utc": "2023-09-21 18:00:18.388606 UTC"},
    {"store_id": 7359316090119129836, "status": "active", "timestamp_utc": "2023-09-21 19:02:18.388606 UTC"},
    {"store_id": 7359316090119129836, "status": "inactive", "timestamp_utc": "2023-09-21 20:00:18.388606 UTC"},

    {"store_id": 7359316090119129837, "status": "active", "timestamp_utc": "2023-09-21 14:02:18.388606 UTC"},
    {"store_id": 7359316090119129837, "status": "inactive", "timestamp_utc": "2023-09-21 18:00:18.388606 UTC"},
    {"store_id": 7359316090119129837, "status": "active", "timestamp_utc": "2023-09-21 19:02:18.388606 UTC"},
    {"store_id": 7359316090119129837, "status": "inactive", "timestamp_utc": "2023-09-21 20:00:18.388606 UTC"},
]

for store_id in set(data['store_id'] for data in status_data):
    store_data = [data for data in status_data if data['store_id'] == store_id]

    # Specify start_time and end_time for each store_id (you can customize this
    if store_id == 7359316090119129836:
        start_time = "10:00:00"
        end_time = "20:59:59"
    elif store_id == 7359316090119129837:
        start_time = "10:00:00"
        end_time = "20:59:59"
    else:
      
        start_time = "10:00:00"
        end_time = "20:59:59"

    # Initialize variables
    today = datetime.now().date()
    start_datetime = datetime.combine(today, datetime.strptime(start_time, "%H:%M:%S").time())
    end_datetime = datetime.combine(today, datetime.strptime(end_time, "%H:%M:%S").time())
    currDayUptime = timedelta()
    lastHourUptime = timedelta()
    prevTimestamp = start_datetime

    # varible for Hours
    currentTime = datetime.combine(today, datetime.strptime(start_time, "%H:%M:%S").time())   #current_datetime = datetime.datetime.now()
    oneHourBackTime = new_datetime = datetime.datetime.now() - datetime.timedelta(hours=1)

    isPrevStateInactive = True

    # Loop through the status data for the current store_id
    for data in store_data:
        observationTime = datetime.strptime(data['timestamp_utc'], "%Y-%m-%d %H:%M:%S.%f UTC")
        status = data['status']

        # Check if the timestamp is within the specified time range
        if start_datetime <= observationTime <= end_datetime:
            if status == 'active' and isPrevStateInactive is True:
                # Found an active status, update start_timestamp
                prevTimestamp = observationTime
                isPrevStateInactive = False

            elif status == 'active':
                currDayUptime += observationTime - prevTimestamp
                prevTimestamp = observationTime

            elif status == 'inactive' and prevTimestamp:
                # Found an inactive status, calculate uptime and reset start_timestamp
                currDayUptime += observationTime - prevTimestamp
                prevTimestamp = None
                isPrevStateInactive = True

        #for Last Hour
        isPrevStateInactive = True
        if oneHourBackTime <= observationTime <= currentTime:
            if status == 'active' and isPrevStateInactive is True:
                # Found an active status, update prevTimestamp
                prevTimestamp = observationTime
                isPrevStateInactive = False

            elif status == 'active':
                lastHourUptime += observationTime - prevTimestamp
                prevTimestamp = observationTime

            elif status == 'inactive' and prevTimestamp:
                # Found an inactive status, calculate uptime and reset prevTimestamp
                lastHourUptime += observationTime - prevTimestamp
                prevTimestamp = None
                isPrevStateInactive = True

    # Calculate downtime by subtracting uptime from the total time range
    currDayUptimeStr = f"{int(currDayUptime.total_seconds() // 3600)}:{int((currDayUptime.total_seconds() % 3600) // 60):02d}"
    LastHourUptimeStr = f"{int(lastHourUptime.total_seconds() // 3600)}:{int((lastHourUptime.total_seconds() % 3600) // 60):02d}"

    currDayDownTimeStr = f"{int(((end_datetime - start_datetime - currDayUptime).total_seconds() // 3600))}:{int(((end_datetime - start_datetime - currDayUptime).total_seconds() % 3600) // 60):02d}"
    LastHourDownTimeStr = f"{int(((end_datetime - start_datetime - lastHourUptime).total_seconds() // 3600))}:{int(((end_datetime - start_datetime - lastHourUptime).total_seconds() % 3600) // 60):02d}"

    # Create a dictionary to store uptime and downtime for each store_id
    upTimeDownTimeDict = {}
    # Store uptime and downtime in the dictionary
    upTimeDownTimeDict[store_id] = {"day": today, "uptime(timedelta)": currDayUptimeStr, "downtime": currDayDownTimeStr}# last week, last day
    # last hour
# Output results for all store_ids
for store_id, data in upTimeDownTimeDict.items():
    print(f"Store ID: {store_id}")
    print(f"Uptime: {data['uptime']} (hh:mm)")
    print(f"Downtime: {data['downtime']} (hh:mm)")


# lastweek
{   
    "storeId":
}
# last day

# store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours)

