import streamlit as st

# 1- Unit Converter Application
# 2- Input for Unit Converter Application
# 3- Output Given By Unit Converter Application

# Inputs
# 1 - Value
# 2 - Unit From Conversion / Kis Unit Se Convert Karna Hai
# 3 - Unit To Conversion / Kis Unit Me Convert Karna Hai

# Value Unit_From Unit_To
# 20000 Meter   Kilometer

# Output
# Converted Value in Preferred Unit Type
# Floating Point Value = 2.0 / 1.5


#                       2.0 / 1.5
def convert_units(value: float, unit_from: str, unit_to: str):
    #    print("Value>>>",value)
    #    print("Unit_From>>>",unit_from)
    #    print("Unit_To>>>",unit_to)

    # 1 Kilometer = 1000 Meters
    # 1 Meter = 0.001 Kilometer
    # 1 Kilogram = 1000 Grams
    # 1 Gram = 0.001 Kilogram
    # Value Ho Kilometers Men or Value Convert Karni Ho Meters Main
    if unit_from == "Kilometers" and unit_to == "Meters":
        # 1.5 * 1000
        return value * 1000
    elif unit_from == "Meters" and unit_to == "Kilometers":
        #       1 * 0.001 = 0.001 Kilometer
        return value * 0.001
    elif unit_from == "KIlograms" and unit_to == "Grams":
        #       2    * 1000 = 2000
        return value * 1000
    elif unit_from == "Grams" and unit_to == "Kilograms":
        return value * 0.001
    else:
        return "Conversion is Not Supported!"


# Result = Output Ki Value
# result1 = convert_units(1.5, "Kilometers","Meters")
# print("The Result in Meters is",result1)
# result2 = convert_units(5000,"Grams","Kilograms")
# print("The Value in Kilograms is", result2)


def main():
    st.title("🌍Unit Converter App")
    st.header("Welcome to Unit Converter!")

    value = st.number_input("Enter The Value You Want to Convert:", min_value=0.0)
    unit_to = st.text_input("Enter The Unit You Want to Convert From(e.g Kilometers, Meters, Kilograms,Grams):")
    unit_from = st.text_input("Enter The Unit You Want to Conversion (e.g Kilometers, Meters, Kilograms,Grams):")

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write("Converted Value is:", result)


#    print("Unit Converter")
#    print("Welcome to Unit Converter!")

#    value = float(input("Enter The Value You Want to Convert:")) # 1 -> 1.5
#    unit_to = input("Enter The Unit You Want to Convert From(e.g Kilometers, Meters, Kilograms,Grams):")
#    unit_from = input("Enter The Unit You Want to Conversion (e.g Kilometers, Meters, Kilograms,Grams):")

#    print("Value>>>",value)
#    print("Unit_From>>>",unit_from)
#    print("Unit_To>>>",unit_to)
#    result = convert_units(value, unit_from, unit_to)
#    print("Converted Value is :", result)


main()
