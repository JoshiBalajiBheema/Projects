from difflib import SequenceMatcher
import time

text1 = input("Enter the First Sentence : ")
text2 = input("Enter the Second Sentence : ")
print("Analyzing your INPUTS..")
time.sleep(1)
MatchScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {round(MatchScore * 100,2)} % similar.")
