# 📧 Personalized Email Sender from Excel

This Python script automates the process of sending personalized emails using data from an Excel file.

## 📄 Features

- Reads an Excel file with the following columns: `Ruta`, `Nombre`, and `Correo`.
- Sends a personalized email to each recipient, including:
  - Their name
  - Their assigned route
  - A custom signature

## 🛠️ Requirements

Install the required packages:

```bash
pip install pandas openpyxl
