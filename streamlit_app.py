# init
import streamlit as sl
import pandas as pd

# var
f = 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

sl.text('hello')
lst = pd.read_csv(f)

lst = lst.set_index('Fruit')
sl.multiselect('pick:', list(lst.index))
sl.dataframe(lst)

### EOL
