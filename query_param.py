import streamlit as st

# Get the query parameters
query_params = st.experimental_get_query_params()

# Extract the client_id parameter if it exists
client_id = query_params.get("client_id", [None])[0]

# Check the client_id value and display output accordingly
if client_id == "1":
    st.write("Es el cliente 1")
elif client_id == "2":
    st.write("Es el cliente 2")
else:
    st.write("Invalid client ID")

