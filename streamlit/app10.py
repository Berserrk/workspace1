import streamlit as st
import json

# Load the JSON data from the file
with open('categories_label.json', 'r') as f:
    categories_label = json.load(f)

# Extract the list of activities
all_activities = set()
for country_info in categories_label.values():
    all_activities.update(country_info["activities"])

all_activities = sorted(all_activities)

# Create a table with countries as rows and activities as columns
st.header("Activities Table")

# Create the header row
header_cols = st.columns(len(all_activities) + 1)
header_cols[0].write("Country")
for i, activity in enumerate(all_activities):
    header_cols[i + 1].write(activity)

# Create the rows for each country
for country, info in categories_label.items():
    row_cols = st.columns(len(all_activities) + 1)
    row_cols[0].write(country)
    for i, activity in enumerate(all_activities):
        if activity in info["activities"]:
            row_cols[i + 1].markdown("✅", unsafe_allow_html=True)
        else:
            row_cols[i + 1].write("")

# Define the scroll operation as a function and pass in something unique for each
# page load that it needs to re-evaluate where "bottom" is
import time
js = f"""
<script>
    function scroll(dummy_var_to_force_repeat_execution){{
        setTimeout(function(){{
            // Select all 'section.main' elements on the page
            var textAreas = parent.document.querySelectorAll('section.main');
            for (let index = 0; index < textAreas.length; index++) {{
                // Scroll to the bottom of each 'section.main' element
                textAreas[index].scrollTop = textAreas[index].scrollHeight;
            }}
        }}, 1000);  // Delay of 1 second
    }}
    // Call the scroll function with the current time in milliseconds as an argument
    scroll({int(time.time() * 1000)})
</script>
"""

# Insert the JavaScript code into the page and set the height of the component to 0 to hide it
st.components.v1.html(js, height=0)