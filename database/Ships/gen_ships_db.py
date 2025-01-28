import random
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

class_types = ['bb', 'bc']
countries = ['USA', 'DEN', 'JAP', 'UK', 'IT', 'RUS', 'AU', 'BR']
num_classes = 5
num_battles = 5
max_num_ships_in_class = 5
max_num_ships_in_battle = 10

# Генерация случайных данных для Classes
def generate_classes():
    classes = []
    for i in range(1, num_classes):
        country = random.choice(countries)
        class_data = {
            'class': country + ' ' + str(i),
            'type': random.choice(class_types),
            'country': country,
            'numGuns': str(random.randint(4, 12)),
            'bore': str(random.randint(10, 18)),
            'displacement': str(random.randint(20000, 50000))
        }
        classes.append(class_data)
    return classes

# Генерация случайных данных для Ships
def generate_ships(classes):
    ships = []
    for cls in classes:
        for i in range(random.randint(1, max_num_ships_in_class)):
            ship = {
                'name': f"{cls['class']}_{i+1}",
                'class': cls['class'],
                'launched': str(random.randint(1910, 1940))
            }
            ships.append(ship)
    return ships

# Генерация случайных данных для Battles
def generate_battles(num_battles):
    battles = []
    start_date = datetime(1939, 9, 1)
    for i in range(1, num_battles+1):
        date = start_date + timedelta(days=random.randint(0, 365*6))  # между 1939 и 1945
        battle = {
            'name': f"Battle_{i}",
            'date': date.strftime('%Y-%m-%d')
        }
        battles.append(battle)
        start_date = date
    return battles

# Генерация случайных данных для Outcomes
def generate_outcomes(ships, battles):
    outcomes = []
    ships_tmp = ships.copy()
    result_types = ['OK', 'damaged', 'sunk']
    for battle in battles:
        num_ships_in_battle = random.randint(1, max_num_ships_in_battle)
        participating_ships = random.sample(ships_tmp, min(len(ships_tmp), num_ships_in_battle))
        for ship in participating_ships:
            outcome = {
                'ship': ship['name'],
                'battle': battle['name'],
                'result': random.choice(result_types)
            }
            if outcome['result'] == 'sunk':
                ships_tmp.remove(ship)
            outcomes.append(outcome)
    return outcomes

# Конвертация данных в формат XML
def data_to_xml(classes, ships, battles, outcomes):
    root = ET.Element('ships')

    # Создание блока Classes
    classes_element = ET.SubElement(root, 'classes')
    for c in classes:
        row = ET.SubElement(classes_element, 'row')
        for key, value in c.items():
            element = ET.SubElement(row, key)
            element.text = value

    # Создание блока Ships
    ships_element = ET.SubElement(root, 'ships')
    for ship in ships:
        row = ET.SubElement(ships_element, 'row')
        for key, value in ship.items():
            element = ET.SubElement(row, key)
            element.text = value

    # Создание блока Battles
    battles_element = ET.SubElement(root, 'battles')
    for battle in battles:
        row = ET.SubElement(battles_element, 'row')
        for key, value in battle.items():
            element = ET.SubElement(row, key)
            element.text = value

    # Создание блока Outcomes
    outcomes_element = ET.SubElement(root, 'outcomes')
    for outcome in outcomes:
        row = ET.SubElement(outcomes_element, 'row')
        for key, value in outcome.items():
            element = ET.SubElement(row, key)
            element.text = value

    return ET.ElementTree(root)

# Генерация данных
classes = generate_classes()
ships = generate_ships(classes)
battles = generate_battles(num_battles)
outcomes = generate_outcomes(ships, battles)

# Конвертация данных в XML и запись в файл
tree = data_to_xml(classes, ships, battles, outcomes)
tree.write("ships_data.xml", encoding="utf-8", xml_declaration=True)

# Вывод файла для просмотра
# ET.dump(tree)
