# code-assistant
Smart AI Developer for Surooh

## Usage
1. Copy `.env.template` to `.env` and add your OpenAI key
2. Run the app:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```
3. Send POST request to `/ask` with JSON:
```json
{
  "message": "اكتبلي صفحة تسجيل دخول بـ React"
}
```