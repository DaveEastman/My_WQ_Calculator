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

st.title("Norgan Calculator")
st.write("___")

left_column, right_column = st.columns(2)
with left_column:
    with st.form(key='form2'):
        my_amount = st.number_input("Total arrears £: ", placeholder="None")
        start_date = st.date_input("Date of Witness Statement:")
        end_date = st.date_input("Date of Mortgage End:")
        my_cmi = st.number_input("Current Monthly Installment (CMI) £: ", placeholder="None")

        submit_button = st.form_submit_button(label="Submit")

st.write("### Output data")

st.write("___")
col1, col2, col3 = st.columns(3)
col2.metric(label="Date of Witness Statement ", value=f"{start_date}")
col3.metric(label="Date of Mortgage End ", value=f"{end_date}")
col1.metric(label="Total arrears", value=f"£{my_amount:,.2f}\n")

d1 = str(start_date)
d2 = str(end_date)

sdate1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
edate2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

delta = relativedelta(edate2, sdate1)
res_months = delta.months + (delta.years * 12)

st.write("___")

if res_months == 0:
    res_months = 1

min_pay = (my_amount / res_months)

col1.metric(label="Number of months ", value=f"{res_months:}")
col2.metric(label="Minimum monthly payment ", value=f"£{min_pay:,.2f}")

st.write("___")

if my_cmi == 0:
    my_cmi = 1

eq_cmi = (my_amount / my_cmi)

col1, col2, col3 = st.columns(3)
col1.metric(label="Arrears ", value=f"{my_amount:}")
col2.metric(label="CMI ", value=f"£{my_cmi:,.2f}")
col3.metric(label="Equivalent # of CMIs ", value=f"{eq_cmi:,.1f}")
