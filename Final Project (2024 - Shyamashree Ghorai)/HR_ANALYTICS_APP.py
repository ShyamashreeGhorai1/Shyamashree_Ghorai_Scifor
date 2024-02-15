import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("HR_Analytics_.xlsx")
df = df.rename(columns={'Marital Status': 'Marital_Status'})

 
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="	:chart_with_downwards_trend:",
    layout="wide",
)
st.sidebar.header(" Please Filter Here :gear:",divider='gray')
gender = st.sidebar.multiselect(
    "Select the Gender:",
    options = df["Gender"].unique(),
    default = df["Gender"].unique()

)
marital_status = st.sidebar.multiselect(
    "Select Marital Status",
    options = df["Marital_Status"].unique(),
    default = df["Marital_Status"].unique()

 )
df_selection = df.query(
    "Gender == @gender & Marital_Status == @marital_status"
) 
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

st.title("	:bar_chart: 𝐻𝑅 :blue[𝐴𝑛𝑎𝑙𝑦𝑡𝑖𝑐𝑠]:red[𝐷𝑎𝑠ℎ𝑏𝑜𝑎𝑟𝑑] ")
data = st.button(":white_check_mark: Data")
if data:
    close = st.button(":white_check_mark: Close")
    write = st.write(df)
    if close:
        write = ''


# KPI's
total_employee = int(df_selection["Employee Count"].sum())
attrition = int(df_selection["Attrition Count"].sum())
active_employee = int(df_selection["Active Employee"].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Employee:")
    st.subheader(f":male-office-worker: {total_employee}")
with middle_column:
    st.subheader("Attrition Count")  
    st.subheader(f":male-office-worker: {attrition}")  
with right_column:
    st.subheader("Active Employee")  
    st.subheader(f":male-office-worker: {active_employee}")

active_employee_by_job_role = df_selection.groupby(by=["Job Role"])[["Active Employee"]].sum().sort_values(by="Job Role")
fig_job_role_employee = px.bar(
    active_employee_by_job_role,
    x = active_employee_by_job_role.index,
    y = "Active Employee",
    title="Active Employee by Job Role",
    color_discrete_sequence=["#F08080"]*len(active_employee_by_job_role),
    height=400,
    width=500
)   
active_employee_by_education = df_selection.groupby(by=["Education"])[['Active Employee']].sum().sort_values(by=["Education"])
fig_education_employee = px.pie(
    active_employee_by_education,
    values = "Active Employee",
    title= "Active Employee by Education",
    names= active_employee_by_education.index,
    height=400,
    width=500
)
left_column,middle_column, right_column = st.columns(3)
with left_column:
    st.write(fig_job_role_employee) 
with middle_column:
    st.write("")   
with right_column:
    st.write(fig_education_employee)

active_employee_by_age = df_selection.groupby(by=["CF_age band"])[["Active Employee"]].sum().sort_values(by=["Active Employee"],ascending=True)
fig_age_employee = px.bar(
    active_employee_by_age,
    x = "Active Employee",
    y = active_employee_by_age.index,
    orientation='h',
    title = "Active Employee by Age",
    color_discrete_sequence=["#00FFFF"]*len(active_employee_by_age),
    height=400,
    width=500
)
avg_monthly_income_by_job_role = df_selection.groupby(by=["Job Role"])[["Monthly Income"]].mean().sort_values(by=["Monthly Income"],ascending=False)
fig_income_job_role = px.area(
    avg_monthly_income_by_job_role,
    x = avg_monthly_income_by_job_role.index,
    y = "Monthly Income",
    height = 400,
    width=500
)
left_column,middle_column, right_column = st.columns(3)
with left_column:
    st.write(fig_age_employee) 
with middle_column:
    st.write("")   
with right_column:
    st.write(fig_income_job_role)

active_employee_by_department = df_selection.groupby(by=["Department"])[["Active Employee"]].sum().sort_values(by=["Department"])
attrition_by_department = df_selection.groupby(by=["Department"])[["Attrition Count"]].sum().sort_values(by=["Department"]) 

fig_job_role_employee = px.bar(
    active_employee_by_department,
    x = active_employee_by_department.index,
    y = "Active Employee",
    title="Active Employee by Job Role",
    color_discrete_sequence=["#CCCCFF"]*len(active_employee_by_department),
    height=400,
    width=500
)
fig_attrition = px.bar(
    attrition_by_department,
    x = attrition_by_department.index,
    y = "Attrition Count",
    title="Attrition by Job Role",
    color_discrete_sequence=["#008080"]*len(attrition_by_department),
    height=400,
    width=500
)
left_column,middle_column, right_column = st.columns(3)
with left_column:
    st.write(fig_job_role_employee) 
with middle_column:
    st.write("")   
with right_column:
    st.write(fig_attrition)

performance_rating_by_job_role = df_selection.groupby(by=["Job Role"])[['Performance Rating']].sum().sort_values(by=["Job Role"])
fig_performance = px.pie(
    performance_rating_by_job_role,
    values = "Performance Rating",
    title= "Performance Rating by Job Role",
    names= performance_rating_by_job_role.index,
    height=400,
    width=500
) 
st.write(fig_performance) 
 
#theme
hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

