# RedFlag

RedFlag checks an internship offer before a student pays or shares documents.

Paste the letter, the company name, and the sender's email domain. The site runs five checks and returns a trust score, with the pages it opened left on the card.

Live site: https://redflaggs.streamlit.app/

Built by Soumil Bansal and Gunmay Bhanot for HackIIITD, a 24-hour national hackathon organised by IIIT Delhi.

## What it checks

The score starts at 80.

| Check | What it looks at | Points cut |
|---|---|---|
| Fee demand | Words such as deposit, training fee, security deposit, and pay to confirm | 30 |
| Company name | A short list of known companies. Any other name is marked unknown | 25 |
| Email domain | Gmail, Yahoo, Outlook, Hotmail, or a domain that does not match the company site | 15 |
| Domain record | A company domain with little public registration information | 5 |
| Scam reports | Reddit posts where the company name sits next to scam, fake, fraud, or cheat | 8 for a known company, 18 for any other name. Two or more Reddit mentions cut 5 more |
| Careers page | A jobs or internship page that names the company. Only unknown companies are cut when this is missing | 10 |

If the letter says there is no fee, the fee check does not cut. If no email is given, type `nil` or `n.a.` and the email check does not cut.

Under 40 is high risk. From 40 to 64 is medium. 65 and above is low.

A low score is a warning. A high score is not a promise. Never pay money to get an internship.

## How a scan runs

1. The letter is read for a payment demand.
2. The company name is compared with the known list.
3. TinyFish searches Reddit for scam reports and keeps up to three links.
4. TinyFish searches for a careers, jobs, or internship page.
5. If the email is not a free inbox, TinyFish checks whether the domain appears on the company site and whether a public registration record exists.
6. Each result is shown as its own card. The score is shown at the end.

## Stack

- Backend: Python
- Frontend: Python, HTML, and CSS
- Site: Streamlit
- Live search: TinyFish

## Run it locally

From the project folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install streamlit tinyfish
export TINYFISH_API_KEY="your-key-here"
streamlit run app.py
