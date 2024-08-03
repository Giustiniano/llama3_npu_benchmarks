import streamlit as st
import pandas as pd
from helpers.data_helpers import get_stats_per_prompt, get_stats_per_prompt_battery
import altair as alt

stats_per_prompt = get_stats_per_prompt()
stats_per_prompt_battery = get_stats_per_prompt_battery()

'''
### :bar_chart: Tokens per second for each prompt :electric_plug: vs :battery:
'''

st.bar_chart(stats_per_prompt.loc[:,["avg_tokens_per_second", "avg_tokens_per_second_battery"]])
