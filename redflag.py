from tinyfish import TinyFish

client = TinyFish()

print("RedFlag - Internship Offer Checker")
print("Paste the FULL offer in ONE line and press Enter:")

offer = input()

bad_words = ["training fee", "registration fee", "pay to confirm", "security deposit", "refundable deposit", "pay a deposit", "deposit of","program fee","fee"]
has_money = any(word in offer.lower() for word in bad_words)


if "no deposit" in offer.lower() or "no payment" in offer.lower() or "no fee" in offer.lower():
    has_money = False

print("\nEnter the company name from the offer:")

company = input()
print("\nEnter the email domain from the offer (e.g. amazon.com):")
print("If there is no email, type nil or n.a.")
email_domain = input().strip().lower()

print("\nAsks student to pay money?", "YES" if has_money else "No")

print("\nSearching for scam reports (including Reddit)...")
scam = client.search.query(query=f"{company} internship scam site:reddit.com")

serious_scam = False
reddit_mentions = 0

for result in scam.results[:15]:
    text = (result.title + " " + getattr(result, "snippet", "")).lower()
    url = result.url.lower()
    if "reddit.com" in url:
        reddit_mentions += 1
    
    if company.lower() in text and any(word in text for word in ["scam", "fake", "fraud", "cheat"]):
        serious_scam = True

if serious_scam:
    print(f"Serious scam reports found (including {reddit_mentions} Reddit mentions).")
else:
    print("No strong scam reports found specifically about this company.")
    
    if "reddit.com" in url:
        reddit_mentions += 1
    
    if company.lower() in text and any(word in text for word in ["scam", "fake", "fraud", "cheat"]):
        serious_scam = True

score = 80
known_companies = ["google", "amazon", "microsoft", "ibm", "tcs", "infosys", "accenture", "deloitte", "wipro", "hcl"]

if serious_scam:
    if company.lower() in known_companies:
        score -= 8
    else:
        score -= 18
    if reddit_mentions >= 2:
        score -= 5   


print("\nChecking if company is registered...")

if company.lower() in known_companies:
    registered = True
    print("Company is a well-known registered company.")
else:
    
    reg_search = client.search.query(query=f'"{company}" CIN OR MCA OR incorporated')
    registered = False
    for result in reg_search.results[:8]:
        text = (result.title + " " + getattr(result, "snippet", "")).lower()
        if company.lower() in text and any(w in text for w in ["cin", "incorporated", "mca"]):

            registered = True
            break
    if registered:
        print("Company appears to be registered.")
    else:
        print("Could not confirm company registration.")
      

print("\nChecking if the role is listed on the company careers page...")

careers_search = client.search.query(query=f"{company} careers OR {company} jobs OR {company} internship")

role_listed = False
for result in careers_search.results[:6]:
    text = (result.title + " " + getattr(result, "snippet", "")).lower()
    if any(word in text for word in ["intern", "internship", "career", "job", "opening"]):
        role_listed = True
        break

if role_listed:
    print("Role appears to be listed on careers/jobs pages.")
else:
    print("Could not find the role on official careers pages.")

score = 80
if has_money:
    score -= 30
if serious_scam:
    if company.lower() in known_companies:
        score -= 10   
    else:
        score -= 30  
if not registered:
    score -= 25
if not role_listed:
    score -= 15

no_email = email_domain in ["nil", "n.a.", "na", "n/a", "none", ""]

if no_email:
    domain_match = True
    domain_trust = True
    print("No email was given, so domain points were not cut.")
else:
    print("Checking if email domain matches company...")
    domain_search = client.search.query(query=f"{company} official website")

    domain_match = False
    for result in domain_search.results[:5]:
        if email_domain in result.url.lower():
            domain_match = True
            break

    if domain_match:
        print("Email domain appears to match the company website.")
    else:
        print("Email domain does not clearly match the company website.")

    print("\nChecking domain trust signals...")
    trust_search = client.search.query(query=f"{email_domain} domain age OR whois OR registered")

    domain_trust = False
    for result in trust_search.results[:5]:
        text = (result.title + " " + getattr(result, "snippet", "")).lower()
        if any(word in text for word in ["registered", "created", "whois", "domain age"]):
            domain_trust = True
            break

    if domain_trust:
        print("Domain has some public registration information.")
    else:
        print("Limited public information found about the domain.")

if not domain_match:
    score -= 15

score = max(0, min(100, score))

print(f"\nTrust Score: {score}%")

if score < 40:
    print("Risk Level: HIGH RISK")
elif score < 70:
    print("Risk Level: MEDIUM RISK")
else:
    print("Risk Level: LOW RISK")
