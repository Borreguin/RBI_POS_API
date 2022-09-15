import os
import uvicorn
os.environ["ENV"] = 'prod'

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    print(f">>>>> \tUI API deployed over: http://{host}:{port}/docs")
    uvicorn.run("app.main:api", host=host, port=port)
