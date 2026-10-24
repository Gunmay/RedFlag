from tinyfish import TinyFish

client = TinyFish()

print("RedFlag - Internship Offer Checker")
print("Paste the FULL offer in ONE line and press Enter:")

offer = input()

has_money = any(w in offer.lower() for w in ["deposit", "fee", "pay", "₹", "training"])
print("\nAsks for money?", "YES" if has_money else "No")

print("\nBasic version ready.")
