def strings_to_floats(str_list):
    result = []
    for s in str_list:
        try:
            value = float(s)
            result.append(value)
        except ValueError:
            continue
    return result

# Sample usage
sample_data = ["3.14", "not_a_number", "42", "7.0", "NaN", "five"]
converted = strings_to_floats(sample_data)
print(converted)