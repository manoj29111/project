b=raw_input("")
 num_words = 0
 for line in b:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
