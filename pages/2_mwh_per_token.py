import streamlit as st
import pandas as pd
from helpers.data_helpers import get_stats_per_prompt
import altair as alt

stats_per_prompt = get_stats_per_prompt()

'''
### :bar_chart: mWh per token for each prompt :battery:
'''

st.bar_chart(stats_per_prompt.loc[:,"avg_mWh_per_token"])
