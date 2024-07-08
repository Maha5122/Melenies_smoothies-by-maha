# Import python packages
import streamlit as st

from snowflake.snowpark.functions import col
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruit you want in your custom smoothie! 
    """
)

#import streamlit as st

cnx = st.connection("snowflake")
session = cnx.session()


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect(
    'choose upto 5 ingredients:'
    ,my_dataframe
    ,max_selections = 5
)
if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string = ''
    name_on_order = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """','""" +name_on_order+ """')"""

    #st.write(my_insert_stmt)

    time_to_insert = st.button('Submit order')
    if time_to_insert:

        
        
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
