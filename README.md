# converting-word-pdf

## Files Overview

- **start_servers.bat**: Starts backend and frontend servers.
- **run_app.bat**: Installs dependencies, checks prerequisites, and starts servers.
- **requirements.txt**: Python dependencies required for the project.
- **frontend/index.html**: Static HTML page for the frontend.
- **backend/app.py**: Flask API for the backend.

## Prerequisites

- Python 3.x
- Microsoft Word (required for backend functionality)

## Quick Setup

For a **fast and automated setup**, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/solixoi/converting-word-pdf.git
    cd converting-word-pdf
    ```

2. Run the application:

    - **Windows**: Double-click `run_app.bat`.

    This will:
    - Install dependencies.
    - Start both backend and frontend servers.
    - Open the frontend at `http://localhost:8000`.

---

## Manual Setup

For a **manual setup**, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/solixoi/converting-word-pdf.git
    cd converting-word-pdf
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Start the Backend Server**:

    - Navigate to the `backend` directory and run the Flask application (`app.py`):

    ```bash
    cd backend
    python app.py
    ```

4. **Start the Frontend Server**:

    - Open a new terminal or command prompt, navigate to the `frontend` directory, and run the static file server:

    ```bash
    cd ../frontend
    python -m http.server 8000
    ```

5. Access the frontend at `http://localhost:8000`.

---

## Stopping the Servers

To stop the application, simply close the command prompt or terminal windows where the backend and frontend servers are running.

---

## Notes

- Microsoft Word is required for the backend to function correctly (via COM).
- Ensure Python is installed and accessible through the `python` command.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
