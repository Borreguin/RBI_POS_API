import os
import uvicorn
os.environ["ENV"] = 'dev'

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    print(f">>>>> \tUI API deployed over: http://{host}:{port}/docs")
    uvicorn.run("app.main:api", host=host, port=port, debug=True, reload=True)
