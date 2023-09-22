import os
from fastapi import APIRouter
import pandas as pd

user = APIRouter()


































# # Specify the directory containing your CSV files
# csv_directory = "D:\project\store_managment/ip"

# batch_size = 5000

# def extract_and_join_data():
#     # Initialize DataFrames to store data from CSV files
#     df_store_status = pd.DataFrame()
#     df_menu_hours = pd.DataFrame()
#     df_area = pd.DataFrame()

#     # Loop through the CSV files in the specified directory
#     for filename in os.listdir(csv_directory):
#         print("start the loop")
#         if filename.endswith(".csv"):
#             csv_file_path = os.path.join(csv_directory, filename)
#             print("completed joint")
#             # Read the CSV file using pandas with chunking
#             chunks = pd.read_csv(csv_file_path, chunksize=batch_size)
#             print("completed reding with chunk")
#             # Process and concatenate data from each chunk into respective DataFrames
#             for chunk in chunks:
#                 if "storeStatus.csv" in filename:
#                     df_store_status = pd.concat([df_store_status, chunk.head(10)], ignore_index=True)
#                 elif "MenuHours.csv" in filename:
#                     df_menu_hours = pd.concat([df_menu_hours, chunk.head(10)], ignore_index=True)
#                 elif "area.csv" in filename:
#                     df_area = pd.concat([df_area, chunk.head(10)], ignore_index=True)

#     print("store_status columns:", df_store_status.columns)
#     print("menu_hours columns:", df_menu_hours.columns)
#     print("area columns:", df_area.columns)
#     print("end the function")
#     print(csv_directory)


#     # Perform a join operation based on common keys (adjust this as needed)
#     merged_data = pd.merge(df_store_status, df_menu_hours, on="store_id", how="inner")

#     # Convert the merged DataFrame to a list of dictionaries
#     data = merged_data.head(100).to_dict(orient="records")
#     merged_data = pd.merge(merged_data, df_area, on="store_id", how="inner")
#     return data

# @user.get("/trigger_report")
# async def fetch_csv_data():
#     print("in the trigger")

#     try:
#         # csv_file_path = "ip/storeStatus.csv"
#         # print('csv file path',csv_file_path)

#         # df = pd.read_csv(csv_file_path)
#         # print("Data from CSV File 1:")
#         # print(df.head(1))

#         # Extract and join data from CSV files
#         data = extract_and_join_data()

#         return data
#     except Exception as e:
#         return {"error": str(e)}

# @user.get("/trigger_report")
# # funtion hit karenge report generation ka 
# async def fetch_csv_data():
# #     # Specify the path to your CSV file
#     csv_file_path = "ip/storeStatus.csv"
#     csv_file_path2 = "ip/MenuHours.csv"
#     csv_file_path3 = "ip/area.csv"


#     try:
#         # Read the CSV file using pandas
#         df = pd.read_csv(csv_file_path)
#         df2 = pd.read_csv(csv_file_path2)
#         df3 = pd.read_csv(csv_file_path3)

        
#         # Convert the DataFrame to a list of dictionaries
#         data = df.head(100).to_dict(orient="records")
#         data2 = df2.head(100).to_dict(orient="records")
#         data3 = df3.head(100).to_dict(orient="records")



#         return data, data2, data3
#     except Exception as e:
#         return {"error": str(e)}


# Endpoint to trigger report generation
# @app.get("/trigger_report")
# async def fetch_csv_data():
# #     # Specify the path to your CSV file
#     csv_file_path = "storeStatus.csv"

#     try:
#         # Read the CSV file using pandas
#         df = pd.read_csv(csv_file_path)
#         # Convert the DataFrame to a list of dictionaries
#         data = df.head(1).to_dict(orient="records")

#         return data
#     except Exception as e:
#         return {"error": str(e)}
    
    
    # store_collection = db["stores"]
    # business_hours_collection = db["business_hours"]
    # timezone_collection = db["timezones"]


    # store_collection.insert_many([store.model_dump() for store in store_data])
    # business_hours_collection.insert_many([hours.model_dump() for hours in business_hours_data])
    # timezone_collection.insert_many([tz.model_dump() for tz in timezone_data])
