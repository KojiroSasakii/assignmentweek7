try:
    filename = input("Enter the file name: ")
    with open(filename, 'r') as file:
        senders = []
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1:
                    sender = words[1]
                    print(sender)
                    senders.append(sender)
        
        print(f"Total {len(senders)} lines were printed")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)
