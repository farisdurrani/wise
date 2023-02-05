import csv
import re


def __parse_text_file(file_path):
    # Open the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire file contents into a string
        file_contents = file.read()

        # Use regular expressions to split the string into sentences
        sentences = re.findall(r'[^\.\?!]+[\.\?!]+', file_contents)

        # Return the list of sentences
        return sentences


def concertTxtToCsv(file_path: str) -> bool:
    # Call the `parse_text_file` function
    sentences = __parse_text_file(file_path)
    path_parts = file_path.split("/")

    base_name = path_parts[-1].split(".")[0]

    # Specify the name of the CSV file
    csv_file_name = f"{'/'.join(path_parts[:-1])}/{base_name}.csv"

    # Open the CSV file for writing
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Text'])

        # Write each sentence as a separate row
        for sentence in sentences:
            writer.writerow([sentence])

    return True
