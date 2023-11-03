try:
    with open('romeo.txt', 'r') as file:
        unique_words = []
        for line in file:
            words = line.split()
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

        unique_words.sort()
        print(unique_words)
except FileNotFoundError:
    print("The 'romeo.txt' file was not found.")
except Exception as e:
    print("An error occurred:", e)
