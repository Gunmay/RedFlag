from tinyfish import TinyFish

client = TinyFish()

print("RedFlag - Internship Offer Checker")
print("Paste the FULL offer in ONE line and press Enter:")

offer = input()


bad_words = ["deposit", "training fee", "registration fee", "pay to confirm", "security deposit", "refundable deposit"]
has_money = any(word in offer.lower() for word in bad_words)

print("\nAsks student to pay money?", "YES" if has_money else "No")

print("\nBasic version ready.")
