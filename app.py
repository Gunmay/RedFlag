import streamlit as st

st.set_page_config(page_title="RedFlag", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background: #06050d; color: #f3f1ff; }
    .hero {
        font-size: 72px;
        font-weight: 800;
        line-height: 0.95;
    }
    .pink { color: #ff2d55; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="hero">Don\'t pay for<br>a <span class="pink">fake offer.</span></p>', unsafe_allow_html=True)
st.write("Paste an internship offer. RedFlag checks it and shows the evidence.")
st.markdown(
    """
    <p>
    <b>5</b> checks &nbsp;&nbsp;
    <b>80</b> starting score &nbsp;&nbsp;
    <b>nil</b> if the offer has no email
    </p>
    """,
    unsafe_allow_html=True,
)
if "page" not in st.session_state:
    st.session_state.page = "Home"

home, scams, scanner, how, about = st.columns(5)

if home.button("Home"):
    st.session_state.page = "Home"
if scams.button("Real scams"):
    st.session_state.page = "Real scams"
if scanner.button("Scanner"):
    st.session_state.page = "Scanner"
if how.button("How it works"):
    st.session_state.page = "How it works"
if about.button("About"):
    st.session_state.page = "About"

st.write("You are on: " + st.session_state.page)
if st.session_state.page == "Home":
    st.write("This is the opening page.")
elif st.session_state.page == "Real scams":
    st.write("Four common fake-offer tricks will be listed here.")
elif st.session_state.page == "Scanner":
    st.write("Paste the offer. The checks will use this text.")
    offer = st.text_area("The full offer", height=200)
    company = st.text_input("Company name")
    domain = st.text_input("Sender email domain")
    if st.button("Run RedFlag scan"):
        bad_words = ["training fee", "registration fee", "pay to confirm", "security deposit", "refundable deposit", "pay a deposit", "deposit of", "deposit"]
        known = ["google", "amazon", "microsoft", "ibm", "tcs", "infosys", "accenture", "deloitte", "wipro", "hcl"]
        no_email_words = ["", "nil", "n.a.", "na", "n/a", "none"]
        free_emails = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
        low = offer.lower()
        company_name = company.lower().strip()
        domain_name = domain.lower().strip()
        has_money = any(word in low for word in bad_words)
        if "no deposit" in low or "no payment" in low or "no fee" in low:
            has_money = False
        if "deposit of" in low or "security deposit" in low or "refundable deposit" in low or "pay a deposit" in low:
            has_money = True
        if has_money:
            st.write("Asks the student to pay money? YES")
        else:
            st.write("Asks the student to pay money? No")

        registered = company_name in known
        if company_name == "":
            st.write("Type the company name.")
        elif registered:
            st.write("Company is a well-known registered company.")
        else:
            st.write("This company is not on the known list.")
        no_email = domain_name in no_email_words
        free_email = any(item in domain_name for item in free_emails)
        if no_email:
            st.write("No email was given, so domain points were not cut.")
        elif free_email:
            st.write("This is a free email, not a company domain.")
        else:
            st.write("Email domain noted: " + domain_name)
        score = 80
        if has_money:
            score -= 30
        if company_name != "" and not registered:
            score-=25
        if free_email and not no_email:
            score -= 15
        st.write("Trust score: " + str(score)+"%")
        if score < 40:
            st.write("Risk level: HIGH RISK")
        elif score < 70:
            st.write("Risk level: MEDIUM RISK")
        else:
            st.write("Risk level: LOW RISK")
elif st.session_state.page == "How it works":
    st.write("The five checks will be explained here.")
elif st.session_state.page == "About":
    st.write("RedFlag checks an offer before a student pays anything.")
