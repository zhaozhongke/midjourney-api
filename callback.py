from fastapi import FastAPI
from typing import List, Optional, TypedDict

app = FastAPI()

class Attachment(TypedDict, total=False):
    id: int
    url: str
    proxy_url: str
    filename: str
    content_type: str
    width: Optional[int]
    height: Optional[int]
    size: Optional[int]
    ephemeral: Optional[bool]

class EmbedsImage(TypedDict, total=False):
    url: str
    proxy_url: str

class Embed(TypedDict, total=False):
    type: str
    description: str
    image: Optional[EmbedsImage]

class CallbackData(TypedDict):
    type: str
    id: int
    content: str
    attachments: List[Optional[Attachment]]
    embeds: List[Optional[Embed]]
    trigger_id: str

@app.post("/callback")
async def callback(callback_data: CallbackData):
# 在这里可以访问解析后的参数
    print("Callback received")
    print(callback_data)
    return {"message": "Callback received"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)