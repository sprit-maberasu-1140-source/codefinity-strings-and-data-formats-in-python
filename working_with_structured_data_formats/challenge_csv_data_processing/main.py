def average_age(csv_string):
    lines = csv_string.strip().split("\n")
    if len(lines) <= 1:
        return 0.0
    ages = []
    for line in lines[1:]:
        parts = line.split(",")
        if len(parts) == 2:
            try:
                ages.append(int(parts[1]))
            except ValueError:
                continue
    if not ages:
        return 0.0
    return sum(ages) / len(ages)
