import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
import pickle
import streamlit as st
import plotly.express as px
st.header("Banglore House Price Prediction")
location = st.selectbox('Location', ('1st Block Jayanagar',
 '1st Phase JP Nagar',
 '2nd Phase Judicial Layout',
 '2nd Stage Nagarbhavi',
 '5th Block Hbr Layout',
 '5th Phase JP Nagar',
 '6th Phase JP Nagar',
 '7th Phase JP Nagar',
 '8th Phase JP Nagar',
 '9th Phase JP Nagar',
 'AECS Layout',
 'Abbigere',
 'Akshaya Nagar',
 'Ambalipura',
 'Ambedkar Nagar',
 'Amruthahalli',
 'Anandapura',
 'Ananth Nagar',
 'Anekal',
 'Anjanapura',
 'Ardendale',
 'Arekere',
 'Attibele',
 'BEML Layout',
 'BTM 2nd Stage',
 'BTM Layout',
 'Babusapalaya',
 'Badavala Nagar',
 'Balagere',
 'Banashankari',
 'Banashankari Stage II',
 'Banashankari Stage III',
 'Banashankari Stage V',
 'Banashankari Stage VI',
 'Banaswadi',
 'Banjara Layout',
 'Bannerghatta',
 'Bannerghatta Road',
 'Basavangudi',
 'Basaveshwara Nagar',
 'Battarahalli',
 'Begur',
 'Begur Road',
 'Bellandur',
 'Benson Town',
 'Bharathi Nagar',
 'Bhoganhalli',
 'Billekahalli',
 'Binny Pete',
 'Bisuvanahalli',
 'Bommanahalli',
 'Bommasandra',
 'Bommasandra Industrial Area',
 'Bommenahalli',
 'Brookefield',
 'Budigere',
 'CV Raman Nagar',
 'Chamrajpet',
 'Chandapura',
 'Channasandra',
 'Chikka Tirupathi',
 'Chikkabanavar',
 'Chikkalasandra',
 'Choodasandra',
 'Cooke Town',
 'Cox Town',
 'Cunningham Road',
 'Dasanapura',
 'Dasarahalli',
 'Devanahalli',
 'Devarachikkanahalli',
 'Dodda Nekkundi',
 'Doddaballapur',
 'Doddakallasandra',
 'Doddathoguru',
 'Domlur',
 'Dommasandra',
 'EPIP Zone',
 'Electronic City',
 'Electronic City Phase II',
 'Electronics City Phase 1',
 'Frazer Town',
 'GM Palaya',
 'Garudachar Palya',
 'Giri Nagar',
 'Gollarapalya Hosahalli',
 'Gottigere',
 'Green Glen Layout',
 'Gubbalala',
 'Gunjur',
 'HAL 2nd Stage',
 'HBR Layout',
 'HRBR Layout',
 'HSR Layout',
 'Haralur Road',
 'Harlur',
 'Hebbal',
 'Hebbal Kempapura',
 'Hegde Nagar',
 'Hennur',
 'Hennur Road',
 'Hoodi',
 'Horamavu Agara',
 'Horamavu Banaswadi',
 'Hormavu',
 'Hosa Road',
 'Hosakerehalli',
 'Hoskote',
 'Hosur Road',
 'Hulimavu',
 'ISRO Layout',
 'ITPL',
 'Iblur Village',
 'Indira Nagar',
 'JP Nagar',
 'Jakkur',
 'Jalahalli',
 'Jalahalli East',
 'Jigani',
 'Judicial Layout',
 'KR Puram',
 'Kadubeesanahalli',
 'Kadugodi',
 'Kaggadasapura',
 'Kaggalipura',
 'Kaikondrahalli',
 'Kalena Agrahara',
 'Kalyan nagar',
 'Kambipura',
 'Kammanahalli',
 'Kammasandra',
 'Kanakapura',
 'Kanakpura Road',
 'Kannamangala',
 'Karuna Nagar',
 'Kasavanhalli',
 'Kasturi Nagar',
 'Kathriguppe',
 'Kaval Byrasandra',
 'Kenchenahalli',
 'Kengeri',
 'Kengeri Satellite Town',
 'Kereguddadahalli',
 'Kodichikkanahalli',
 'Kodigehaali',
 'Kodigehalli',
 'Kodihalli',
 'Kogilu',
 'Konanakunte',
 'Koramangala',
 'Kothannur',
 'Kothanur',
 'Kudlu',
 'Kudlu Gate',
 'Kumaraswami Layout',
 'Kundalahalli',
 'LB Shastri Nagar',
 'Laggere',
 'Lakshminarayana Pura',
 'Lingadheeranahalli',
 'Magadi Road',
 'Mahadevpura',
 'Mahalakshmi Layout',
 'Mallasandra',
 'Malleshpalya',
 'Malleshwaram',
 'Marathahalli',
 'Margondanahalli',
 'Marsur',
 'Mico Layout',
 'Munnekollal',
 'Murugeshpalya',
 'Mysore Road',
 'NGR Layout',
 'NRI Layout',
 'Nagarbhavi',
 'Nagasandra',
 'Nagavara',
 'Nagavarapalya',
 'Narayanapura',
 'Neeladri Nagar',
 'Nehru Nagar',
 'OMBR Layout',
 'Old Airport Road',
 'Old Madras Road',
 'Padmanabhanagar',
 'Pai Layout',
 'Panathur',
 'Parappana Agrahara',
 'Pattandur Agrahara',
 'Poorna Pragna Layout',
 'Prithvi Layout',
 'R.T. Nagar',
 'Rachenahalli',
 'Raja Rajeshwari Nagar',
 'Rajaji Nagar',
 'Rajiv Nagar',
 'Ramagondanahalli',
 'Ramamurthy Nagar',
 'Rayasandra',
 'Sahakara Nagar',
 'Sanjay nagar',
 'Sarakki Nagar',
 'Sarjapur',
 'Sarjapur  Road',
 'Sarjapura - Attibele Road',
 'Sector 2 HSR Layout',
 'Sector 7 HSR Layout',
 'Seegehalli',
 'Shampura',
 'Shivaji Nagar',
 'Singasandra',
 'Somasundara Palya',
 'Sompura',
 'Sonnenahalli',
 'Subramanyapura',
 'Sultan Palaya',
 'TC Palaya',
 'Talaghattapura',
 'Thanisandra',
 'Thigalarapalya',
 'Thubarahalli',
 'Tindlu',
 'Tumkur Road',
 'Ulsoor',
 'Uttarahalli',
 'Varthur',
 'Varthur Road',
 'Vasanthapura',
 'Vidyaranyapura',
 'Vijayanagar',
 'Vishveshwarya Layout',
 'Vishwapriya Layout',
 'Vittasandra',
 'Whitefield',
 'Yelachenahalli',
 'Yelahanka',
 'Yelahanka New Town',
 'Yelenahalli',
 'Yeshwanthpur'))
bath = st.slider('No. of Bathrooms in the House', 1, 13, 1)
bhk = st.slider('No. of Bedrooms in the House', 1, 13, 1)
sqft = st.number_input('Build Up Area(Square Feet)', 200, 20000)
df = pd.read_csv("BHP_cleaned.csv")

df.head()

X = df.drop(['price'], axis='columns')
X.head(3)

y = df.price
y.head()

len(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=10)

from sklearn.linear_model import LinearRegression
lr_clf = LinearRegression()
lr_clf.fit(X_train,y_train)
lr_clf.score(X_test,y_test)
def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return lr_clf.predict([x])[0]
if st.button("Estimate Price"):
    prediction = predict_price(location,sqft,bath,bhk)
    pred = int(prediction)
    st.subheader(str(pred) + " " + "**Lakhs**")
chart_data = df
fig1 = px.scatter(chart_data, x = 'total_sqft', y = 'price', hover_data = ['total_sqft', 'price'], labels = {'total_sqft': 'Area in Square Feet', 'price': 'House Price (In Lakhs)'}, height = 600, width = 600)
st.write(fig1)
if st.checkbox("Show Raw Data", False):
    df1 = pd.read_csv("bengaluru_house_prices.csv")
    st.dataframe(df1)
