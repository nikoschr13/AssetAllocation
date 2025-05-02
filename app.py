
import streamlit as st

st.set_page_config(page_title="Elxi - Full Client Profile", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = 1
if 'data' not in st.session_state:
    st.session_state.data = {}

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def reset_form():
    st.session_state.page = 1
    st.session_state.data = {}

# Page 1: Personal Details
if st.session_state.page == 1:
    st.title("Step 1: Personal Details")
    st.session_state.data['name'] = st.text_input("Full Name")
    st.session_state.data['dob'] = st.date_input("Date of Birth")
    st.session_state.data['marital_status'] = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    st.session_state.data['occupation'] = st.text_input("Occupation")
    st.session_state.data['sector'] = st.text_input("Business Sector")
    if st.radio("Do you have dependent children?", ["Yes", "No"]) == "Yes":
        st.session_state.data['num_kids'] = st.number_input("Number of Children", min_value=1, step=1)
        st.session_state.data['kid_dobs'] = st.text_input("Dates of Birth (comma-separated)")
    if st.button("Next ➔"):
        next_page()

# Page 2: Financial Overview
elif st.session_state.page == 2:
    st.title("Step 2: Financial Overview")
    st.session_state.data['income_sources'] = st.multiselect("Sources of Income", [
        "Salary/Wages", "Business", "Pensions", "Rent", "Investments", "Other"])
    st.session_state.data['income_bracket'] = st.selectbox("Annual Income", [
        "<100k", "100k–250k", "250k–500k", "500k–1M", "1M–2M", "2M–5M", ">5M"])
    st.session_state.data['payments'] = st.multiselect("Payment Methods", [
        "Credit Card", "Debit Card", "Cash", "Mobile Apps", "Other"])
    st.session_state.data['savings'] = st.selectbox("Savings Rate", [
        "<10%", "10–20%", "20–30%", ">30%"])
    if st.radio("Any recurring financial commitments?", ["Yes", "No"]) == "Yes":
        st.session_state.data['commitment_details'] = st.text_area("Specify commitments")
    st.button("◀ Back", on_click=prev_page)
    if st.button("Next ➔"):
        next_page()

# Page 3: Expenses
elif st.session_state.page == 3:
    st.title("Step 3: Expenses & Commitments")
    st.session_state.data['housing'] = st.text_input("Annual Housing Costs")
    st.session_state.data['education'] = st.text_input("Education Expenses")
    st.session_state.data['healthcare'] = st.text_input("Healthcare Expenses")
    st.session_state.data['travel'] = st.text_input("Travel/Leisure")
    st.session_state.data['other_exp'] = st.text_input("Other Recurring Expenses")
    st.session_state.data['major_expenses'] = st.text_area("Any major expenses in next 5–10 years?")
    st.button("◀ Back", on_click=prev_page)
    if st.button("Next ➔"):
        next_page()

# Page 4: Assets & Liabilities
elif st.session_state.page == 4:
    st.title("Step 4: Assets & Liabilities")
    st.session_state.data['financial_assets'] = st.selectbox("Total Financial Assets", [
        "<100k", "100k–250k", "250k–500k", "500k–1M", "1M–2M", "2M–5M", ">5M"])
    st.session_state.data['real_estate'] = st.text_input("Real Estate Holdings")
    st.session_state.data['business'] = st.text_input("Business Equity/Private Assets")
    st.session_state.data['liabilities'] = st.text_area("Loans, mortgages, other debts")
    st.button("◀ Back", on_click=prev_page)
    if st.button("Next ➔"):
        next_page()

# Page 5: Risk Preferences
elif st.session_state.page == 5:
    st.title("Step 5: Risk Preferences & Investment Goals")
    st.session_state.data['goal'] = st.selectbox("Primary Investment Goal", [
        "Growth", "Income", "Retirement", "Wealth Transfer", "Speculation"])
    st.session_state.data['horizon'] = st.selectbox("Investment Horizon", [
        "1–5 years", "5–10 years", "10+ years"])
    st.session_state.data['risk_tolerance'] = st.radio("Risk Tolerance", [
        "Very Low", "Low", "Moderate", "Medium", "High"])
    st.session_state.data['liquidity'] = st.selectbox("Preferred Liquidity Buffer", [
        "<5%", "5–10%", "10–20%", ">20%"])
    st.session_state.data['leverage'] = st.radio("Comfort with Leveraging?", [
        "Very Comfortable", "Somewhat Comfortable", "Not Comfortable"])
    st.button("◀ Back", on_click=prev_page)
    if st.button("Next ➔"):
        next_page()

# Page 6: ESG & Tax
elif st.session_state.page == 6:
    st.title("Step 6: ESG & Tax Planning")
    st.session_state.data['esg'] = st.text_area("Do you prefer ESG/ethical investments?")
    st.session_state.data['currency_exposure'] = st.text_area("Any foreign currency exposure concerns?")
    st.session_state.data['tax_structuring'] = st.text_area("Any tax or wealth structuring needs?")
    st.session_state.data['review_frequency'] = st.text_input("Preferred review frequency")
    st.button("◀ Back", on_click=prev_page)
    if st.button("Finish"):
        next_page()

# Page 7: Summary and Export
elif st.session_state.page == 7:
    st.title("✅ Client Profile Complete")
    st.success("All sections filled. You can now export the summary.")
    summary = "\n".join([f"{k}: {v}" for k, v in st.session_state.data.items()])
    st.download_button("Download Summary (TXT)", summary, file_name="elxi_client_summary.txt")
    if st.button("Reset Form"):
        reset_form()
