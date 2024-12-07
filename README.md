# POC: Flask Error Handler

This Proof of Concept (POC) demonstrates a structured approach to implement custom error handling in a Flask application.

The error handler is designed to manage different types of errors, such as:

- **Network errors**
- **Database errors**
- **Authentication errors**
- **General server errors**

Any errors not explicitly defined in the `exceptions.py` module will be handled as **Internal Server Errors**.

---

## 📁 Project Structure

```plaintext
.
├── src
│   └── app
│       ├── app.py             # Main Flask application file
│       ├── error_handlers.py  # Module containing error-handling functions
│       ├── exceptions.py      # Module defining custom exception classes
│       └── routes.py          # Module defining application routes
└── tests
    ├── app
    │   └── test_routes.py     # Test file for the application's routes
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Poetry package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

### Running the Application

Start the server in either production or debug mode:

- Production:
  ```bash
  poetry run start
  ```

- Debug:
  ```bash
  poetry run debug
  ```

### Running Tests

Execute the test suite using `pytest`:

```bash
poetry run pytest
```

---

## 🔍 Example Usage: `/ping` Route

You can test the `/ping` route to simulate different behaviors. The endpoint accepts a query parameter `action` with the following options:

| **Action**    | **Behavior**                   |
|---------------|--------------------------------|
| `ok`          | Returns a success response.    |
| `not_found`   | Simulates a "not found" error. |
| `not_handled` | Simulates an unhandled error.  |

### Example cURL Request

```bash
curl --request GET \
  --url 'http://localhost:5000/ping?action=not_handled'
```

---

## 🛠️ Additional Notes

- Ensure all new exceptions are added to `exceptions.py` to avoid them being classified as internal server errors.
- Use `error_handlers.py` to register and customize additional error handlers as needed.
