def format_scores(data):
    if not data:
        return ""
    name_width = max(len(name) for name, _ in data)
    score_width = max(len(str(score)) for _, score in data)
    lines = []
    for name, score in data:
        lines.append(f"{name.ljust(name_width)} {str(score).rjust(score_width)}")
    return "\n".join(lines)

# Example usage:
scores = [("Alice", 95), ("Bob", 88), ("Charlie", 100), ("Dana", 72)]
result = format_scores(scores)
print(result)