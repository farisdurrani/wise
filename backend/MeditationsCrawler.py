import csv
#import re


#with open("meditations_raw.txt", "r") as meditations_raw:
#    for

#def parse_sentences(file_path):
#    with open(file_path, 'r') as f:
#        text = f.read()
#        #sentences = re.split("([.!?\n])", text)
#        sentences = re.split("(?<=[.!?])\s+", text)
        #sentences = re.split(r'[.!?\n]', text)
        #sentences = text.split('.')
#        return sentences
#
#file_path = 'meditations_raw.txt'
#sentences = parse_sentences(file_path)

#for sentence in sentences[0:20]:
#    if re.match(r'^\s*$', sentence):
#       continue
#    else:
#        print(sentence.strip())




#test print
#for sentence in sentences:
    #print(sentence.strip())

# Open the text file and the .csv file for writing
with open('meditations_raw.txt', 'r') as text_file, open('meditations.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Read each line from the text file
    for line in text_file:
        # Write each line as a separate row in the .csv file
        writer.writerow([line.strip()])

