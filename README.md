# Gmail Invoice Downloader

## 📌 Overview

Gmail Invoice Downloader is a Python script that automates the retrieval of invoice PDFs from your Gmail inbox. It uses the Gmail API to authenticate, search for invoice-related emails, and download attached PDFs.

## 🚀 Features

- **Gmail API Integration** – Connects securely to your Gmail account.
- **Automated Search** – Finds emails with invoice-related attachments.
- **PDF Download** – Saves invoice PDFs to a local folder.
- **Easy Setup** – Requires minimal configuration.

## 🛠️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/Gmail-Invoice-Downloader.git
cd Gmail-Invoice-Downloader
```

### 2️⃣ Install Dependencies

Ensure you have Python installed (version 3.x recommended). Then, run:

```sh
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 3️⃣ Setup Gmail API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Gmail API**.
3. Create **OAuth 2.0 Client ID credentials**.
4. Download `credentials.json` and place it in the project folder.

## 🏃 Usage

### Running the Script

```sh
python download_invoices.py
```

The script will:

1. Authenticate with Gmail.
2. Search for emails containing invoices.
3. Download invoice PDFs to the `Invoices/` folder.

## 🔍 How It Works

1. **Authentication**: Uses OAuth 2.0 to connect securely to your Gmail account.
2. **Searching Emails**: Queries Gmail for attachments named like `invoice.pdf`.
3. **Downloading Attachments**: Extracts and saves the PDF files locally.

## 🛑 Troubleshooting

### Invalid Credentials

If you get an authentication error, delete `token.json` and rerun the script to re-authenticate.

### No Invoices Found

- Ensure invoices in your Gmail have the term `invoice` in the attachment name.
- Check your **Spam/Promotions** folder.
- Modify the `search_invoices` function to customize the search query.

## 📝 License

This project is open-source under the **MIT License**.

## 🙌 Contributions

Pull requests are welcome! If you have improvements or bug fixes, feel free to contribute.

---

👨‍💻 Developed by **Abdullah**

