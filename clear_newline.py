def remove_newlines(file_path):
    with open(file_path, "r") as file:
        content = file.read().replace("\n", "")
    with open(file_path, "w") as file:
        file.write(content)

# Example usage
remove_newlines("meditations_raw.txt")