import os
import csv
from collections import defaultdict

# Helper function to calculate seasonal averages
def calculate_seasonal_averages(temperature_data):
    seasonal_months = {
        "Summer": [12, 1, 2],  # December, January, February
        "Autumn": [3, 4, 5],   # March, April, May
        "Winter": [6, 7, 8],   # June, July, August
        "Spring": [9, 10, 11]  # September, October, November
    }

    seasonal_averages = defaultdict(list)

    for station, yearly_data in temperature_data.items():
        for month_data in yearly_data:
            for season, months in seasonal_months.items():
                season_temps = [month_data[month - 1] for month in months]
                seasonal_averages[season].extend(season_temps)

    seasonal_avg = {season: sum(temps) / len(temps) for season, temps in seasonal_averages.items()}
    return seasonal_avg

# Helper function to calculate temperature range for each station
def calculate_temp_range(temperature_data):
    temp_ranges = {}
    for station, yearly_data in temperature_data.items():
        all_monthly_data = [temp for month_data in yearly_data for temp in month_data]
        temp_range = max(all_monthly_data) - min(all_monthly_data)
        temp_ranges[station] = temp_range
    return temp_ranges

# Helper function to find warmest and coolest stations
def find_extreme_stations(temperature_data):
    warmest_temp = -float('inf')
    coolest_temp = float('inf')
    warmest_stations = []
    coolest_stations = []

    for station, yearly_data in temperature_data.items():
        all_monthly_data = [temp for month_data in yearly_data for temp in month_data]
        max_temp = max(all_monthly_data)
        min_temp = min(all_monthly_data)
        
        if max_temp > warmest_temp:
            warmest_temp = max_temp
            warmest_stations = [station]
        elif max_temp == warmest_temp:
            warmest_stations.append(station)

        if min_temp < coolest_temp:
            coolest_temp = min_temp
            coolest_stations = [station]
        elif min_temp == coolest_temp:
            coolest_stations.append(station)

    return warmest_stations, coolest_stations

# Main function to process all CSV files
def process_temperature_data(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    temperature_data = defaultdict(list)

    # Read all CSV files in the folder
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            
            # Extract the year from the file name (assuming the format 'stations_group_YYYY.csv')
            year = filename.split('_')[-1].split('.')[0]
            print(f"Processing file for year: {year}")

            with open(filepath, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header

                for row in reader:
                    station = row[0]  # Station Name
                    monthly_temps = list(map(float, row[4:]))  # Monthly temperatures (Jan-Dec)

                    # Add monthly data to the temperature_data dictionary
                    if station not in temperature_data:
                        temperature_data[station] = []

                    temperature_data[station].append(monthly_temps)

    # Proceed with calculations if the data was successfully read
    if temperature_data:
        print("Writing results to files...")

        # Specify a full path to save files
        output_directory = r'C:\\Users\dharm\OneDrive\Desktop\Assesment2_q2\\result'  # Modify this path if needed

        # Ensure the output directory exists, if not, create it
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        seasonal_averages = calculate_seasonal_averages(temperature_data)
        with open(os.path.join(output_directory, "average_temp.txt"), "w") as f:
            for season, avg_temp in seasonal_averages.items():
                f.write(f"{season}: {avg_temp:.2f}\n")

        # Find station with largest temperature range
        temp_ranges = calculate_temp_range(temperature_data)
        max_range = max(temp_ranges.values())
        largest_temp_range_stations = [station for station, temp_range in temp_ranges.items() if temp_range == max_range]
        with open(os.path.join(output_directory, "largest_temp_range_station.txt"), "w") as f:
            f.write(f"Stations with the largest temperature range ({max_range}°C):\n")
            for station in largest_temp_range_stations:
                f.write(f"{station}\n")

        # Find warmest and coolest stations
        warmest_stations, coolest_stations = find_extreme_stations(temperature_data)
        with open(os.path.join(output_directory, "warmest_and_coolest_station.txt"), "w") as f:
            f.write(f"Warmest stations:\n")
            for station in warmest_stations:
                f.write(f"{station}\n")
            f.write(f"\nCoolest stations:\n")
            for station in coolest_stations:
                f.write(f"{station}\n")

    else:
        print("No data found in the folder.")

# Set the directory path directly in the script
directory = r'C:\\Users\dharm\OneDrive\Desktop\Assesment2_q2\\temperature_data'  # Change this to your actual path

# Run the process with the specified folder path
process_temperature_data(directory)