import streamlit as st
import json
import requests

# App description
st.markdown('''
# Currency Converter

- Source Code: https://github.com/steven-ngo/Currency-Converter
- Language: `Python`
- Libraries: `streamlit`
''')
st.write('---')

API_KEY = 'fca_live_KWw5BNQpWERkqxXNyJGnuGRpSgV7P9rTsx0ru8vK'
BASE_URL = 'https://api.freecurrencyapi.com/v1/'

currencies = requests.get(BASE_URL + 'currencies',
    params={'apikey': API_KEY}
).json()

options = list(currencies['data'].keys())

col1, col2, col3 = st.columns(3)

base = col1.selectbox(
   'Base Currency:',
   options,
   index=1,
)

target = col2.selectbox(
   'Target Currency:',
   options,
   index=0,
)

amount = col3.number_input('Amount:', value=1.00)


if st.button("Convert"):
   retrieveRate = requests.get(BASE_URL + 'latest',
            params={'apikey': API_KEY, 'base_currency':base ,'currencies': target}
   ).json()
   
   rate = list(retrieveRate['data'].values())[0]

   converted = amount * rate

   st.write(f"<h2> {str(amount)} {base} = {str(converted)} {target}</h2>",unsafe_allow_html=True)

st.table(currencies['data'])

