import serial
import csv
import time

# Set up serial connection (adjust the port and baud rate)
ser = serial.Serial('COM6', 9600)
headings = ["Treatment", "Timestamp", "MQ2", "MQ3", "MQ4", "MQ5", "MQ6", "MQ7", "MQ8", "MQ9", "MQ135"]


def sampling(treatment, duration, wait):
    print(f"Wait for {wait} seconds before sampling...")
    count = 0
    for t in range(wait):
        time.sleep(1)
        print(f"{wait - count} seconds left")
        count += 1
    # Open a CSV file to store the data
    with open(f'{treatment}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headings)
        start_time = time.time()
        preheating = 0
        try:
            while time.time() - start_time < (duration + 1):
                if ser.in_waiting > 0:
                    line = ser.readline()
                    try:
                        if (time.time() - start_time) > 1:
                            # Attempt to decode
                            decoded_line = line.decode('utf-8').rstrip()
                            data = decoded_line.split(",")  # Split data by comma for CSV columns
                            data.insert(0, treatment)
                            data.insert(1, int(time.time()))
                            status = ""
                            remaining_measure_time = int(duration - (time.time() - start_time))
                            if int(data[7]) > 3700:
                                preheating += 1
                                duration += 1
                                status += f"Status: Pre-heating...({preheating})"
                            else:
                                status += f"Status: Time remaining for measurement = {remaining_measure_time} seconds"

                            print(data, status)
                            writer.writerow(data)  # Write split data to CSV file
                    except UnicodeDecodeError:
                        # Handle non-decodable data
                        print("UnicodeDecodeError - raw data:", line)
                        writer.writerow([line])  # Write raw data to CSV file

        finally:
            ser.close()
            print("Serial connection closed")


# Example usage
sampling("D", 100, 0)  # Sample for 10 seconds
