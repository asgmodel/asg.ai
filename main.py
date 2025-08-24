from typing import Optional
import gradio as gr
from pydantic import BaseModel
from gradio_client import Client

from fastapi import FastAPI
import dash
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# تهيئة Gradio Client مرة واحدة

# نموذج للطلب
class PromptRequest(BaseModel):
    prompt: str

# endpoint رئيسي للتوليد
@app.post("/generate")
def generate_text(req: PromptRequest):
    try:
        client = Client("wasmdashai/LAHJA-AI")

        result = client.predict(
            prompt=req.prompt,
            api_name="/generate_from_prompt"
        )
        return {"input": req.prompt, "output": result}
    except Exception as e:
        return {"error": str(e)}
app = gr.mount_gradio_app(app, dash.demo, path='/dash')
