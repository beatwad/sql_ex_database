import xml.etree.ElementTree as ET
import random
import string
from datetime import datetime, timedelta

def random_name():
    first_names = ["Alex", "John", "Emily", "Bruce", "Sarah", "Michael", "Jessica", "David", "Laura", "Robert"]
    last_names = ["Merser", "Willis", "Johnson", "Smith", "Brown", "Taylor", "Anderson", "White", "Harris", "Clark"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_plane():
    return random.choice(["Boeing", "Airbus", "Suckhoy", "Embraer", "Tupolev"])

def random_city():
    return random.choice(["Moscow", "New York", "London", "Paris", "Berlin", "Tokyo", "Beijing", "Dubai", "Madrid", "Rome"])

def random_seat():
    return f"{random.randint(1, 30)}{random.choice(['a', 'b', 'c', 'd'])}"

def generate_data():
    root = ET.Element("aero")
    
    company = ET.SubElement(root, "company")
    passenger = ET.SubElement(root, "passenger")
    trip = ET.SubElement(root, "trip")
    pass_in_trip = ET.SubElement(root, "pass_in_trip")
    
    # Generate companies
    companies = []
    for i in range(1, 6):
        companies.append(i)
        row = ET.SubElement(company, "row")
        ET.SubElement(row, "id_comp").text = str(i)
        ET.SubElement(row, "name").text = f"Company {i}"
    
    # Generate passengers
    passengers = []
    for i in range(1, 11):
        passengers.append(i)
        row = ET.SubElement(passenger, "row")
        ET.SubElement(row, "id_psg").text = str(i)
        ET.SubElement(row, "name").text = random_name()
    
    # Generate trips
    trips = []
    for i in range(1, 11):
        trips.append(i)
        row = ET.SubElement(trip, "row")
        ET.SubElement(row, "trip_no").text = str(i)
        ET.SubElement(row, "id_comp").text = str(random.choice(companies))
        ET.SubElement(row, "plane").text = random_plane()
        town_from = random_city()
        town_to = random_city()
        while town_from == town_to:
            town_to = random_city()
        ET.SubElement(row, "town_from").text = town_from
        ET.SubElement(row, "town_to").text = town_to
        time_out = datetime(1900, 1, 1, random.randint(0, 23), random.randint(0, 59))
        time_in = time_out + timedelta(hours=random.randint(1, 5))
        ET.SubElement(row, "time_out").text = time_out.strftime("%Y-%m-%d %H:%M:%S.000")
        ET.SubElement(row, "time_in").text = time_in.strftime("%Y-%m-%d %H:%M:%S.000")
    
    # Generate pass_in_trip
    for _ in range(20):
        row = ET.SubElement(pass_in_trip, "row")
        ET.SubElement(row, "trip_no").text = str(random.choice(trips))
        date = datetime(2003, random.randint(1, 12), random.randint(1, 28))
        ET.SubElement(row, "date").text = date.strftime("%Y-%m-%d %H:%M:%S.000")
        ET.SubElement(row, "id_psg").text = str(random.choice(passengers))
        ET.SubElement(row, "place").text = random_seat()
    
    tree = ET.ElementTree(root)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)
    print("XML file generated as output.xml")

if __name__ == "__main__":
    generate_data()
