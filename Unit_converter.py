import streamlit as st

st.title("Unit Converter App")
st.markdown("### Convert Lenght, Weight and Time Instantly")
st.write("##### Welcome! Select  a category, enter the value and click convert to get the result in real time project.")

category = st.selectbox("Choose a Category", ["Lenght", "Weight", "Time",])

def convert_units(category, value, unit):
    if category == "Lenght":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
    
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0
        
if category == "Lenght":
    unit = st.selectbox("Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")