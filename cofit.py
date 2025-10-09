import streamlit as st

from millify import millify, prettify

def show_value(value):
  if value >= 1e6:
    return millify(value, precision=3)
  return millify(value, precision=0)


# Use whole page width
st.set_page_config(layout="wide")

st.title("Cohousing Finance Tool - CoFiT")

st.header("Units")

units_columns_param = st.columns(5, gap="large", vertical_alignment="center")
with units_columns_param[1]:
  st.text("Type I")
  n_small = st.number_input("Number", min_value=0, max_value=50, value=10, step=1, key="n_small")
  size_small = st.number_input("Size (sf)", min_value=200, max_value=2000, value=700, step=10)
with units_columns_param[2]:
  st.text("Type II")
  n_medium = st.number_input("Number", min_value=0, max_value=50, value=10, step=1, key="n_medium")
  size_medium = st.number_input("Size (sf)", min_value=200, max_value=2000, value=900, step=10)
with units_columns_param[3]:
  st.text("Type III")
  n_large = st.number_input("Number", min_value=0, max_value=50, value=10, step=1, key="n_large")
  size_large = st.number_input("Size (sf)", min_value=200, max_value=2000, value=1100, step=10)


n_units = n_small + n_medium + n_large
total_size = n_small * size_small + n_medium * size_medium + n_large * size_large
size_average = total_size / n_units


units_columns_res = st.columns(5, gap="large", vertical_alignment="center")
with units_columns_res[1]:
  st.metric("Units", n_units)
with units_columns_res[2]:
  st.metric("Avg Area", prettify(int(size_average)))


st.header("Development Size")

size_params = st.columns(5, gap="large")
with size_params[1]:
  total_sealable_area = st.slider("Total Sealable Area (sf)", min_value=10000, max_value=50000, value=27000, step=1000)
with size_params[2]:
  common_house_area = st.slider("Common House Area (sf)", min_value=1000, max_value=10000, value=4000, step=100)
with size_params[3]:
  circulation_percent = st.slider("Circulation (%)", min_value=0, max_value=100, value=15)


circulation_area = circulation_percent * total_sealable_area / 100
total_area = total_sealable_area + common_house_area + circulation_area

size_results = st.columns(5, gap="large")
with size_results[2]:
  st.metric("Circulation Area (sf)", prettify(int(circulation_area)))
with size_results[1]:
  st.metric("Total Area (sf)", prettify(int(total_area)))


st.header("Development Analysis")

st.subheader("Phase 1: Aquisiton")

aqui_params = st.columns(5, gap="large")
with aqui_params[1]:
  purchase_price = 1e6 * st.slider("Purchase Prince ($)", min_value=0.5, max_value=5.0, value=1.4, format="%0.2fM")
with aqui_params[3]:
  closing_cost_percent = st.slider("Closing Costs (%)", min_value=0.0, max_value=5.0, value=2.0, step=0.1, format="%0.1f")
with aqui_params[2]:
  transfer_fee_percent = st.slider("Realtor Transfer Fee (%)", min_value=0.0, max_value=5.0, value=1.0, step=0.1, format="%0.1f")

transfer_cost = transfer_fee_percent * purchase_price / 100
closing_cost = closing_cost_percent * purchase_price / 100
total_aqui_cost = purchase_price + transfer_cost + closing_cost

aqui_results = st.columns(5, gap="large")
with aqui_results[1]:
  st.metric("Total Aqusition Costs ($)", show_value(total_aqui_cost))
with aqui_results[2]:
  st.metric("Closing Costs ($)", show_value(closing_cost))
with aqui_results[3]:
  st.metric("Realtor Transfer Fee ($)", show_value(transfer_cost))

st.subheader("Phase 2: Pre-Construction (Soft Costs)")

preco_params = st.columns(5, gap="large")
with preco_params[1]:
  st.text("> $100k")
  design = 1000 * st.slider("Design Professionals, Project Managment ($)", min_value=0, max_value=1000, value=800, step=10, format="%dk")
  legal = 1000 * st.slider("Legal, Accounting, Appraisal ($)", min_value=0, max_value=1000, value=100, step=10, format="$%dk")
  application = 1000 * st.slider("Application Fees($)", min_value=0, max_value=1000, value=200, step=10, format="%dk")
  hpo = 1000 * st.slider("HPO Insurance ($)", min_value=0, max_value=1000, value=100, step=10, format="%dk")
  insurance = 1000 * st.slider("Insurance($)", min_value=0, max_value=1000, value=130, step=10, format="%dk")
with preco_params[2]:
  st.text("> $10k")
  tax = 1000 * st.slider("Municpal and Property Tax ($)", min_value=0, max_value=100, value=25, format="%dk")
  survey = 1000 * st.slider("Survey ($)", min_value=0, max_value=100, value=50, format="%dk")
  travel = 1000 * st.slider("Disburments and Travel ($)", min_value=0, max_value=100, value=15, format="%dk")
with preco_params[3]:
  st.text("> $1k")
  outreach = 1000 * st.slider("Outreach ($)", min_value=0, max_value=10, value=5, format="%dk")

preco_total = design + legal + application + hpo + insurance + tax + survey + travel + outreach

preco_results = st.columns(5, gap="large")
with preco_results[1]:
  st.metric("Total Pre-construction Costs ($)", show_value(preco_total))

