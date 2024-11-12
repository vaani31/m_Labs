import os
import subprocess
from django.http import HttpResponse
from datetime import datetime
import pytz

def htop_view(request):
    # Set IST timezone
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Run `top` command and get the output
    top_output = subprocess.getoutput('top -b -n 1')

    # Prepare data for display
    name = "Your Full Name"  # Replace with your full name

    # Try to get the username from the system/environment
    try:
        username = os.getlogin()
    except OSError:
        username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Render the data as HTML
    html_content = f"""
    <html>
        <body>
            <h1>/htop Endpoint</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content)
