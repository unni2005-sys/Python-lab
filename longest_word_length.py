words = input("Enter words: ").split()
longest = max(words, key=len)
print("Length of the longest word:", len(longest))
