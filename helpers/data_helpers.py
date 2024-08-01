import streamlit as st
import pandas as pd
from pathlib import Path

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
