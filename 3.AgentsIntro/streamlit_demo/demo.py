import streamlit as st
import time

st.set_page_config(page_title="Streamlit Intro1",page_icon=":tada:",layout="wide")
st.title("Streamlit basics")
st.caption("A tiny tour of the widgets and patterns used in projects.")

section = st.sidebar.radio("Section",[
    "1.Text & Layout",
    "2. Widgets & re-runs",
    "3. Session State",
    "4. Chat UI Preview"
    ])
# print(section)
if section =="1.Text & Layout":
    st.header("Text & Layout")
    st.markdown(
        """
        **`st.write`** is the Swiss-army knife — it renders strings, numbers,
        lists, dicts, and even DataFrames.

        **`st.markdown`** accepts GitHub-flavoured markdown (bold, links, lists).

        **`st.columns`** splits the page horizontally so you can place widgets
        side by side.
        """
    )
    st.write("Hello World!")
    left,right = st.columns(2)
    with left:
        st.metric(label="Token used", value = 128, delta = 12)
    with right:
        st.info("st.info / st.succes / st.warning / st.error")
        st.success("st.info / st.succes / st.warning / st.error")
        st.warning("st.info / st.succes / st.warning / st.error")
        st.error("st.info / st.succes / st.warning / st.error")
    st.divider()
    st.subheader("code")
    st.code("""
     'st.write("Hello world!")',
    """,language="python")
elif section == "2. Widgets & re-runs":
    st.header("Widgets & re-runs")
    st.markdown("""
     Widgets return the user's current choice/input on the current run.
    """
    )
    name = st.text_input(label="Your Name:",placeholder="Type your name here...")
    mood = st.selectbox(label="Your Mood",options=["Happy","Sad","Angry","Ambivalent"])
    slider = st.slider(label="Enthusiasm",min_value=0,max_value=100,value=45)
    # print(f"name: {name}, mood: {mood}, slider: {slider}")
    st.divider()
    if st.button("Say hello"):
        st.success(f"Hello {name}! You are {mood} and your enthusiasm is {slider}.")

    # counter = 0
    if "counter" not in st.session_state:
        st.session_state.counter =0
    if st.button("Increment"):
        st.session_state.counter +=1
        st.success(f"Counter: {st.session_state.counter}")
elif section == "3. Session State":
    st.header("Session State")
    st.markdown(
        """
        Session state allows you to store values that persist across runs.
        """
    )

    if "click_count" not in st.session_state:
        st.session_state.click_count =0
    col_a, col_b,col_c = st.columns(3)
    with col_a:
        if st.button("Click me"):
            st.session_state.click_count +=1
    with col_b:
        if st.button("Reset"):
            st.session_state.click_count =0
    with col_c:
        st.metric(label="Click Count", value=st.session_state.click_count)

    st.divider()
    if "note" not in st.session_state:
        st.session_state.note = []

    note = st.text_input(label="Add Note",placeholder="Enter your notes..")
    if st.button("Add Note") and note.strip():
        st.session_state.note.append(note.strip())
    if st.session_state.note:
        st.header("Notes:")
        for item in st.session_state.note:
            st.write(item)
    else:
        st.write("Add a Note to get started!") 
elif section == "4. Chat UI Preview":
    st.header("Chat UI Preview")
    st.markdown(
        """
        This is a preview of the Chat UI
        """
    )
    if "chat_log" not in st.session_state:
        st.session_state.chat_log=[]

    for entry in st.session_state.chat_log:
        with st.chat_message(entry["role"]):
            st.write(entry["content"])

    prompt = st.chat_input("Try asking me anything...")

    if prompt:
        st.session_state.chat_log.append({"role":"user","content":prompt})

        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking...."):
                time.sleep(2)
            st.write("Dummy response")
            st.session_state.chat_log.append({"role":"assistant","content":"Dummy Response"})