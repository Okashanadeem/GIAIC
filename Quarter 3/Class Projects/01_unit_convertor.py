import streamlit as st
import numpy as np

def length_conversion(value, from_unit, to_unit):
    # Dictionary of length conversion factors (to meters)
    length_factors = {
        'Meters': 1,
        'Kilometers': 1000,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Miles': 1609.34,
        'Yards': 0.9144,
        'Feet': 0.3048,
        'Inches': 0.0254
    }
    return value * length_factors[from_unit] / length_factors[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Dictionary of weight conversion factors (to kilograms)
    weight_factors = {
        'Kilograms': 1,
        'Grams': 0.001,
        'Milligrams': 0.000001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    return value * weight_factors[from_unit] / weight_factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32

def volume_conversion(value, from_unit, to_unit):
    # Dictionary of volume conversion factors (to liters)
    volume_factors = {
        'Liters': 1,
        'Milliliters': 0.001,
        'Gallons': 3.78541,
        'Quarts': 0.946353,
        'Pints': 0.473176,
        'Cups': 0.236588,
        'Fluid Ounces': 0.0295735
    }
    return value * volume_factors[from_unit] / volume_factors[to_unit]

def area_conversion(value, from_unit, to_unit):
    # Dictionary of area conversion factors (to square meters)
    area_factors = {
        'Square Meters': 1,
        'Square Kilometers': 1000000,
        'Square Centimeters': 0.0001,
        'Square Miles': 2589988.11,
        'Square Yards': 0.836127,
        'Square Feet': 0.092903,
        'Square Inches': 0.00064516,
        'Acres': 4046.86
    }
    return value * area_factors[from_unit] / area_factors[to_unit]

def main():
    st.title("Unit Converter")
    st.write("Convert between different units of measurement")

    # Create tabs for different conversion types
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Length", "Weight", "Temperature", "Volume", "Area"])

    with tab1:
        st.header("Length Conversion")
        col1, col2 = st.columns(2)
        with col1:
            length_value = st.number_input("Enter value", min_value=0.0, key="length_value")
            length_from = st.selectbox("From", ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Miles', 'Yards', 'Feet', 'Inches'], key="length_from")
        with col2:
            length_to = st.selectbox("To", ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Miles', 'Yards', 'Feet', 'Inches'], key="length_to")
        if st.button("Convert Length", key="length_button"):
            result = length_conversion(length_value, length_from, length_to)
            st.success(f"{length_value} {length_from} = {result:.4f} {length_to}")

    with tab2:
        st.header("Weight Conversion")
        col1, col2 = st.columns(2)
        with col1:
            weight_value = st.number_input("Enter value", min_value=0.0, key="weight_value")
            weight_from = st.selectbox("From", ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces'], key="weight_from")
        with col2:
            weight_to = st.selectbox("To", ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces'], key="weight_to")
        if st.button("Convert Weight", key="weight_button"):
            result = weight_conversion(weight_value, weight_from, weight_to)
            st.success(f"{weight_value} {weight_from} = {result:.4f} {weight_to}")

    with tab3:
        st.header("Temperature Conversion")
        col1, col2 = st.columns(2)
        with col1:
            temp_value = st.number_input("Enter value", key="temp_value")
            temp_from = st.selectbox("From", ['Celsius', 'Fahrenheit', 'Kelvin'], key="temp_from")
        with col2:
            temp_to = st.selectbox("To", ['Celsius', 'Fahrenheit', 'Kelvin'], key="temp_to")
        if st.button("Convert Temperature", key="temp_button"):
            result = temperature_conversion(temp_value, temp_from, temp_to)
            st.success(f"{temp_value}°{temp_from} = {result:.4f}°{temp_to}")

    with tab4:
        st.header("Volume Conversion")
        col1, col2 = st.columns(2)
        with col1:
            volume_value = st.number_input("Enter value", min_value=0.0, key="volume_value")
            volume_from = st.selectbox("From", ['Liters', 'Milliliters', 'Gallons', 'Quarts', 'Pints', 'Cups', 'Fluid Ounces'], key="volume_from")
        with col2:
            volume_to = st.selectbox("To", ['Liters', 'Milliliters', 'Gallons', 'Quarts', 'Pints', 'Cups', 'Fluid Ounces'], key="volume_to")
        if st.button("Convert Volume", key="volume_button"):
            result = volume_conversion(volume_value, volume_from, volume_to)
            st.success(f"{volume_value} {volume_from} = {result:.4f} {volume_to}")

    with tab5:
        st.header("Area Conversion")
        col1, col2 = st.columns(2)
        with col1:
            area_value = st.number_input("Enter value", min_value=0.0, key="area_value")
            area_from = st.selectbox("From", ['Square Meters', 'Square Kilometers', 'Square Centimeters', 'Square Miles', 'Square Yards', 'Square Feet', 'Square Inches', 'Acres'], key="area_from")
        with col2:
            area_to = st.selectbox("To", ['Square Meters', 'Square Kilometers', 'Square Centimeters', 'Square Miles', 'Square Yards', 'Square Feet', 'Square Inches', 'Acres'], key="area_to")
        if st.button("Convert Area", key="area_button"):
            result = area_conversion(area_value, area_from, area_to)
            st.success(f"{area_value} {area_from} = {result:.4f} {area_to}")

if __name__ == "__main__":
    main()
