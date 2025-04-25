def exchange_money(budget, exchange_rate):
    """
    Convierte el presupuesto ingresado a la moneda extranjera usando la tasa de cambio.

    Parámetros:
    - budget: cantidad de dinero en moneda original (float)
    - exchange_rate: tasa de cambio (float)

    Retorna:
    - El valor convertido en la moneda extranjera (float)
    """
    return budget * exchange_rate

# Prueba 1 de Japón
print("300 USD a yenes:", exchange_money(300, 133.33))

# Prueba 2 de México
print("500 USD a pesos mexicanos:", exchange_money(500, 16.95))

# Prueba 3 de Alemania
print("200 USD a euros:", exchange_money(200, 0.935))