# Simple short-run macroeconomic model
#

def calculate_ae(a, i, g, x, b, t, m, y):
    auto_expenditure = a + i + g + x
    induced_expenditure = (b * (1 - t) - m)
    ae = auto_expenditure + induced_expenditure * y
    return ae, auto_expenditure, induced_expenditure
