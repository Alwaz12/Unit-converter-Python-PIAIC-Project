import streamlit as st
import pandas as pd
from datetime import datetime

# Temperature Converter
def temperature_converter(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

# Length Converter
def length_converter(value, from_unit, to_unit):
    # Convert everything to meters first
    conversions = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    meters = value * conversions[from_unit]
    return meters / conversions[to_unit]

# Area Converter
def area_converter(value, from_unit, to_unit):
    # Convert everything to square meters first
    conversions = {
        "Square Meter": 1,
        "Square Kilometer": 1000000,
        "Square Mile": 2590000,
        "Square Yard": 0.836127,
        "Square Foot": 0.092903,
        "Acre": 4046.86,
        "Hectare": 10000
    }
    sq_meters = value * conversions[from_unit]
    return sq_meters / conversions[to_unit]

# Volume Converter
def volume_converter(value, from_unit, to_unit):
    # Convert everything to liters first
    conversions = {
        "Liter": 1,
        "Milliliter": 0.001,
        "Cubic Meter": 1000,
        "Gallon": 3.78541,
        "Quart": 0.946353,
        "Pint": 0.473176,
        "Cup": 0.236588
    }
    liters = value * conversions[from_unit]
    return liters / conversions[to_unit]

# Mass Converter
def mass_converter(value, from_unit, to_unit):
    # Convert everything to kilograms first
    conversions = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    kg = value * conversions[from_unit]
    return kg / conversions[to_unit]

# Speed Converter
def speed_converter(value, from_unit, to_unit):
    # Convert everything to meters per second first
    conversions = {
        "Meters per second": 1,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444
    }
    mps = value * conversions[from_unit]
    return mps / conversions[to_unit]

# Time Converter
def time_converter(value, from_unit, to_unit):
    # Convert everything to seconds first
    conversions = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2592000,  # Assuming 30 days
        "Year": 31536000  # Assuming 365 days
    }
    seconds = value * conversions[from_unit]
    return seconds / conversions[to_unit]

# Frequency Converter
def frequency_converter(value, from_unit, to_unit):
    # Convert everything to Hertz first
    conversions = {
        "Hertz": 1,
        "Kilohertz": 1000,
        "Megahertz": 1000000,
        "Gigahertz": 1000000000
    }
    hertz = value * conversions[from_unit]
    return hertz / conversions[to_unit]

# Data Transfer Rate Converter
def data_transfer_converter(value, from_unit, to_unit):
    # Convert everything to bits first
    conversions = {
        "Bit": 1,
        "Byte": 8,
        "Kilobyte": 8 * 1024,
        "Megabyte": 8 * 1024 * 1024,
        "Gigabyte": 8 * 1024 * 1024 * 1024,
        "Terabyte": 8 * 1024 * 1024 * 1024 * 1024
    }
    bits = value * conversions[from_unit]
    return bits / conversions[to_unit]

# Pressure Converter
def pressure_converter(value, from_unit, to_unit):
    # Convert everything to Pascal first
    conversions = {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325
    }
    pascal = value * conversions[from_unit]
    return pascal / conversions[to_unit]

# Fuel Economy Converter
def fuel_economy_converter(value, from_unit, to_unit):
    # Convert everything to kilometers per liter first
    conversions = {
        "Kilometers per liter": 1,
        "Miles per gallon": 0.425144,
        "Liters per 100 kilometers": lambda x: 100/x if x != 0 else float('inf')
    }
    
    if from_unit == "Liters per 100 kilometers":
        kpl = 100/value if value != 0 else float('inf')
    else:
        kpl = value * conversions[from_unit]
    
    if to_unit == "Liters per 100 kilometers":
        return 100/kpl if kpl != 0 else float('inf')
    return kpl / conversions[to_unit]

# Plane Angle Converter
def plane_angle_converter(value, from_unit, to_unit):
    # Convert everything to radians first
    conversions = {
        "Radian": 1,
        "Degree": 0.0174533,
        "Gradian": 0.015708,
        "Milliradian": 0.001
    }
    radians = value * conversions[from_unit]
    return radians / conversions[to_unit]

