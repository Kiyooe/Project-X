class Robot:
    # Klassenvariable zur Ermittlung der Anzahl der insgesamt ezeugten Roboter
    count_robots = 0

    # Der Konstruktor der Klasse, der die Attribute initialisiert
    def __init__(self, name, color):
        Robot.count_robots += 1
        self.name = name
        self.color = color
        self.position = "Fabrik"
        self.serial_number = f"R{Robot.count_robots:03d}"  # Automatische Seriennummer

    # Magic-Method für die String-Repräsentation des Objekts
    def __str__(self):
        return f"Roboter {self.name} ({self.serial_number}) ist {self.color} und steht hier: {self.position}"   
    
    # Magic-Method für die offizielle Repräsentation des Objekts
    def __repr__(self):
        return f"Robot(name='{self.name}', color='{self.color}', position='{self.position}', serial_number='{self.serial_number}'"   
    
    # Methode zum Bewegen des Roboters an eine neue Position
    def move(self, new_position):
        self.position = new_position
class Battery:
    def __init__(self,capacity_wh:float ,state_of_charge:float = 1 ,max_discharge_rate_w:float = 50):
        self.capacity_wh = capacity_wh
        self.state_of_charge = state_of_charge
        self.max_discharge_rate_w = max_discharge_rate_w
    # Die Charge Methode Lädt die Batterie um amount_wh auf und aktualisiert den Ladestand
    def charge(self,amout_wh:float):
        new_Energy = self.capacity_wh * self.state_of_charge + amout_wh
        self.state_of_charge = min(new_Energy/ self.capacity_wh,1,0)
    
    def discharge(self,amount_wh:float):
        if amount_wh < self.state_of_charge * self.capacity_wh:
            return False
        self.state_of_charge = self.state_of_charge - amount_wh/ self.capacity_wh
        return True
    class ScoutBot(Robot):
    class HeavyBot(Robot):
    class TechBot(Robot):
    

# Erstellen von Instanzen der Klasse Robot
robot1 = Robot("ScoutBot", "Rot")
robot2 = Robot("TechBot", "Blau")
robot3 = Robot("HeavyBot", "Grün")

robot_list = [robot1, robot2, robot3]

print()
print("Es wurden bisher", Robot.count_robots, "Roboter erstellt")  # Ausgabe: Es wurden bisher 3 Roboter erstellt.
# Ausgabe der Informationen der Roboter
for robot in robot_list:
    print(robot)  # Verwendet die __str__-Methode
    print(repr(robot))  # Verwendet die __repr__-Methode

print()
print("Roboter werden bewegt... ")
robot1.move("Landezone")
robot2.move("Werkstatt")
robot3.move("Transportboot")

print()
# Ausgabe der Informationen der Roboter nach der Bewegung
for robot in robot_list:
    print(robot)  # Verwendet die __str__-Methode
#feste Wegpunkte in Reihenfolge ( Orte oder Koordinaten)   
Route = [
    ("Werkhalle A", (0,0)),
    ("Gabelstapler",(5,2)),
    ("Sensorenfeld",(9,4)),
    ("Tor West",    (13,4)),
    ("Ladestation", (6,1)), # offizieler Ladepunkt
    ("Lager C",     (10,1)),
    ("Werkhalle B", (3,7)),
    ("Tor Nord",    (8,4)),
    ("Lager A",     (18,11))
    ("Lager D",     (10,8))
]
#print(Route)