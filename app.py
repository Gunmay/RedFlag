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