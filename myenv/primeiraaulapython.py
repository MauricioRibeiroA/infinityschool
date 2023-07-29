
def converter(f):
    celsius = f'{((f-32)/1.8):.6f}'
    return celsius

print(converter(32))


def converterOposto(c):
    farenheit = f'{(c*1.8+32):.4f}'
    return farenheit

print(converterOposto(32))
