from typing import Optional
import gradio as gr

from fastapi import FastAPI
import dash
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app = gr.mount_gradio_app(app, dash.demo, path='/dash')
