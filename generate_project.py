import os

# Define the project structure and contents
files = {
    "requirements.txt": "Flask==3.0.3\ngunicorn==22.0.0\n",
    
    "app.py": """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""",
    
    "templates/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RGB Hello World</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-init: border-box;
      box-sizing: border-box;
    }

    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: Arial, Helvetica, sans-serif;
      background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff, #ff00ff);
      background-size: 400% 400%;
      animation: rgbGlow 10s ease infinite;
    }

    h1 {
      color: #ffffff;
      font-size: 4rem;
      text-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
      letter-spacing: 2px;
    }

    @keyframes rgbGlow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
  </style>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
"""
}

def create_project():
    print("Creating Flask project structure...")
    for filepath, content in files.items():
        # Ensure directories exist if the path includes a folder (like templates/)
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
            
        # Write the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {filepath}")
        
    print("\nProject structure generated successfully!")

if __name__ == "__main__":
    create_project()

