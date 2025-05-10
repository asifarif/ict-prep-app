---
title: Applications of ICT Exam Prep Chatbot 
emoji: 🧮 
colorFrom: indigo 
colorTo: pink 
sdk: gradio 
sdk_version: 4.31.5 
app_file: app.py 
pinned: true
---

Applications of ICT Course Project — CI/CD for Hugging Face Space

🔧 Title: “Applications of ICT Exam Prep Chatbot”

📚 Learning Objectives (for students)

By the end of this project, students will:
Understand the basic concepts, components, and importance of ICT, including computer hardware, software, networking, and the Internet (CLO1, PLO-1, Bloom’s C2 - Understanding)

Apply ICT tools and techniques to build an exam preparation chatbot (CLO2, PLO-3, Bloom’s C3 - Applying)

Use GitHub Actions to automate deployment of a Python app to Hugging Face Spaces

Explore collaborative development using GitHub repositories and CI/CD pipelines


🏗️ Project Setup
Students will:
Clone this repository (or create a new one with the provided files)

Ensure the following files are included:
app.py (main application file)
api.py (Grok API integration)
requirements.txt (dependencies)
Push the code to a GitHub repository

Set up one workflow for deployment:
.github/workflows/deploy.yml (already included in the repository)

🔐 Add Hugging Face Token
Go to Hugging Face > Settings > Access Tokens
Generate a token with Write permission
On GitHub, go to repo Settings > Secrets and Variables > Actions


Add secret: HF_TOKEN
🔐 Add Grok API Key

Obtain an API key from x.ai/api
On GitHub, go to repo Settings > Secrets and Variables > Actions

Add secret: GROQ_API_KEY

🚀 Deployment
Push changes to the main branch of your GitHub repository
The GitHub Actions workflow (deploy.yml) will automatically deploy the app to your Hugging Face Space
Access the deployed app via the Space URL (e.g., https://huggingface.co/spaces/your-username/ict-exam-prep)