st.subheader("Phase 3: Construction (Hard Costs)")

constr_params = st.columns(5, gap="large")
with constr_params[1]:
  building_per_sf = st.slider("Building Contruction per sf ($)", min_value=0, max_value=500, value=160, step=5, format="%d")
with constr_params[2]:
  common_house = 1000 * st.slider("Commmon House ($)", min_value=0, max_value=1000, value=800, step=10, format="%dk")
with constr_params[3]:
  site = 1000 * st.slider("Site Servising and Landscape ($)", min_value=0, max_value=1000, value=300, step=10, format="%dk")

building_cost = building_per_sf * total_area
construction_cost = building_cost + common_house + site 

constr_results = st.columns(5, gap="large")
with constr_results[1]:
  st.metric("Building Contructions ($)", show_value(building_per_sf * total_area))
with constr_results[2]:
  st.metric("Total Construction Cost ($)", show_value(construction_cost))


st.subheader("Phase 4: Financing (Primary)")

primary_params = st.columns(5, gap="large")
with primary_params[3]:
  surveyor = 1000 * st.slider("Quantity surveyor ($)", min_value=0, max_value=50, value=30, format="%dk")
  contingency_percent = st.slider("Contingency (%)", min_value=0, max_value=20, value=12, format="%d")
with primary_params[2]:
  time = st.slider("Construction Time (months)", min_value=0, max_value=36, value=18)
  bonus_percent = st.slider("Financing Bonus (%)", min_value=0.0, max_value=10.0, value=0.7, step=0.1, format="%0.1f")
with primary_params[1]:
  carry_cost = st.slider("Carry Cost on Land (per months)", min_value=0, max_value=5000, value=2500, step=100)
  interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=10.0, value=6.0, step=0.1, format="%0.1f")

carry = carry_cost * (time + 2)

primary_results = st.columns(5, gap="large")
with primary_results[1]:
  st.metric("Carry Cost on Land ($)", show_value(carry))

loan = total_aqui_cost + preco_total + construction_cost
bonus = loan * bonus_percent / 100

text_columns = st.columns([0.185, 0.815], gap="large")
with text_columns[1]:
  st.text("Loan Distribution (we only pay interests on what we take out)")

loan_params = st.columns(5, gap="large")
with loan_params[1]:
    loan_early = st.number_input("Early Stage (%)", min_value=0, max_value=100, value=50)
with loan_params[2]:
    loan_mid = st.number_input("Middle Stage (%)", min_value=0, max_value=100, value=30)
with loan_params[3]:
    loan_late = st.number_input("Late Stage (%)", min_value=0, max_value=100, value=100 - loan_early - loan_mid, disabled=True)

stage_interest = (interest_rate / 12) * (time / 3) / 100
interest = stage_interest * loan * (loan_early * 3 + loan_mid * 2 + loan_late) / 100
total_financing = carry_cost + bonus + surveyor + interest
contingency = (contingency_percent / 100) * (total_aqui_cost + preco_total + construction_cost)

st.text("")
interest_columns = st.columns(5, gap="large")
with interest_columns[1]:
  st.metric("Required Loan ($)", show_value(loan))
  st.metric("Total Financing ($)", show_value(total_financing))
with interest_columns[2]:
  st.metric("Interest ($)", show_value(interest))
  st.metric("Contingency ($)", show_value(contingency))
with interest_columns[3]:
  st.metric("Financing Bonus ($)", show_value(bonus))


st.header("Grand Total")

grand_total = loan + total_financing + contingency

grand_total_columns = st.columns(5, gap="large")
with grand_total_columns[1]:
  st.metric("Grand Total ($)", show_value(grand_total), border=True)


st.header("Home Costs")


home_cost_params = st.columns(5, gap="large")
with home_cost_params[1]:
  member_discounts = 1000 * st.slider("Member Discounts ($)", min_value=0, max_value=1000, value=500, step=10, format="%dk")
with home_cost_params[2]:
  realty_fee_percent = st.slider("Realty Transfer Fee (%)", min_value=0, max_value=5, value=1)

realty_fee = realty_fee_percent * grand_total / 100
total_home_costs = grand_total + member_discounts + realty_fee
home_costs_per_sf = total_home_costs / total_area

factor_small = 3 * size_small / (size_small + size_medium + size_large)
factor_medium = 3 * size_medium / (size_small + size_medium + size_large)
factor_large = 3 * size_large / (size_small + size_medium + size_large)

home_cost_small = factor_small * total_home_costs / n_units
home_cost_medium = factor_medium * total_home_costs / n_units
home_cost_large = factor_large * total_home_costs / n_units

home_cost_results = st.columns(5, gap="large")
with home_cost_results[1]:
  st.metric("Total Home Cost ($)", show_value(total_home_costs))
  st.metric("Home Cost Type I ($)", show_value(home_cost_small))
with home_cost_results[2]:
  st.metric("Home Cost per sf ($)", show_value(home_costs_per_sf))
  st.metric("Home Cost Type II ($)", show_value(home_cost_medium))
with home_cost_results[3]:
  st.metric("Average Home Cost ($)", show_value(total_home_costs / n_units))
  st.metric("Home Cost Type III ($)", show_value(home_cost_large))


