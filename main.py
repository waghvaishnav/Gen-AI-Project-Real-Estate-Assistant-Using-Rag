import streamlit as st
from rag import process_urls,generate_answer

st.set_page_config(
    page_title="Real Estate Assistant",
    page_icon=" ")

st.title("Real Estate Assistant Using Rag")
st.subheader("Queries -> Research -> Information -> Invest")

placeholder1  = st.empty()
placeholder2 = st.empty()
placeholder3 = st.empty()


url1 = st.sidebar.text_input("Enter URL1 Here ")
url2 = st.sidebar.text_input("Enter URL2 Here ")
url3 = st.sidebar.text_input("Enter URL3 Here ")

new = placeholder1.write("processing........")

col1,col2 = st.columns(2)

with col1:

    temp = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=0.6,
    value=0.2,
    step=0.1)


with col2:

    new = st.write("""default temperature is 0.2
    Higher Value : Random and Varied Results,
    Lower Values : Fixed Results.""")

process_url_button = st.sidebar.button("Process URLS")
if process_url_button:
    urls = [url for url in (url1,url2,url3) if url != '']
    print(urls)
    if len(urls) == 0:
        placeholder2.warning("You Must Provide at least One URL Here for Further Processing")
    else:
        for status in process_urls(urls,temp):
            placeholder2.success(status)


query_button = placeholder1.text_input("What is Your Query Today ?")
if query_button:
    try:
        answer,sources = generate_answer(query_button)
        st.info("Answer :")
        st.write(answer)

        if sources:
            st.subheader("sources")
            for source in sources.split("\n"):
                st.link_button("Go To Sources >",source)
#               st.write(source)
    except RunTimeError as e:
        placeholder2.warning("You Must Process Url First.")
















with st.expander(" How to Use the Real Estate Assistant ?"):

    st.markdown("""
    * 1.Open the App and Ensure you have a stable internet connection.

    * 2.Enter at least one valid research URL in the URL bar

    * 3.Enter a specific question related to the information available on the provided URLs.

    * 4.Click on "Process URLs" to process data.

    * 5.Read the generated answer and verify the provided sources.

    * 6.🏠 Make an Informed Decision and Invest Properly. """)

    st.info(
        "💡 Tip: Use reliable research sources and ask specific questions "
        "for better results."
    )