import streamlit as st
import pandas as pd
import math
from pathlib import Path
from helpers.data_helpers import get_stats_per_prompt
'''
### :bar_chart: Tokens count for each prompt
'''

stats_per_prompt = get_stats_per_prompt()
st.bar_chart(stats_per_prompt.transpose().loc[:, "avg_tokens_count"])
