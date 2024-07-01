import streamlit as st

# Combined pricing formula coefficients
slope_combined = 17.90  # Obtained from the linear regression model
intercept_combined = 612.24  # Obtained from the linear regression model

# Function to calculate new cost and price per sqft
def calculate_new_cost(width, height):
    area = width * height
    cost = slope_combined * area + intercept_combined
    price_per_sqft = cost / area
    return round(cost, 2), round(price_per_sqft, 2)

# Function to calculate old cost and price per sqft based on area tiers
def calculate_old_cost(width, height):
    area = width * height
    if 6 <= area <= 10:
        cost_per_sqft = 151
    elif 11 <= area <= 15:
        cost_per_sqft = 140
    elif 16 <= area <= 20:
        cost_per_sqft = 125
    elif 21 <= area <= 24:
        cost_per_sqft = 113
    else:
        return "Area out of bounds (6-24 sqft)", None

    cost = cost_per_sqft * area
    return round(cost, 2), round(cost_per_sqft, 2)

st.title('Window Pricing Calculator')

width = st.number_input('Width (sqft):', min_value=1.0, value=1.0)
height = st.number_input('Height (sqft):', min_value=1.0, value=1.0)

if st.button('Calculate'):
    new_cost, new_price_per_sqft = calculate_new_cost(width, height)
    old_cost, old_price_per_sqft = calculate_old_cost(width, height)
    if old_cost == "Area out of bounds (6-24 sqft)":
        st.write(old_cost)
    else:
        st.write(f"**New cost for {width} sqft x {height} sqft window:** ${new_cost} (Price per sqft: ${new_price_per_sqft})")
        st.write(f"**Old cost for {width} sqft x {height} sqft window:** ${old_cost} (Price per sqft: ${old_price_per_sqft})")