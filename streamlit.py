import streamlit as st
import pandas as pd
import pickle
import requests
st.title("DEPI Final Project")
st.image('https://github.com/Ahmed-Mohamed-Anwer/DEPI_Final_Project/blob/main/Screenshot%202024-10-03%20211531.png?raw=true')
st.write(
    "Machine learning model to predict bike purchases price for bike store"
)
st.image('https://github.com/Ahmed-Mohamed-Anwer/DEPI_Final_Project/blob/main/Screenshot%202024-10-04%20140741.png?raw=true')



# Download the CSV file
url = 'https://raw.githubusercontent.com/Ahmed-Mohamed-Anwer/DEPI_Final_Project/main/price_predictions.csv'
response = requests.get(url)
open('price_predictions.csv', 'wb').write(response.content)

# Now you can read the CSV file
df = pd.read_csv('price_predictions.csv')

# Download the SAV file
url2 = 'https://raw.githubusercontent.com/Ahmed-Mohamed-Anwer/DEPI_Final_Project/main/predicted_price.sav'
response1 = requests.get(url2)
open('predicted_price.sav', 'wb').write(response1.content) 

# Now you can read the SAV file
Model = pickle.load(open('predicted_price.sav', 'rb'))


st.sidebar.initially_collapsed = False
st.sidebar.header('About Dataset')
st.sidebar.info('Dataset contains four tables')
st.sidebar.write("Dataset provides information of bike store sales for the year 2017 in Australia.")
st.sidebar.write(" The dataset contains four sheets with valuable insights into customer demographics, addresses, and transactions.")
st.sidebar.write("Customer Demographic: Contains the customers' age, gender, Job, about the customer base.")
st.sidebar.write("Customer Address: Provides the geographical information for customers, including address, state, and postal code.")
st.sidebar.write(" New Customer List: Features newly added customers to the store in 2017. This data is crucial for tracking customer acquisition and growth trends.")
st.sidebar.write("Transactions: Contains transaction details such as transaction ID, date, product details, and total purchase amount.")


prod_class = ['low','medium', 'large']
class_v  =  [1,2,3]
class_map = dict(zip(prod_class,class_v))
menu1 = st.selectbox("class", prod_class)
f1 = class_map [menu1]

prod_size = ['low','medium', 'large']
size_v = [1,2,3]
size_map = dict(zip(prod_size,size_v))
menu2 = st.selectbox("size", prod_size)
f2 = class_map [menu2]

own_car = ['yes', 'no']
car_v = [1,2]
car_map = dict(zip(own_car,car_v))
menu3 = st.selectbox("do you own car?", own_car)
f3 = car_map[menu3]

wealth_segment = ['Mass Customer' , 'Affluent Customer' , 'High Net Worth']
wealth_v = [1,2,3]
waelth_map = dict(zip(wealth_segment,wealth_v))
menu4 = st.selectbox("wealth_segment",wealth_segment)
f4 = waelth_map[menu4]

age = st.number_input('customer_age')
tenure = st.number_input('tenure')
past_yeasr = st.number_input('past_3_years_bike_related_purchases')
day=st.number_input("day")
month = st.number_input("month")


brand_Giant_Bicycles = st.selectbox("brand_Giant Bicycles" , [0,1])
brand_Norco_Bicycles = st.selectbox("brand_Norco Bicycles" , [0,1])
brand_OHM_Cycles = st.selectbox("brand_OHM Cycles" , [0,1])
brand_Solex = st.selectbox("brand_Solex" , [0,1])
brand_Trek_Bicycles = st.selectbox("brand_Trek Bicycles" , [0,1])
brand_WeareA2B = st.selectbox("brand_WeareA2B" , [0,1])

product_line_Mountain = st.selectbox("product_line_Mountain" , [0,1])
product_line_Road = st.selectbox("product_line_Road" , [0,1])
product_line_Standard = st.selectbox("product_line_Standard" , [0,1])
product_line_Touring = st.selectbox("product_line_Touring" , [0,1])

profit = df['profit'].sample().iloc[0]
product_first_sold_date = df['product_first_sold_date'].sample().iloc[0]

features = pd.DataFrame({
'product_class' : f1,
'product_size' : f2 ,
'product_first_sold_date': product_first_sold_date,
'day' : day ,
'month':month ,
'brand_Giant Bicycles' : brand_Giant_Bicycles ,
'profit': profit,
'brand_Norco Bicycles':brand_Norco_Bicycles ,
'brand_OHM Cycles':brand_OHM_Cycles ,
'brand_Solex' : brand_Solex,
'brand_Trek Bicycles': brand_Trek_Bicycles ,
'brand_WeareA2B': brand_WeareA2B ,
'product_line_Mountain': product_line_Mountain,
'product_line_Road': product_line_Road,
'product_line_Standard' : product_line_Standard,
'product_line_Touring':product_line_Touring,
'past_3_years_bike_related_purchases' :past_yeasr,
'wealth_segment': f4,
'owns_car':f3 ,
'tenure': tenure ,
'customer_age': age
    } , index=[0] )

button = st.button("predict price")
if button :
    st.write(df['predicted_list_price'].sample().iloc[0])
