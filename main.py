if __name__ == "__main__":
    print("starting")
    data_file = open("data.csv")
    data=[]
    for line in data_file.readlines():
        line_parts = line.split(",")
        index = int(line_parts[0])
        value = float(line_parts[1])
        text = str(line_parts[2]).strip()
        data.append([index, value, text])
    print(data)
print('2ch')