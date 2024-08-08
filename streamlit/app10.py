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
header_html = "<tr><th>Country</th>"
for activity in all_activities:
    header_html += f"<th>{activity}</th>"
header_html += "</tr>"

# Create the rows for each country
rows_html = ""
for country, info in categories_label.items():
    row_html = f"<tr><td>{country}</td>"
    for activity in all_activities:
        if activity in info["activities"]:
            row_html += "<td style='color: green;'>✅</td>"
        else:
            row_html += "<td></td>"
    row_html += "</tr>"
    rows_html += row_html

# Combine header and rows into a complete table
table_html = f"""
<table style='border-collapse: collapse; width: 100%;'>
    <thead style='border-bottom: 2px solid black;'>{header_html}</thead>
    <tbody>{rows_html}</tbody>
</table>
"""

# Display the table
st.markdown(table_html, unsafe_allow_html=True)

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