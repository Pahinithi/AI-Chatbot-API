# LankaMate AI Chatbot

LankaMate AI Chatbot is a generative artificial intelligence chatbot that provides various functionalities such as image insights, text embeddings, answering questions, and sports-related queries.

## Requirements

- Python 3.10.16
- The required Python packages are listed in `requirements.txt`.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Pahinithi/AI-Chatbot-API.git
    cd LankaMate-AI-Chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the configuration:
    - Create a `config.json` file in the root directory with your Google API key:
        ```json
        {
            "GOOGLE_API_KEY": "your_google_api_key"
        }
        ```

## Usage

1. Run the FastAPI application:
    ```sh
    fastapi dev main.py (dev mode)
    ```

    ```sh
    fastapi main.py (production mode)
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- `POST /image-insight`: Get insights about an uploaded image.
- `POST /embed-text`: Get text embeddings for a given text.
- `POST /ask-anything`: Ask any question and get a response.
- `GET /current-datetime`: Get the current date and time.
- `GET /location`: Get the location information based on the client's IP address.
- `POST /sport-query`: Get responses for sports-related queries.

## License

This project is licensed under the MIT License.

## Author

This project is developed by Nithilan Pahrathan. For any inquiries, contact nithilan32@gmail.com.
