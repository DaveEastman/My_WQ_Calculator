import datetime
import math
import streamlit as st

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

st.title("Interest Calculator")
st.write("___")

left_column, right_column = st.columns(2)
with left_column:
    with st.form(key='form1'):
    
        my_amount = st.number_input("Amount £: ", placeholder="None")
        my_interest = st.number_input("Interest rate %: ", placeholder="None")
        start_date = st.date_input("Start date:")
        end_date = st.date_input("End date:")

        submit_button = st.form_submit_button(label="Submit")

st.write("### Output data")

st.write("___")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Start date ", value=f"{start_date}", label_visibility="hidden")
col2.metric(label="End date ", value=f"{end_date}", label_visibility="hidden")
col3.metric(label="Interest rate", value=f"{my_interest:,.2f}%", label_visibility="hidden")
col4.metric(label="Amount", value=f"£{my_amount:,.2f}\n", label_visibility="hidden")



date1 = str(start_date).split('-')
date2 = str(end_date).split('-')

ptdt1 = datetime.date(year=int(date1[0]), month=int(date1[1]), day=int(date1[2]))
ptdt2 = datetime.date(year=int(date2[0]), month=int(date2[1]), day=int(date2[2]))

st.write("___")

daily_rate = float((my_amount * (my_interest / 100)) /365) 
daysbetween = (ptdt2 - ptdt1).days
int_owing = float(daysbetween * daily_rate)
final_owing = float(int_owing + my_amount)

col1.metric(label="Daily rate £ ", value=f"{daily_rate:,.2f}", label_visibility="hidden")
col2.metric(label="Number of days ", value=f"{daysbetween:}", label_visibility="hidden")
col3.metric(label="Interest owing ", value=f"£{int_owing:,.2f}", label_visibility="hidden")
col4.metric(label="Final amount ", value=f"£{final_owing:,.2f}", label_visibility="hidden")


col_1, col_2, col_3, col_4 = st.columns(4)
col_1.metric(label="Interest rate", value="")
col_2.metric(label="Daily rate", value="")
col_3.metric(label="Interest owing", value="")
col_4.metric(label="Final amount", value="")

rates = [8, 7, 6 , 5, 4, 3, 2, 1, 0.75, 0.5, 0.25]

for rate in rates:
    fltrate = float(rate)
    dayrate = (my_amount * ((fltrate / 100) / 365))
    interest = (daysbetween * dayrate)
    final = (interest + my_amount)
    col_1.metric(label="", value=f"{fltrate}%", label_visibility="hidden")
    col_2.metric(label="", value=f"£{dayrate:,.2f}", label_visibility="hidden")
    col_3.metric(label="", value=f"£{interest:,.2f}", label_visibility="hidden")
    col_4.metric(label="", value=f"£{final:,.2f}", label_visibility="hidden")
    if fltrate == 0.25:
        break


st.write("___")

