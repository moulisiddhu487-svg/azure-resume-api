import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="", auth_level=func.AuthLevel.ANONYMOUS)
def root_redirect(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        status_code=302,
        headers={"Location": "/api/cv"}
    )
    
@app.route(route="cv")
def get_resume(req: func.HttpRequest) -> func.HttpResponse:
    
    resume_data = {
        "name": "Your Full Name",
        "role": "Cloud & DevOps Engineer",
        "skills": [
            "Docker", 
            "Kubernetes", 
            "Azure", 
            "CI/CD (GitHub Actions)", 
            "Python", 
            "Linux"
        ],
        "projects": [
            {
                "title": "Job Track Hub",
                "description": "Containerized multi-service application architecture."
            },
            {
                "title": "Serverless Resume API",
                "description": "Automated cloud API delivering structured JSON resume data."
            }
        ]
    }
    
    return func.HttpResponse(
        body=json.dumps(resume_data, indent=2),
        status_code=200,
        mimetype="application/json"
    )
