import streamlit as st
from serpapi import GoogleSearch

# Set your SerpAPI Key here
SERP_API_KEY = "2ecb5b7675d2ff7330c5c84da8ebc585b3a7e1b872b124059b01488806098f8f"

st.title("🔍 Google Search via Streamlit")

query = st.text_input("Search on Google:")

if query:
    st.write(f"Showing top results for: **{query}**")

    # SerpAPI parameters
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" in results:
        for result in results["organic_results"]:
            title = result.get("title")
            link = result.get("link")
            snippet = result.get("snippet", "")
            st.markdown(f"### [{title}]({link})\n{snippet}")
    else:
        st.error("No results found or API limit exceeded.")
