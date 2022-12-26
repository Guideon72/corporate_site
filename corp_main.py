import streamlit as st
import pandas as pd

st.set_page_config(page_title="Our Company Details", layout="wide")

t_content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n 
Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere. Massa ultricies mi quis hendrerit dolor magna eget est.\n 
Adipiscing elit ut aliquam purus sit amet luctus venenatis. \n
Neque sodales ut etiam sit amet nisl purus in. Neque volutpat ac tincidunt vitae semper quis lectus nulla. 
Tincidunt eget nullam non nisi est. Nulla facilisi etiam dignissim diam quis enim lobortis. 
Felis donec et odio pellentesque diam volutpat. 
Velit aliquet sagittis id consectetur purus ut faucibus pulvinar. Quis risus sed vulputate odio ut. 
Viverra maecenas accumsan lacus vel. Varius vel pharetra vel turpis nunc.
"""

team_df = pd.read_csv("data/data.csv")


st.header("The Best Company")
st.write(t_content)

st.subheader("Our People")

col1, col2, col3 = st.columns([1.0, 1.0, 1.0])

with col1:
    for index, row in team_df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}  {row["last name"].title()}')
        st.write(row["role"].title())
        st.image("images/" + row["image"], width=300)

with col2:
    for index, row in team_df[4:8].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"].title())
        st.image("images/" + row["image"], width=300)

with col3:
    for index, row in team_df[8:].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"].title())
        st.image("images/" + row["image"], width=300)

with st.sidebar:
    st.text("Main and About will go here")
