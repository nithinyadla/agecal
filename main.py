from datetime import datetime
import streamlit as st

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    st.title("Age Calculator")
    st.write("Enter your birth date to calculate your age")

    # Date input with reasonable defaults (18 years ago)
    default_date = datetime.now().replace(year=datetime.now().year - 18)
    birth_date = st.date_input("Select your birth date", value=default_date)

    if st.button("Calculate Age"):
        age = calculate_age(birth_date)
        st.success(f"Your age is: {age} years")
        
print("hello world")
for i in range()
  print(i)
    if:
        2>0:




if __name__ == "__main__":
    main()
