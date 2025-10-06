# Simple short-run macroeconomic model
#

def calculate_ae(data):
    auto_expenditure = data["a"] + data["i"] + data["g"] + data["x"]
    induced_expenditure = (data["b"] * (1 - data["t"]) - data["m"])
    ae = auto_expenditure + induced_expenditure * data["y"]
    return ae, auto_expenditure, induced_expenditure
