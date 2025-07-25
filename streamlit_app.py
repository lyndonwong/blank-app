import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Lyndon's hello streamlit app!")
st.write(
    "v2 adds various widgets and interactive elements. "
)

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060]
})
 
## Create a map with the data
st.map(data, zoom=1)

"""
### Continue with streamlit get-started guide Basic Concepts
Create a table with data:    
"""

df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

# write table manually as well
st.write(df)

# writing an interactive table

dataframe = np.random.randn(5,7)
st.dataframe(dataframe)

# interactive table that highlights minimum values in each column

st.subheader("Interactive Table that highlights minimum values in each column") 

dataframe = pd.DataFrame(
    np.random.randn(11, 17),
    columns=('col %d' % i for i in range(17)),
    index=('row %d' % i for i in range(11))      
)   

st.dataframe(dataframe.style.highlight_min(axis=0)) 

# generate static table with st.table function
st.subheader("Static Table Example")    

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe) 

# Draw a line chart

st.subheader("Line Chart Example")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['apha', 'beta', 'gamma']
)   

st.line_chart(chart_data)

# display table for above chart
st.text("Data table for above chart")
st.dataframe(chart_data)

# display table conditionally based on a checkbox
if st.checkbox('Show data table'):
    st.subheader("Conditional Data table for above chart")
    st.dataframe(chart_data)  



# Plot a map
st.subheader("Map Plot")
map_data = pd.DataFrame(
    np.random.randn(80, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)    

st.caption("Map data is generated randomly, so it will change every time you refresh the page.")
st.subheader("Lat Lon data table for above map")
st.dataframe(map_data)

# add some cool widgets
st.header("Cool Widgets")   

# Collect and store visitor's name in session state 
st.text_input("What is your name?", "Type here...", key="name_input")
guest_name = st.session_state.name_input
st.write(f"Hello {guest_name}, welcome to my first streamlit app!") 

st.subheader("Mood Selector")
scale = 100
start = 0
default = 50
st.write(f'How do you feel today? (0 = sad, {scale} = happy)') 
x = st.slider('Set the sliding scale:', start, scale, default)
# Address visitor by name and share their mood
st.write(f'{guest_name}, your mood is: {x} out of {scale}')

st.subheader("Pet Survey")
x = st.selectbox('What makes the best family pet?', ['Budgie', 'Cat', 'Hamster', 'Dog', 'Goldfish'])
st.write(f'The best pet is a {x}')    

st.subheader("Number Squarer")  
x = st.slider('x')
st.write(x, 'squared is', x * x)

# Add some checkboxes
st.subheader("Reveal the table with a checkbox")

if st.checkbox('Check box to show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.caption("Your check is my command!")
    st.dataframe(chart_data)

# Try selectbox widget
st.subheader("Pick your potion below")
df = pd.DataFrame({
    'drink_type': ['Coffee', 'Tea', 'Coke', 'Juice'],
    'second column': [10, 20, 30, 40]
})
option = st.selectbox(
    'Which drink do you like best?',
    df['drink_type'])     

st.write(f"**I must agree, {option} is a nice drink!**")


