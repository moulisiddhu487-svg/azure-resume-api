import azure.functions as func

app = func.FunctionApp()

# Root redirect to /api/cv
@app.route(route="", auth_level=func.AuthLevel.ANONYMOUS)
def root_redirect(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        status_code=302,
        headers={"Location": "/api/cv"}
    )

# HTML Resume endpoint to prevent browser search hijacks
@app.route(route="cv", auth_level=func.AuthLevel.ANONYMOUS)
def get_cv(req: func.HttpRequest) -> func.HttpResponse:
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Godaba Mouli Venkata Narsimha - DevOps & Cloud Engineer</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 40px 20px; background: #f9f9f9; }
        .container { background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { margin-bottom: 5px; color: #111; font-size: 26px; }
        .title { color: #0070f3; font-weight: 600; margin-bottom: 15px; font-size: 16px; }
        .contact-info { font-size: 14px; color: #555; margin-bottom: 25px; border-bottom: 1px solid #eaeaea; padding-bottom: 15px; }
        .contact-info a { color: #0070f3; text-decoration: none; margin-right: 15px; }
        h2 { font-size: 18px; color: #111; border-bottom: 2px solid #0070f3; padding-bottom: 5px; margin-top: 30px; text-transform: uppercase; letter-spacing: 0.5px; }
        p, li { font-size: 14px; color: #444; }
        ul { padding-left: 20px; }
        li { margin-bottom: 8px; }
        .skills-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 14px; }
        .skill-category { font-weight: 600; color: #222; }
        .footer { text-align: center; margin-top: 40px; font-size: 12px; color: #888; border-top: 1px solid #eaeaea; padding-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GODABA MOULI VENKATA NARSIMHA</h1>
        <div class="title">DevOps & Cloud Engineer | Fresher</div>
        <div class="contact-info">
            📍 Hyderabad, Telangana, India | 📞 +91 93981 67124 | ✉️ moulisiddhu487@gmail.com<br>
            🔗 <a href="https://github.com/moulisiddhu487-svg" target="_blank">GitHub Profile</a>
        </div>

        <h2>Professional Summary</h2>
        <p>Aspiring DevOps and Cloud Engineer with a BSc in Mathematics, Electronics & Computer Science and hands-on DevOps training covering containerization, orchestration, infrastructure as code, and CI/CD automation. Built and deployed cloud-hosted, containerized applications end-to-end, including a serverless REST API on Azure Functions with an automated GitHub Actions pipeline. Currently pursuing the Microsoft Azure AZ-104 certification. Seeking an entry-level DevOps/Cloud Engineer role or internship to apply and grow these skills in a production environment.</p>

        <h2>Technical Skills</h2>
        <div class="skills-grid">
            <div><span class="skill-category">Cloud Platforms:</span> Microsoft Azure (AZ-104), AWS[cite: 1]</div>
            <div><span class="skill-category">Containers & Tools:</span> Docker, Kubernetes[cite: 1]</div>
            <div><span class="skill-category">IaC & Config:</span> Terraform, Ansible[cite: 1]</div>
            <div><span class="skill-category">CI/CD & Auto:</span> GitHub Actions, Jenkins[cite: 1]</div>
            <div><span class="skill-category">Monitoring:</span> Prometheus, Grafana[cite: 1]</div>
            <div><span class="skill-category">OS & Scripting:</span> Linux, Bash, Windows[cite: 1]</div>
        </div>

        <h2>Projects</h2>
        <div>
            <strong>Serverless Resume API</strong> (Python, Azure Functions, GitHub Actions, REST API)[cite: 1]
            <ul>
                <li>Built and deployed a serverless REST API on Azure Functions that serves structured data[cite: 1].</li>
                <li>Configured a GitHub Actions CI/CD pipeline to automatically package, test, and deploy backend updates[cite: 1].</li>
                <li>Resolved SCM authentication restrictions and configured CORS rules for secure cross-origin requests[cite: 1].</li>
            </ul>
        </div>
        <div>
            <strong>DevOps Learning Lab</strong> (Docker, GitHub Actions, Linux)[cite: 1]
            <ul>
                <li>Containerized a web application with Docker and managed the full container lifecycle[cite: 1].</li>
                <li>Practiced CI/CD pipeline concepts using GitHub Actions for automated build and deployment workflows[cite: 1].</li>
            </ul>
        </div>

        <h2>Certifications & Education</h2>
        <ul>
            <li><strong>Microsoft Azure Administrator (AZ-104):</strong> In Progress[cite: 1]</li>
            <li><strong>DevOps Training Program:</strong> Xtream Tech, Hyderabad (Docker, Kubernetes, Terraform, Ansible, AWS, Azure)[cite: 1]</li>
            <li><strong>BSc (Mathematics, Electronics & Computer Science):</strong> Adikavi Nannaya University, July 2025 (CGPA: 6.71)[cite: 1]</li>
        </ul>

        <div class="footer">
            Powered by Azure Functions & GitHub Actions CI/CD Pipeline
        </div>
    </div>
</body>
</html>
"""
    return func.HttpResponse(
        body=html_content,
        status_code=200,
        headers={"Content-Type": "text/html; charset=utf-8"}
    )
