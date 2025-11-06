import glob
import os
import requests
from requests.auth import HTTPBasicAuth
import time
from Nexus_uploader.env import *

# -------------- Configuration --------------
 
variables = {
    "DIST_FOLDER": DIST_FOLDER,
    "INTERVAL_SECONDS": INTERVAL_SECONDS,
    "NEXUS_URL": NEXUS_URL,
    "REPO_NAME": REPO_NAME,
    "USERNAME": USERNAME,
    "PASSWORD": PASSWORD,
}

for name, value in variables.items():
    print(f"{name} = {value}")


def upload_package(file_path):
    """Upload package using Nexus REST API"""
    pkg_name = os.path.basename(file_path)
    print(f"[START] Uploading {pkg_name}")
    
    try:
        # /service/rest/v1/components?repository=REPO_NAME
        upload_url = f"{NEXUS_URL.rstrip('/')}/service/rest/v1/components"
        
        with open(file_path, 'rb') as f:
            files = {
                'pypi.asset': (pkg_name, f),
            }
            
            params = {
                'repository': REPO_NAME
            }
            
            response = requests.post(
                upload_url,
                params=params,
                files=files,
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                verify=False, 
                timeout=60
            )
        
        if response.status_code in [200, 201, 204]:
            print(f"[OK] Successfully uploaded: {pkg_name}\n")
            return True
        else:
            print(f"[FAIL] Error uploading {pkg_name}:")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text[:300]}\n")
            return False
            
    except Exception as e:
        print(f"[ERROR] Exception uploading {pkg_name}:")
        print(f"Error: {str(e)}\n")
        return False


def main():
    # Validate configuration
    if USERNAME == "your-username" or PASSWORD == "your-password":
        print("❗️ Error: USERNAME or PASSWORD not set in env file")
        return
    
    print(f"Using Nexus: {NEXUS_URL}")
    print(f"Repository: {REPO_NAME}")
    print(f"Dist folder: {DIST_FOLDER}\n")
    
    # Find all .whl and .tar.gz files
    files = sorted(
        glob.glob(os.path.join(DIST_FOLDER, "*.whl")) +
        glob.glob(os.path.join(DIST_FOLDER, "*.tar.gz"))
    )
    
    if not files:
        print("❗️ The {DIST_FOLDER} folder is empty.")
        return
    
    print(f"Found {len(files)} package(s) to upload\n")
    
    # Upload each file
    success_count = 0
    for file_path in files:
        if upload_package(file_path):
            success_count += 1
        time.sleep(INTERVAL_SECONDS)
    
    print(f"✅ Upload process completed: {success_count}/{len(files)} successful")


if __name__ == "__main__":
    main()