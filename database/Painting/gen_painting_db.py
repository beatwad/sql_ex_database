import random
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def generate_random_data(num_squares=100, num_sprays=100, num_paint_events=500):
    root = ET.Element("painting")
    
    # Generate utQ (Squares)
    utq = ET.SubElement(root, "utq")
    squares = []
    for i in range(-num_squares//2, num_squares//2 + 1):
        row = ET.SubElement(utq, "row")
        q_id = ET.SubElement(row, "q_id")
        q_id.text = str(i)
        q_name = ET.SubElement(row, "q_name")
        q_name.text = f"Square {i}"
        squares.append(i)
    
    # Generate utV (Spray Cans)
    utv = ET.SubElement(root, "utv")
    colors = ['R', 'G', 'B']
    sprays = []
    for i in range(-num_sprays//2, num_sprays//2 + 1):
        row = ET.SubElement(utv, "row")
        v_id = ET.SubElement(row, "v_id")
        v_id.text = str(i)
        v_name = ET.SubElement(row, "v_name")
        v_name.text = f"Balloon {i}"
        v_color = ET.SubElement(row, "v_color")
        color = random.choice(colors)
        v_color.text = color
        sprays.append((i, color))
    
    # Generate utB (Painting Events)
    utb = ET.SubElement(root, "utb")
    start_time = datetime(2000, 1, 1, 1, 0, 0)
    
    for _ in range(num_paint_events):
        row = ET.SubElement(utb, "row")
        b_datetime = ET.SubElement(row, "b_datetime")
        event_time = start_time + timedelta(seconds=random.randint(1, 600))
        b_datetime.text = event_time.strftime("%Y-%m-%d %H:%M:%S.000")
        
        b_q_id = ET.SubElement(row, "b_q_id")
        square = random.choice(squares)
        b_q_id.text = str(square)
        
        b_v_id = ET.SubElement(row, "b_v_id")
        spray_id, _ = random.choice(sprays)
        b_v_id.text = str(spray_id)
        
        b_vol = ET.SubElement(row, "b_vol")
        volume = random.randint(1, 255)
        b_vol.text = str(volume)
    
    # Save to file
    tree = ET.ElementTree(root)
    with open("random_painting_data.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    
    print("XML file 'random_painting_data.xml' generated successfully.")

if __name__ == "__main__":
    generate_random_data()
