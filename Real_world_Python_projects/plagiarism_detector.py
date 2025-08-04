import string

# Function to load and clean essay content
def load_and_clean(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        # Remove punctuation
        for p in string.punctuation:
            text = text.replace(p, "")
        words = text.split()
    return words

# Load both essays
essay1_words = load_and_clean("essay1.txt")
essay2_words = load_and_clean("essay2.txt")

# Convert to sets for comparison
set1 = set(essay1_words)
set2 = set(essay2_words)

# 1. Compare essays
intersection = set1.intersection(set2)
union = set1.union(set2)

# 2. Find common words with frequency
def count_common_words():
    print("\n COMMON WORDS AND FREQUENCIES:")
    print("-" * 30)
    for word in sorted(intersection):
        count1 = essay1_words.count(word)
        count2 = essay2_words.count(word)
        print(f"{word} - Essay1: {count1}, Essay2: {count2}")

# 3. Search for a specific word
def search_word(word):
    word = word.lower()
    count1 = essay1_words.count(word)
    count2 = essay2_words.count(word)
    if count1 == 0 and count2 == 0:
        print(f"'{word}' not found in either essay.")
        return False
    print(f"'{word}' appears {count1} times in Essay 1 and {count2} times in Essay 2.")
    return True

# 4. Calculate plagiarism percentage
def calculate_plagiarism():
    if len(union) == 0:
        return 0.0
    percentage = (len(intersection) / len(union)) * 100
    return round(percentage, 2)

# ------------------------------
# User Interaction & Testing
# ------------------------------

# Show common words
count_common_words()

# Word Search Example
user_word = input("\nEnter a word to search: ")
found = search_word(user_word)
if not found:
    print(f"{user_word} not found in either essay.")

# Show plagiarism result
plagiarism_score = calculate_plagiarism()
print(f"\nPlagiarism Score: {plagiarism_score}%")
if plagiarism_score >= 50:
    print("⚠️ Potential Plagiarism Detected!")
else:
    print("✅ No major plagiarism detected.")
