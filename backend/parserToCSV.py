import csv
import re

def parse_text_file(file_path):
    # Open the file
    with open(file_path, 'r') as file:
        # Read the entire file contents into a string
        file_contents = file.read()

        # Use regular expressions to split the string into sentences
        sentences = re.findall(r'[^\.\?!]+[\.\?!]+', file_contents)

        # Return the list of sentences
        return sentences

if __name__ == '__main__':
    # Provide the file path
    file_path = 'meditations2.txt'

    # Call the `parse_text_file` function
    sentences = parse_text_file(file_path)

    # Specify the name of the CSV file
    csv_file_name = 'meditations2.csv'

    # Open the CSV file for writing
    with open(csv_file_name, 'w', newline='') as csvfile:
        # Create a writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Sentence'])

        # Write each sentence as a separate row
        for sentence in sentences:
            writer.writerow([sentence])





