def mask_data(data):
    if len(data) <= 4:
        return "*" * len(data)
    return data[:2] + "*" * (len(data) - 4) + data[-2:]
