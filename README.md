# Sentiment-analysis-SAS
projet SAS Sentiment analysis 
# Sentiment Analysis Application

## Overview
This project is a simple sentiment analysis application that uses a pre-trained model from Hugging Face to classify the sentiment of a given text as positive, negative, or neutral. The backend is built with FastAPI, and the application is deployed on Railway.app for cloud hosting.

---

## Features
- **Model:** `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face.
- **API Backend:** Built using FastAPI to handle sentiment analysis requests.
- **Frontend:** A simple HTML form (form.html) for user input.
- **Cloud Deployment:** Hosted on Railway.app.

---

## Project Structure
```
.
├── main.py              # FastAPI backend script
├── form.html            # HTML form for user input
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
```

---

## How to Use

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open `form.html` in a browser to use the application.

### Deployment
The application is deployed on Railway.app. You can access it at the deployed URL. 

---

## API Endpoints

### POST `/analyze/`
- **Description:** Analyzes the sentiment of the input text.
- **Input:** JSON with a `text` field.
  ```json
  {
    "text": "This is a great example!"
  }
  ```
- **Response:**
  ```json
  {
    "text": "This is a great example!",
    "sentiment": {
      "label": "POSITIVE",
      "score": 0.9998
    }
  }
  ```

---

## Technologies Used
- **FastAPI:** For creating the backend API.
- **Hugging Face Transformers:** For pre-trained sentiment analysis models.
- **Railway.app:** For cloud deployment.
- **HTML:** For the simple user interface.

---

## Future Enhancements
- Add more models and functionalities (e.g., summarization, translation).
- Enhance the frontend design for better user experience.
- Support batch text analysis.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

