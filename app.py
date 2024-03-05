from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import uvicorn
import warnings
#from chatbot import chatbot
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
warnings.filterwarnings("ignore")
    
@app.get("/")
def hello():
    return{"message":"HELLO USER"}
 
@app.post("/ask")
async def get_text(text: str):
    print("Received Query!")
    #answer=chatbot(text)
    answer="WORKING"
    print("Response fetched!")
    return JSONResponse({'status':'OK','answer':answer})
    
    
        
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)