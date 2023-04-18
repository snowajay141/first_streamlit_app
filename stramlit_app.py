import streamlit

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast MENU')
streamlit.text('Omega3 & Blueberry Oatmeal')
streamlit.text('Kale Spinach & Rocket Smoothee')
streamlit.text('Hard boiled free range egg')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
