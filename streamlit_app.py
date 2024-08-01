import streamlit as st
import pandas as pd
import math

# -----------------------------------------------------------------------------
# Declare some useful functions.



stats_per_prompt = get_stats_per_prompt()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
### :bar_chart: Tokens per second for each prompt
'''

st.bar_chart(stats_per_prompt.transpose().loc[:,"avg_tokens_per_second"], use_container_width=True)


