# 🌟 Streamlit Application with Ollama Integration

## 📄 Overview

This repository hosts a 🌈 Streamlit application that leverages the 🦙 Ollama model for its core functionality. Follow the steps below to set up and 🚀 run the application on your 🖥️.

---

## 🛠️ Prerequisites

1. **🐍 Install Python**:
   Ensure Python 3.8 or later is installed on your system. You can download it from the [🌐 official Python website](https://www.python.org/downloads/).

2. **🦙 Install Ollama**:
   Download and install the Ollama software from the [🌐 official Ollama website](https://ollama.ai/download). This is required to manage and use the models in the application.

3. **⬇️ Download Required Models**:
   Once Ollama is installed, download the required model(s) by running:
   ```bash
   ollama pull llama2:latest
   ```

---

## 🧰 Installation Steps

1. **📥 Clone the Repository**:
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/neerajkhatri04/ollama-chatbot-langchain/your-repository-name.git
   cd ollama-chatbot-langchain
   ```

2. **📦 Install Dependencies**:
   Install all required Python dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Application

1. **⚙️ Start the Ollama Server**:
   Ensure the Ollama server is running in the background. Start it by running:

   ```bash
   ollama serve
   ```

2. **▶️ Run the Streamlit Application**:
   Launch the Streamlit application with this command:

   ```bash
   streamlit run app.py
   ```

3. **🌐 Access the App**:
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## 📝 Notes

- Ensure the Ollama server is running before starting the Streamlit application.
- Make sure to download the required model (e.g., `llama2:latest`) before using the application.
- If you encounter any issues, consult the Ollama documentation or check the repository for updates.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions or support, please reach out to [yourname](mailto:your.email@example.com).