def main():
    st.set_page_config(
        page_title="Universal Unit Converter",
        page_icon="🔄"
    )
    
    # Add custom CSS for styling
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #2c3e50;
            font-size: 3rem !important;
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔄 Universal Unit Converter")
    
    # Create a dictionary of conversion types and their units with emojis
    conversion_types = {
        "Temperature 🌡️": ["Celsius", "Fahrenheit", "Kelvin"],
        "Length 📏": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "Area 📐": ["Square Meter", "Square Kilometer", "Square Mile", "Square Yard", "Square Foot", "Acre", "Hectare"],
        "Volume 🧊": ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Quart", "Pint", "Cup"],
        "Mass ⚖️": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
        "Speed 🏃": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"],
        "Time ⏰": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "Frequency 📻": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
        "Data Transfer Rate 💾": ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
        "Pressure 🌪️": ["Pascal", "Kilopascal", "Bar", "PSI", "Atmosphere"],
        "Fuel Economy ⛽": ["Kilometers per liter", "Miles per gallon", "Liters per 100 kilometers"],
        "Plane Angle 📐": ["Radian", "Degree", "Gradian", "Milliradian"]
    }
    
    # Update conversion functions dictionary keys to match new emoji keys
    conversion_functions = {
        "Temperature 🌡️": temperature_converter,
        "Length 📏": length_converter,
        "Area 📐": area_converter,
        "Volume 🧊": volume_converter,
        "Mass ⚖️": mass_converter,
        "Speed 🏃": speed_converter,
        "Time ⏰": time_converter,
        "Frequency 📻": frequency_converter,
        "Data Transfer Rate 💾": data_transfer_converter,
        "Pressure 🌪️": pressure_converter,
        "Fuel Economy ⛽": fuel_economy_converter,
        "Plane Angle 📐": plane_angle_converter
    }
    
    # Add some space and a divider
    st.markdown("---")
    
    # Create the sidebar for conversion type selection with a nice header
    st.sidebar.markdown("## 🛠️ Select Conversion Type")
    conversion_type = st.sidebar.selectbox(
        "",  # Empty label since we have the header above
        list(conversion_types.keys())
    )
    
    # Add conversion formulas in the sidebar
    st.sidebar.markdown("### 📝 Common Formulas")
    formulas = {
        "Temperature 🌡️": """
        - Celsius to Fahrenheit: °F = (°C × 9/5) + 32
        - Fahrenheit to Celsius: °C = (°F - 32) × 5/9
        - Kelvin to Celsius: °C = K - 273.15
        """,
        "Length 📏": """
        - 1 meter = 100 centimeters
        - 1 kilometer = 1000 meters
        - 1 mile = 1.60934 kilometers
        - 1 foot = 0.3048 meters
        """,
        "Area 📐": """
        - 1 square meter = 10.764 square feet
        - 1 acre = 4046.86 square meters
        - 1 hectare = 10000 square meters
        - 1 square mile = 2.59 square kilometers
        """,
        "Volume 🧊": """
        - 1 liter = 1000 milliliters
        - 1 gallon = 3.78541 liters
        - 1 cubic meter = 1000 liters
        - 1 cup = 236.588 milliliters
        """,
        "Mass ⚖️": """
        - 1 kilogram = 1000 grams
        - 1 pound = 0.453592 kilograms
        - 1 ounce = 28.3495 grams
        - 1 metric ton = 1000 kilograms
        """,
        "Speed 🏃": """
        - 1 km/h = 0.277778 m/s
        - 1 mph = 1.60934 km/h
        - 1 knot = 1.852 km/h
        - 1 m/s = 3.6 km/h
        """,
        "Time ⏰": """
        - 1 hour = 60 minutes
        - 1 minute = 60 seconds
        - 1 day = 24 hours
        - 1 week = 7 days
        """,
        "Frequency 📻": """
        - 1 kHz = 1000 Hz
        - 1 MHz = 1000 kHz
        - 1 GHz = 1000 MHz
        - Period = 1/frequency
        """,
        "Data Transfer Rate 💾": """
        - 1 Byte = 8 bits
        - 1 KB = 1024 bytes
        - 1 MB = 1024 KB
        - 1 GB = 1024 MB
        """,
        "Pressure 🌪️": """
        - 1 bar = 100,000 Pascal
        - 1 atm = 101,325 Pascal
        - 1 PSI = 6,894.76 Pascal
        - 1 kPa = 1000 Pascal
        """,
        "Fuel Economy ⛽": """
        - MPG to L/100km: L/100km = 235.215/MPG
        - km/L to MPG: MPG = km/L × 2.35215
        - L/100km to km/L: km/L = 100/(L/100km)
        """,
        "Plane Angle 📐": """
        - 1 radian = 57.2958 degrees
        - 1 degree = 0.0174533 radians
        - 1 gradian = 0.9 degrees
        - Full circle = 360° = 2π radians
        """
    }
    
    # Display the formula for the selected conversion type
    st.sidebar.markdown(formulas[conversion_type])
    
    # Add a divider in sidebar
    st.sidebar.markdown("---")
    
    # Add a note about precision
    st.sidebar.markdown("""
    ℹ️ **Note:** Formulas shown are approximate. 
    The converter uses precise conversion factors.
    """)
    
    # Get the available units for the selected conversion type
    units = conversion_types[conversion_type]
    
    # Create three columns for the input value and unit selections
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Enter Value")
        value = st.number_input("", value=0.0)
        
    with col2:
        st.markdown("### From Unit")
        from_unit = st.selectbox("", units, key="from_unit")
        
    with col3:
        st.markdown("### To Unit")
        to_unit = st.selectbox("", units, key="to_unit")
    
    # Add some space before the convert button
    st.markdown("")
    
    # Center the convert button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        convert_button = st.button("🔄 Convert")
    
    # Perform the conversion
    if convert_button:
        try:
            result = conversion_functions[conversion_type](value, from_unit, to_unit)
            # Create a nice box for the result
            st.markdown("### Result:")
            st.markdown(
                f"""
                <div style="padding: 1rem; border-radius: 0.5rem; background-color: #e8f4ea; text-align: center;">
                    <h3 style="color: #28a745;">{value} {from_unit} = {result:.6f} {to_unit}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
    
    # Add footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #666;">
            Universal Unit Converter Made By Nazia Imran
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()