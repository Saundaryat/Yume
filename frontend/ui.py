import streamlit as st
import requests
import json
import ast
import pandas as pd

st.set_page_config(page_title="Estetica")

# Load configuration
with open('config/config.json') as config_file:
    config = json.load(config_file)
BASE_URL = config['BASE_URL']

# Load resources
@st.cache_resource
def get_products():
    products = []
    df = pd.read_csv('data/catalog_ts_is.csv')
    for idx, row in df.iterrows():
        images = ast.literal_eval(row['images']) if row['images'] else []
        products.append({
            "id": row['parent_asin'],
            "name": row['title'],
            "url": images[0]['large'] if images and 'large' in images[0] else None,
            "description": row['description']
        })
    options = {item["name"]: item["id"] for item in products}
    ids = {item["id"]: item["name"] for item in products}
    urls = {item["name"]: item["url"] for item in products}
    descs = {item["name"]: item["description"] for item in products}
    return options, ids, urls, descs

options, ids, urls, descs = get_products()

### Methods
def update_sidebar():
    with st.sidebar:
        st.title('Estetica')

        if 'selected_product_id' not in st.session_state:
            st.session_state.selected_product_id = None

        selected_name = st.selectbox(
            "Choose an option:", 
            options.keys(), 
            index=list(options.values()).index(st.session_state.selected_product_id) if st.session_state.selected_product_id else None,
            placeholder="Select..."
        )

        if selected_name:
            st.session_state.selected_product_id = options[selected_name]

        # Display the selected product information
        if st.session_state.selected_product_id:
            selected_name = ids[st.session_state.selected_product_id]
            selected_url = urls[selected_name]
            selected_description = descs[selected_name]

            # Display the selected name and ID
            print(f"Debug: selected_url = {selected_url}")
            if selected_url:
                st.image(selected_url, use_column_width=True)
            else:
                st.warning("No image selected or invalid URL.")

            st.write(f"{selected_name}")
            st.write(f"{','.join(eval(selected_description))}")


# Call update_sidebar at the beginning of your app
update_sidebar()

# @cache_data
def render_stuff(response):
    if response.startswith("Bot says:"):
        try:
            response_dict = eval(response[9:])  # Extract the dictionary from the response
            if 'product_recommendations' in response_dict:
                st.subheader("Product Recommendations")
                col1, col2 = st.columns(2)
                for i, (product_id, product_info) in enumerate(response_dict['product_recommendations'].items()):
                    try:
                        with col1 if i % 2 == 0 else col2:
                            if 'image_url' in product_info and product_info['image_url']:
                                if st.button(f"Select", key=f"select_{product_id}"):
                                    st.session_state['selected_product_id'] = product_id
                                    print("selected_product_id", st.session_state.selected_product_id)
                                    st.rerun()
                                st.image(product_info['image_url'], use_column_width=True)
                            st.write(f"**{product_info.get('title', 'No title')}**")
                            st.write(f"Details: {product_info.get('details', 'No details')}")
                            st.write(f"Reason: {product_info.get('reason', 'No reason provided')}")
                            st.write("---")
                    except Exception as e:
                        print(f"Error rendering similar feature {product_id}: {str(e)}")
                        continue
        except Exception as e:
            print(f"Error in rendering stuff: {str(e)}")
    else:
        st.write(response)

# Function for generating LLM response
# @cache_data
def generate_response(input):
    recommendations_notebook_url = f'{BASE_URL}/recommendations'

    data = {
        "query": input,
        "pid": st.session_state.get('selected_product_id')
    }
    print("generate_response data", data)
    try:
        response = requests.post(recommendations_notebook_url, json=data)
        if response.status_code == 200:
            result = response.json()
            recommendations = result.get('recommendations', 'No recommendations available')
            print("recommendations", recommendations)
            return f"Bot says: {recommendations}"
        else:
            return f"Bot says: Sorry, No matching products found for {st.session_state.selected_product_id} !, Error: {response.status_code}"
    except requests.RequestException as e:
        return f"Bot says: Sorry, there was an error connecting to the recommendation service. Error: {str(e)}"

#### Flow

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, how can I help you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            render_stuff(message["content"])
        else:
            st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Getting your answer from mystery stuff.."):
            response = generate_response(input)
            render_stuff(response) 
            # st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
