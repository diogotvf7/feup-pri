import json

class StockChange:
    def __init__(self, name, value, ):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Stock name: {self.name} -> {self.value}\n"