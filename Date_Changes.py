import datetime
import streamlit as st
from dateutil.relativedelta import relativedelta

st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 15px;
}
</style>
""",
    unsafe_allow_html=True,
)

icons = ["bi-calendar3"]

st.title("Date Calculators")
st.write("___")

st.title("Days Add Calculator")
st.write("___")

left_column, right_column = st.columns(2)
with left_column:
    with st.form(key='form1'):
        start_date = st.date_input("Start date:")
        end_date = st.number_input("Number of days to add:", value=0)

        submit_button = st.form_submit_button(label="Submit")

st.write("___")

d1 = str(start_date)
d2 = int(end_date)

sdate1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
st1 = sdate1.strftime("%d-%m-%Y")

new_date = sdate1 + datetime.timedelta(d2)
output_date = new_date.strftime("%A, %d-%m-%Y")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Start date", value=f"{st1}")
col2.metric(label="number of days added", value=f"{end_date}")
col3.metric(label="Final date", value=f"{output_date}")

st.write("___")

st.title("Length of Mortgage Calculator")
st.write("___")

left_column, right_column = st.columns(2)
with left_column:
    with st.form(key='form3'):
        start_date = st.date_input("Date of Mortgage Start:")
        end_date = st.date_input("Date of Mortgage End:")

        submit_button2 = st.form_submit_button(label="Submit")

day1 = str(start_date)
day2 = str(end_date)

sdate1 = datetime.datetime.strptime(day1, "%Y-%m-%d")
edate2 = datetime.datetime.strptime(day2, "%Y-%m-%d")

# convert string to date object


# Get the relativedelta between two dates
delta = relativedelta(end_date, start_date)
st.write("The length of the mortgage is:")
st.write(delta.years, 'years,', delta.months, 'months,', delta.days, 'days')

st.title("Remaining Mortgage Term")
st.write("___")

left_column, right_column = st.columns(2)
with left_column:
    with st.form(key='form4'):
        start_date = st.date_input("Date of Witness Statement:")
        end_date = st.date_input("Date of Mortgage End:")

        submit_button3 = st.form_submit_button(label="Submit")

sday1 = str(start_date)
eday2 = str(end_date)

sdate1 = datetime.datetime.strptime(sday1, "%Y-%m-%d")
edate2 = datetime.datetime.strptime(eday2, "%Y-%m-%d")

# convert string to date object


# Get the relativedelta between two dates
delta = relativedelta(end_date, start_date)
st.write("The length of time remaining on the mortgage is:")
st.write(delta.years, 'years,', delta.months, 'months,', delta.days, 'days')
