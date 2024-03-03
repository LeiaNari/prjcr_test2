import csv
from convertor.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from convertor.distance import feet_to_meters, meters_to_feet


def convert_temperature_reading(reading, target_unit):
    try:
        if reading.endswith('°C'):
            celsius = float(reading[:-2])
            return celsius_to_fahrenheit(celsius) if target_unit == 'F' else celsius
        elif reading.endswith('°F'):
            fahrenheit = float(reading[:-2])
            return fahrenheit_to_celsius(fahrenheit) if target_unit == 'C' else fahrenheit
        else:
            return reading
    except ValueError:
        return reading



def convert_distance_reading(reading, target_unit):
    if reading.endswith('ft'):
        feet = float(reading[:-2])
        return feet_to_meters(feet) if target_unit == 'm' else feet
    elif reading.endswith('m'):
        meters = float(reading[:-1])
        return meters_to_feet(meters) if target_unit == 'ft' else meters
    else:
        return reading


def main(input_file, output_file, target_temperature_unit, target_distance_unit):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or ['Date', 'Distance', 'Reading']  # Проверка на случай, если reader.fieldnames возвращает None
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            row['Reading'] = convert_temperature_reading(row['Reading'], target_temperature_unit)
            if 'Distance' in row:
                row['Distance'] = convert_distance_reading(row['Distance'], target_distance_unit)
            writer.writerow(row)


if __name__ == "__main__":
    input_file = "measurements.csv"
    output_file = "converted_measurements.csv"
    target_temperature_unit = 'F'
    target_distance_unit = 'm'  
    main(input_file, output_file, target_temperature_unit, target_distance_unit)
