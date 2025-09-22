python -m venv .venv

source .venv/bin/activate

gcloud auth application-default login

```
google.genai.errors.ClientError: 403 PERMISSION_DENIED. 
{'error': {'code': 403, 
'message': "Permission 'aiplatform.endpoints.predict' denied on resource '//aiplatform.googleapis.com/projects/ford-035fd694073c82351fd3e2b4/locations/us-central1/publishers/google/models/gemini-2.5-flash' (or it may not exist).", 
'status': 'PERMISSION_DENIED', 
'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'IAM_PERMISSION_DENIED', 'domain': 'aiplatform.googleapis.com', 'metadata': {'resource': 'projects/ford-035fd694073c82351fd3e2b4/locations/us-central1/publishers/google/models/gemini-2.5-flash', 
'permission': 'aiplatform.endpoints.predict'}}]}}
```