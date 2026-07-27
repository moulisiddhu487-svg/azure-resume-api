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
    
    resume_data = 
       {
  "basics": {
    "name": "GODABA MOULI VENKATA NARSIMHA",
    "label": "DevOps & Cloud Engineer | Fresher",
    "email": "moulisiddhu487@gmail.com",
    "phone": "+91 93981 67124",
    "summary": "Aspiring DevOps and Cloud Engineer with a BSc in Mathematics, Electronics & Computer Science and hands-on DevOps training covering containerization, orchestration, infrastructure as code, and CI/CD automation. Built and deployed cloud-hosted, containerized applications end-to-end, including a serverless REST API on Azure Functions with an automated GitHub Actions pipeline. Currently pursuing the Microsoft Azure AZ-104 certification. Seeking an entry-level DevOps/Cloud Engineer role or internship to apply and grow these skills in a production environment.",
    "location": {
      "city": "Hyderabad",
      "region": "Telangana",
      "countryCode": "IN"
    },
    "profiles": [
      {
        "network": "GitHub",
        "url": "https://github.com/moulisiddhu487-svg"
      },
      {
        "network": "LinkedIn",
        "url": "[Add Linkedin link]"
      },
      {
        "network": "Portfolio",
        "url": "[Add portfolio link]"
      }
    ]
  },
  "education": [
    {
      "institution": "Adikavi Nannaya University",
      "area": "Mathematics, Electronics & Computer Science",
      "studyType": "BSc",
      "endDate": "2025-07",
      "score": "CGPA: 6.71"
    },
    {
      "institution": "Aditya Junior College (Board of Intermediate Education, AP)",
      "studyType": "Class XII",
      "endDate": "2020-03"
    }
  ],
  "skills": [
    {
      "name": "Cloud Platforms",
      "keywords": [
        "Microsoft Azure",
        "AWS"
      ]
    },
    {
      "name": "Containers & Orchestration",
      "keywords": [
        "Docker",
        "Kubernetes"
      ]
    },
    {
      "name": "Infrastructure as Code & Config Management",
      "keywords": [
        "Terraform",
        "Ansible"
      ]
    },
    {
      "name": "CI/CD & Automation",
      "keywords": [
        "GitHub Actions",
        "Jenkins"
      ]
    },
    {
      "name": "Monitoring & Observability",
      "keywords": [
        "Prometheus",
        "Grafana"
      ]
    },
    {
      "name": "Operating Systems & Scripting",
      "keywords": [
        "Linux (Ubuntu/RHEL)",
        "Bash",
        "Windows"
      ]
    },
    {
      "name": "Languages & APIs",
      "keywords": [
        "Python",
        "REST APIs"
      ]
    }
  ],
  "projects": [
    {
      "name": "Serverless Resume API",
      "description": "Built and deployed a serverless REST API on Azure Functions that serves structured resume data in JSON format.",
      "highlights": [
        "Configured a GitHub Actions CI/CD pipeline to automatically package, test, and deploy backend updates on every git push.",
        "Resolved SCM authentication restrictions and configured CORS rules to enable secure cross-origin requests."
      ],
      "keywords": [
        "Python",
        "Azure Functions",
        "GitHub Actions",
        "REST API"
      ],
      "url": "[Add live API link]"
    },
    {
      "name": "DevOps Learning Lab",
      "description": "Containerized a web application with Docker and managed the full container lifecycle.",
      "highlights": [
        "Practiced CI/CD pipeline concepts using GitHub Actions for automated build and deployment workflows."
      ],
      "keywords": [
        "Docker",
        "GitHub Actions",
        "Linux"
      ],
      "url": "[Add GitHub repo link]"
    }
  ],
  "certificates": [
    {
      "name": "Microsoft Azure Administrator (AZ-104)",
      "date": "In Progress",
      "issuer": "Microsoft"
    },
    {
      "name": "DevOps Training Program (Docker, Kubernetes, Terraform, Ansible, AWS, Azure)",
      "date": "Completed",
      "issuer": "Xtream Tech, Hyderabad"
    }
  ],
  "languages": [
    {
      "language": "Telugu",
      "fluency": "Native"
    },
    {
      "language": "Hindi",
      "fluency": "Fluent"
    },
    {
      "language": "English",
      "fluency": "Fluent"
    }
  ]
