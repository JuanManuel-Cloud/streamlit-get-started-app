import streamlit as st
import pandas as pd

# Get the query parameters
query_params = st.experimental_get_query_params()

# Extract the client_id parameter if it exists
client_id = query_params.get("client_id", [None])[0]

loogik_trips_file = "dummy_data/ViajesRealiLoogik.xls"
loogik_fac_trips_file = "dummy_data/ViajesFacLoogik.xls"
qa_trips_file = "dummy_data/ViajesRealiQA.xls"
qa_fac_trips_file = "dummy_data/ViajesFacQA.xls"

# Check the client_id value and display output accordingly
if client_id == "1":
    st.write("Es el cliente QA")
    # Only passenger filter
    qa_trips_ds = pd.read_excel(
        qa_trips_file, usecols="B:AC", skiprows=range(0, 7))
    st.write(qa_trips_ds)
elif client_id == "2":
    st.write("Es el cliente Loogik")
    # Only passenger filter
    loogik_trips_ds = pd.read_excel(
        loogik_trips_file, usecols="B:AC", skiprows=range(0, 7))
    st.write(loogik_trips_ds)
else:
    st.write("Invalid client ID")