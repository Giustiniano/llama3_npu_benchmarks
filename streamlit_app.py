import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_stats_per_prompt():
    """Grab benchmark data from a JSON file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/stats_per_prompt.json'
    return pd.read_json(DATA_FILENAME)


stats_per_prompt = get_stats_per_prompt()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
### :bar_chart: Tokens per second for each prompt
'''

st.bar_chart(stats_per_prompt.transpose().loc[:,"avg_tokens_per_second"], use_container_width=True)

'''
### :bar_chart: Tokens count for each prompt
'''

st.bar_chart(stats_per_prompt.transpose().loc[:, "avg_tokens_count"])

