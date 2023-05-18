import streamlit as st
import pandas as pd
import altair as alt


def show_heat_map(df):
    # Group by date and count the trips
    trip_counts = df.groupby(
        'FECHA VIAJE').size().reset_index(name='count')

    # Create Altair circle-based heatmap chart
    heatmap = alt.Chart(trip_counts).mark_circle().encode(
        x=alt.X('FECHA VIAJE:T', title='Date'),
        y=alt.Y('count:Q', title='Trip Count'),
        size=alt.Size('count:Q', title='Count'),
        color=alt.value('#FF0049')  # Set default color
    ).configure_view(
        fill='transparent'  # Set transparent background
    )

    # Display the heatmap chart
    st.altair_chart(heatmap, use_container_width=True)


# Get the query parameters
query_params = st.experimental_get_query_params()

# Extract the client_id parameter if it exists
client_id = query_params.get("client_id", [None])[0]

loogik_trips_file = "dummy_data/ViajesRealiLoogik.xlsx"
qa_trips_file = "dummy_data/ViajesRealiQA.xlsx"

# Check the client_id value and display output accordingly
if client_id == "1":
    st.write("Es el cliente QA")
    # Only passenger filter
    qa_trips_df = pd.read_excel(
        qa_trips_file, usecols="B:AC", skiprows=range(0, 7), engine="openpyxl")
    qa_trips_df["IMPORTE DEL VIAJE [$]"].replace(
        "s/i", 0, inplace=True)  # Replace "s/i" with 0
    qa_trips_df['FECHA VIAJE'] = pd.to_datetime(qa_trips_df['FECHA VIAJE'])

    # st.write(qa_trips_df)
    st._arrow_bar_chart(
        qa_trips_df.loc[:, ["IMPORTE DEL VIAJE [$]"]])
    show_heat_map(qa_trips_df)

elif client_id == "2":
    st.write("Es el cliente Loogik")
    # Only passenger filter
    loogik_trips_df = pd.read_excel(
        loogik_trips_file, usecols="B:AC", skiprows=range(0, 7), engine="openpyxl")
    loogik_trips_df["IMPORTE DEL VIAJE [$]"].replace(
        "s/i", 0, inplace=True)  # Replace "s/i" with 0
    loogik_trips_df['FECHA VIAJE'] = pd.to_datetime(
        loogik_trips_df['FECHA VIAJE'])
    # st.write(loogik_trips_df)
    st._arrow_bar_chart(
        loogik_trips_df.loc[:, ["IMPORTE DEL VIAJE [$]"]])
    show_heat_map(loogik_trips_df)
else:
    st.write("Invalid client ID")
