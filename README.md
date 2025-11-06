# 🚀 Nexus Uploader

A simple and automated tool for uploading **Python packages (.whl / .tar.gz)** to a **Nexus Repository** using the REST API.


## 📦 Features
- Supports **Nexus Repository** via REST API (`/service/rest/v1/components`)
- Handles both `.whl` and `.tar.gz` package formats
- Easy configuration via `env.py`
- Real-time upload status logs
- Includes a shell script (`uploader.sh`) for one-command execution

## 🗂 Project Structure
```
Nexus_uploader/
├── env.py
├── uploader.py
├── uploader.sh
└── requirements.txt
```
## ⚙️ Configuration (`env.py`)

Update the following values in `env.py` to match your Nexus setup:

```python
DIST_FOLDER = "./dist/"
INTERVAL_SECONDS = 2
NEXUS_URL = "https://your-nexus-url"
REPO_NAME = "your-repo-name"
USERNAME = "your-username"
PASSWORD = "your-password"
```
> 🔐 **Security Tip:** It’s recommended to load sensitive values (like `USERNAME` and `PASSWORD`) from environment variables or `.env` files instead of hardcoding them.

## 🚀 How to Run

### Option 1 – Run with Python
```bash
python3 uploader.py
```
### Option 2 – Run with Shell Script (Recommended)
```bash
chmod +x uploader.sh
./uploader.sh
```
This script will:
1. Install dependencies (`twine`, `requests`, `python-dotenv`)
2. Download packages listed in `requirements.txt` into `dist/`
3. Automatically upload all `.whl` and `.tar.gz` files to Nexus

## 🧠 How It Works
- The script scans the `DIST_FOLDER` for `.whl` and `.tar.gz` files  
- Uploads each file to Nexus with a delay defined by `INTERVAL_SECONDS`  
- Uses the following Nexus API endpoint:
  ```
  POST {NEXUS_URL}/service/rest/v1/components?repository={REPO_NAME}
  ```
- Reports success for HTTP status codes `200`, `201`, or `204`

## 🧪 Example Output
```
Using Nexus: https://your-nexus-url
Repository: pypi-internal
Dist folder: ./dist/

Found 3 package(s) to upload

[START] Uploading example_pkg-0.1.0-py3-none-any.whl
[OK] Successfully uploaded: example_pkg-0.1.0-py3-none-any.whl

✅ Upload process completed: 3/3 successful
```

## ❗️ Common Errors
| Error | Description |
|-------|--------------|
| `USERNAME or PASSWORD not set` | Credentials not configured in `env.py` |
| `Empty dist folder` | No packages found in `DIST_FOLDER` |
| `403 or 401` | Invalid Nexus credentials or permissions |
| `Connection refused` | Invalid Nexus URL or network restrictions |

## 🛡 Security Recommendations
- Do not store credentials directly in the source code  
- Remove `verify=False` for SSL verification in production  
- Use service accounts or temporary tokens in CI/CD environments

## 🧩 Dependencies
- `Python ≥ 3.8` 
- `requests`    

## 📄 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for personal or commercial purposes.

## Contact
For any questions or issues, please contact:

[![Gmail](https://skillicons.dev/icons?i=gmail)](pouria.shahvarpour@gmail.com) 
[![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://ir.linkedin.com/in/pouriashavarpour)
[![Instagram](https://skillicons.dev/icons?i=instagram)](https://www.instagram.com/pouria_shahvarpour)
