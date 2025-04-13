import streamlit as st

# Conversion logic functions
def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592
    }
    return value * units[from_unit] / units[to_unit]

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Miles": 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    return value

# Streamlit UI
st.title("🔁 Unit Converter")

conversion_type = st.selectbox("Select Conversion Type", ["Weight", "Length", "Temperature"])

if conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds"]
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Length":
    units = ["Meters", "Kilometers", "Miles"]
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter temperature", format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

        # At the end of your app, after all your main logic
st.write("Made with ❤️ by Hina Sher using Streamlit — thanks for using it!")
