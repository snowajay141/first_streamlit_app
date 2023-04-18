import streamlit

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast MENU')
streamlit.text('Omega3 & Blueberry Oatmeal')
streamlit.text('Kale Spinach & Rocket Smoothee')
streamlit.text('Hard boiled free range egg')
streamlit.header('Build your own fruit Smoothies')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

