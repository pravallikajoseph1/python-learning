class Machine:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def check_status(self):
        if self.temperature > 80:
            print(f"WARNING: {self.name} is overheating! Current temperature: {self.temperature}°C")
        else:
            print(f"{self.name} is operating normally. Current temperature: {self.temperature}°C")
machine1 = Machine("Pump A", 90)
machine1.check_status()