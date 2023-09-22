import os
from fastapi import APIRouter
import pandas as pd
# from config.database import db
# from models.model import Report

service = APIRouter()

# Specify the directory containing your CSV files
csv_directory = "D:\project\store_managment/ip"

batch_size = 5000


def extract_and_join_data():
    # Initialize DataFrames to store data from CSV files
    df_store_status = pd.DataFrame()
    df_menu_hours = pd.DataFrame()
    df_area = pd.DataFrame()

    # Loop through the CSV files in the specified directory
    for filename in os.listdir(csv_directory):
        print("start the loop")
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(csv_directory, filename)
            print("completed joint")
            # Read the CSV file using pandas with chunking
            chunks = pd.read_csv(csv_file_path, chunksize=batch_size)
            print("completed reding with chunk")
            # Process and concatenate data from each chunk into respective DataFrames
            for chunk in chunks:
                if "storeStatus.csv" in filename:
                    df_store_status = pd.concat([df_store_status, chunk.head(10)], ignore_index=True)
                elif "MenuHours.csv" in filename:
                    df_menu_hours = pd.concat([df_menu_hours, chunk.head(10)], ignore_index=True)
                elif "area.csv" in filename:
                    df_area = pd.concat([df_area, chunk.head(10)], ignore_index=True)

    print("store_status columns:", df_store_status.columns)
    print("menu_hours columns:", df_menu_hours.columns)
    print("area columns:", df_area.columns)
    print("end the function")
    print(csv_directory)


    # Perform a join operation based on common keys (adjust this as needed)
    merged_data = pd.merge(df_store_status, df_menu_hours, on="store_id", how="inner")

    # Convert the merged DataFrame to a list of dictionaries
    data = merged_data.head(100).to_dict(orient="records")
    merged_data = pd.merge(merged_data, df_area, on="store_id", how="inner")
    return data


@service.get("/trigger_report")
async def fetch_csv_data():
    try:
        data = extract_and_join_data()

        # # Set up MongoDB Atlas connection
        # client = MongoClient("mongodb+srv://sambhardiya:Sammongodb@cluster0.b6yirc1.mongodb.net/?retryWrites=true&w=majority")

        # # Access a specific database
        # db = client.storeDb  

        # # Access a specific collection within the database
        # collection_name = db["report"]

        # # Insert the data into MongoDB Atlas
        # collection_name.insert_many(data)

        # # Return a success message or response
        return data
    except Exception as e:
        return {"error": str(e)}

# @service.post("/push_data")
# async def fetch_csv_data():
#      try:
#          # Access a specific collection within the database
#         collection = db["reports"]  
#                         # Create a Report instance
#         report_data = {
#             "report_id": "report123",
#             "business_hours": [
#                 {"store_id": "store1", "day_of_week": 1, "start_time_local": "09:00", "end_time_local": "17:00"},
#                 {"store_id": "store2", "day_of_week": 2, "start_time_local": "10:00", "end_time_local": "18:00"},
#             ],
#             "timezones": [
#                 {"store_id": "store1", "timezone_str": "America/New_York"},
#                 {"store_id": "store2", "timezone_str": "America/Los_Angeles"},
#             ]
#         }

#         report = Report(**report_data)

#         # Serialize the Report instance to a dictionary
#         report_dict = report.dict()

#         # Insert the serialized document into the MongoDB collection
#         collection.insert_one(report_dict)


#      except Exception as e:
#         return {"error": str(e)}


