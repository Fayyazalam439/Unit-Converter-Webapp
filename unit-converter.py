import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # 1 kilometer = 1000 meter  
        "grams_kilograms": 0.001, # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000, # 1 kilograms = 1000 gram
        "minutes_seconds": 60,  # 1 minute = 60 seconds
        "seconds_minutes": 1/60  # 1 second = 1/60 minutes
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions: 
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

st.title("🌍Unit Converter")

st.write("#### 🎯 Welcome! Select a Unit Category, Enter a value and get the converted unit result")

value = st.number_input("Enter the value:", min_value= 1.0, step= 1.0 )

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms", "minutes", "seconds"])

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms", "minutes", "seconds"])

if st.button("🤖 Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value 🎉: {result}")