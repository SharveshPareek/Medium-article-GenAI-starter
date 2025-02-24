import streamlit as st
from config import bedrock_client, BEDROCK_MODEL_ID

# Function to generate product description using AWS Bedrock
def generate_description(product_name, category, features):
    # Constructing the input for the Bedrock model
    prompt = f"Generate a product description for a {category} named {product_name}. The key features are: {', '.join(features)}."
    
    # Calling the AWS Bedrock endpoint
    response = bedrock_client.invoke_model(
        ModelId=BEDROCK_MODEL_ID,  # Using model ID from config.py
        Body=prompt,
        ContentType='text/plain'
    )
    
    # Extracting the response text
    description = response['Body'].read().decode('utf-8')
    
    return description

# Streamlit UI for user input
def app():
    # Title and description
    st.title("AI Product Description Generator")
    st.write("Enter the details of your product and let AWS Bedrock generate a description.")

    # User input fields
    product_name = st.text_input("Product Name")
    category = st.text_input("Category")
    features_input = st.text_area("Product Features (comma separated)")
    
    # Convert features input into a list
    features = [feature.strip() for feature in features_input.split(',')]
    
    # Generate description when button is clicked
    if st.button("Generate Description"):
        if product_name and category and features:
            description = generate_description(product_name, category, features)
            st.subheader("Generated Product Description:")
            st.write(description)
        else:
            st.warning("Please provide all the product details.")

# Run the app
if __name__ == "__main__":
    app()
