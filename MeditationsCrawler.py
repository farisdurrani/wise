import csv
import re



#with open("meditations_raw.txt", "r") as meditations_raw:
#    for

def parse_sentences(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        # sentences = re.split(r"[.?!]+", text)
        # sentences = text.split('/n/n')
        sentences = text.split('.')
        print('sentences: ' + str(sentences))
        return sentences

file_path = 'data.txt'
sentences = parse_sentences(file_path)


# # Reading from a CSV file
# with open("data.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     data = []
#     for row in csv_reader:
#         data.append(row)

# Writing to a CSV file
# with open("processed_data.csv", "w") as file:
#     csv_writer = csv.writer(file)
    # for row in data:
    #     csv_writer.writerow(row)

with open("processed_data.csv", "w") as file:
    for index, sentence in enumerate(sentences[0:20]):
        # print('index: ' + str(index))
        # print('sentence: ' + str(sentence))
        # if re.match(r'^\s*$', sentence):
        #     print('AAAAAAAAAAAAAAAaa')
        #     continue
        # else:

        # Writing to a CSV file
        data = [index, sentence]
        print('data: ' + str(data))
        # with open("processed_data.csv", "w") as file:
        csv_writer = csv.writer(file)
        # for row in data:
        csv_writer.writerow(data)


#test print
#for sentence in sentences:
    #print(sentence.strip())


