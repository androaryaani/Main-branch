import streamlit as st
import requests
from datetime import datetime

# Set up Streamlit UI
st.set_page_config(page_title="Website Data Downloader", layout="centered")
st.title("🌐 Website Data Downloader")
st.markdown("Enter a URL, choose a format, and download the content.")

# Input fields
url = st.text_input("🔗 Enter Website URL", "https://example.com")

format_option = st.selectbox("💾 Select Download Format", ["txt", "html", "json"])

def download_website_data(url, format_choice):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None, f"❌ Failed to fetch data. Status code: {response.status_code}"

        content = response.text
        filename = f"website_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{format_choice}"

        # Format-specific handling
        if format_choice == "txt":
            data = content
        elif format_choice == "html":
            data = content
        elif format_choice == "json":
            try:
                data = response.json()
            except Exception:
                return None, "❌ The response is not valid JSON."
        else:
            return None, "❌ Unsupported format selected."

        return data, filename

    except Exception as e:
        return None, f"❌ Error occurred: {e}"

# Button click
if st.button("📥 Fetch & Download"):
    with st.spinner("Downloading..."):
        data, result = download_website_data(url, format_option)

        if data:
            st.success("✅ Website content downloaded successfully!")

            if format_option == "json":
                st.json(data)
                st.download_button("⬇️ Download JSON", data=str(data), file_name=result, mime="application/json")
            elif format_option == "html":
                st.code(data[:1000], language="html")
                st.download_button("⬇️ Download HTML", data=data, file_name=result, mime="text/html")
            else:  # txt
                st.text_area("📄 Preview (first 1000 chars)", value=data[:1000], height=200)
                st.download_button("⬇️ Download TXT", data=data, file_name=result, mime="text/plain")

        else:
            st.error(result)
