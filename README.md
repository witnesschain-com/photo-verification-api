# FastAPI Photo Classification API

## 📌 Overview
This FastAPI-based service provides an endpoint for classifying whether uploaded photos satisfy a given task using **Claude** AI. It accepts a list of image files along with a task description and returns a JSON response with classification results.

## 🚀 Features
- ✅ Accepts multiple image uploads for classification
- 🔍 Uses Claude AI to analyze photos against a given task
- 📡 FastAPI-based for lightweight and scalable deployment
- 📤 Returns structured JSON response with classification results and reasoning

## 📦 Installation & Setup

### **Prerequisites**
- Python 3.8+
- FastAPI
- Uvicorn

### **Installation**
```bash
# Clone the repository (if applicable)
git clone https://github.com/your-repo/photo-verification-api.git
cd photo-verification-api

# Install dependencies
pip install -r requirements.txt
```

### **Run the API**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`.

## 🔗 API Reference

### **Classify Photos**
**Endpoint:** `POST /classify-photos/`

**Description:**
Classifies if the uploaded photos meet the specified task requirements using Claude AI.

#### **Request Parameters**
| Parameter  | Type               | Description |
|------------|------------------|-------------|
| `task`     | `string`          | Description of what the photos should show/contain |
| `photos`   | `List[UploadFile]` | List of image files to classify |

#### **Request Example** (cURL)
```bash
curl -X 'POST' \
  'http://localhost:8000/classify-photos/' \
  -F 'task="Show a sunset over the ocean"' \
  -F 'photos=@image1.jpg' \
  -F 'photos=@image2.jpg'
```

#### **Response Example**
```json
{
  "success": true,
  "reason": "The uploaded photos clearly depict a sunset over the ocean."
}
```

## 🛠 Project Structure
```
.
├── main.py                  # FastAPI app entry point
├── services/
│   ├── classification_service.py  # Handles photo classification logic
├── schemas.py               # Defines request and response schemas
├── requirements.txt         # Dependencies
└── README.md                # API Documentation
```

## 📜 License
MIT License - see the `LICENSE` file for details.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request with any improvements.

## 📞 Support
For questions or issues, open an issue on GitHub or contact the maintainer.

