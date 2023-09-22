import os
from fastapi import FastAPI
import pandas as pd
import uvicorn
from routes.route import user
from fileM.run import service

app = FastAPI(title= "upload any file heraae")

app.include_router(service)

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1",port=5049, reload=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}



# # Specify the directory containing your CSV files
# csv_directory = "D:\project\store_managment/ip"

# batch_size = 2

# @app.get("/fetch_csv_data")
# async def fetch_csv_data():
#     try:
#         print("In try block")
#         # Initialize an empty DataFrame to store combined data
#         combined_data = pd.DataFrame()

#         # Loop through the CSV files in the specified directory
#         for filename in os.listdir(csv_directory):
#             print("In the for loop")
#             if filename.endswith(".csv"):
#                 csv_file_path = os.path.join(csv_directory, filename)

#                 # Read the CSV file using pandas with chunking
#                 chunks = pd.read_csv(csv_file_path, chunksize=batch_size)

#                 # Process and append each chunk to the combined DataFrame
#                 for chunk in chunks:
#                     combined_data = pd.concat([combined_data, chunk], ignore_index=True)

#         # Fetch the first 20 rows from the combined DataFrame
#         data = combined_data.head(20).to_dict(orient="records")

#         return data
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return {"error": str(e)}


# @app.get("/trigger_report")
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

