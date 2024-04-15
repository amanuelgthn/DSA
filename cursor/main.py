from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GODADDY_API_KEY = 'your_godaddy_api_key'
GODADDY_API_SECRET = 'your_godaddy_api_secret'
CLOUDFLARE_API_KEY = 'your_cloudflare_api_key'
CLOUDFLARE_EMAIL = 'your_cloudflare_email'

@app.post("/update-nameservers/")
async def update_nameservers(domain: str):
    # Change name servers on GoDaddy
    godaddy_headers = {
        "Authorization": f"sso-key {GODADDY_API_KEY}:{GODADDY_API_SECRET}"
    }
    godaddy_url = f"https://api.godaddy.com/v1/domains/{domain}/records"
    godaddy_data = [
        {"type": "NS", "name": "@", "data": "ns1.cloudflare.com", "ttl": 3600},
        {"type": "NS", "name": "@", "data": "ns2.cloudflare.com", "ttl": 3600}
    ]
    godaddy_response = requests.patch(godaddy_url, json=godaddy_data, headers=godaddy_headers)
    if godaddy_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to update GoDaddy name servers")

    # Add and confirm domain on Cloudflare
    cloudflare_headers = {
        "X-Auth-Email": CLOUDFLARE_EMAIL,
        "X-Auth-Key": CLOUDFLARE_API_KEY,
        "Content-Type": "application/json"
    }
    cloudflare_url = "https://api.cloudflare.com/client/v4/zones"
    cloudflare_data = {
        "name": domain,
        "jump_start": True
    }
    cloudflare_response = requests.post(cloudflare_url, json=cloudflare_data, headers=cloudflare_headers)
    if cloudflare_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to add domain to Cloudflare")

    return {"message": "Domain name servers updated successfully and domain added to Cloudflare"}
