# 🏦 Atlas Bank — Alloy API Integration

A bank account application form that integrates with Alloy's identity verification API. Applicants submit their details and receive an instant decision: **Approved**, **Manual Review**, or **Denied**.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python + Flask
- **API:** Alloy Sandbox

Plain HTML was chosen to keep the focus on the API integration.

## How to Run

1. Clone the repo:
```
git clone https://github.com/vp915/alloy-bank-app.git
cd alloy-bank-app
```

2. Install dependencies:
```
pip3 install flask requests python-dotenv
```

3. Add your Alloy credentials to `.env`:
```
ALLOY_TOKEN=your_token_here
ALLOY_SECRET=your_secret_here
```

4. Start the server:
```
python3 server.py
```

5. Open in your browser: http://localhost:3000

## Testing Outcomes

| Last Name | Outcome |
|---|---|
| Any normal name | Approved |
| `Review` | Manual Review |
| `Deny` | Denied |

## Security
Credentials are stored in `.env` which is excluded from version control via `.gitignore`.

## Notes
During testing, discovered that Alloy's sandbox returns `"Denied"` as the outcome value
(not `"Deny"` as documented). Updated the frontend to match the actual API response.
