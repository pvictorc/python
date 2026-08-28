
# demonstration of IndexError in Python

maintenance_records = ["Record 1", "Record 2", "Record 3"]

def check_ride_maintenance_record(check_record):
    try:
        print(maintenance_records[check_record])
    except IndexError as e:
        print(f"Exception: Index {check_record} is out of range for maintenance records.")


check_ride_maintenance_record(5)  # This will raise an IndexError and be caught by the except block