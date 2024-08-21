import google.generativeai as genai
from google.colab import auth, runtime

# Define the name of the secret where your API key is stored
gemini_api_secret_name = 'gemini_api_key'  # Replace with your secret name

# Authenticate your notebook to access the secrets
auth.authenticate_user()

try:
    # Fetch the API key from Colab's secret manager
    GOOGLE_API_KEY = runtime.secrets.get(gemini_api_secret_name)
    
    if GOOGLE_API_KEY:5
        # Configure the API key for the Google Gemini API
        genai.configure(api_key=GOOGLE_API_KEY)
        print("API key configured successfully.")
    else:
        raise ValueError(f"Secret '{gemini_api_secret_name}' not found or is empty.")
        
except ValueError as e:
    print(e)
    print(f"Please ensure the secret '{gemini_api_secret_name}' is set correctly in Colab's secret manager.")
except Exception as e:
    print(f"An unknown error occurred: {str(e)}")
