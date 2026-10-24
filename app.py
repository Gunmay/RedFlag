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
        st.write("Company: " + company)
        st.write("Domain: " + domain)
        st.write("Offer length: " + str(len(offer)))
        
elif st.session_state.page == "How it works":
    st.write("The five checks will be explained here.")
elif st.session_state.page == "About":
    st.write("RedFlag checks an offer before a student pays anything.")
