def clean_string(input_str):
    # 先頭・末尾の空白を除去
    cleaned = input_str.strip()
    # 小文字に変換
    cleaned = cleaned.lower()
    # 空白をアンダースコアに置換
    cleaned = cleaned.replace(" ", "_")
    return cleaned

# Sample calls for demonstration
print(clean_string("   Hello World   "))  # hello_world
print(clean_string("Python Programming"))  # python_programming
print(clean_string("  DATA science  "))    # data_science