from tinyfish import TinyFish

client = TinyFish()

print("RedFlag - Internship Offer Checker")
print("Paste the FULL offer in ONE line and press Enter:")

offer = input()

bad_words = ["training fee", "registration fee", "pay to confirm", "security deposit", "refundable deposit", "pay a deposit", "deposit of"]
has_money = any(word in offer.lower() for word in bad_words)


if "no deposit" in offer.lower() or "no payment" in offer.lower() or "no fee" in offer.lower():
    has_money = False

print("\nAsks student to pay money?", "YES" if has_money else "No")

print("\nEnter the company name from the offer:")
company = input()

print("\nSearching for scam reports...")
scam = client.search.query(query=f"{company} internship scam")


serious_scam = False
for result in scam.results[:20]:  
    text = (result.title + " " + getattr(result, "snippet", "")).lower()
    if company.lower() in text and any(word in text for word in ["scam", "fake", "fraud", "cheat"]):
        serious_scam = True
        break

if serious_scam:
    print("Serious scam reports found about this company.")
else:
    print("No strong scam reports found specifically about this company.")


score = 70
if has_money:
    score -= 40
if serious_scam:
    score -= 25

score = max(0, min(100, score))

print(f"\nTrust Score: {score}/100")

if score < 40:
    print("Risk Level: HIGH RISK")
elif score < 70:
    print("Risk Level: MEDIUM RISK")
else:
    print("Risk Level: LOW RISK")