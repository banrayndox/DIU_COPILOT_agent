from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from query import ask_question_stream

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    user_id: str
    socket_id: str


@app.post("/")
def root(req: ChatRequest):

    def generate():

        for chunk in ask_question_stream(
            req.message,
            req.user_id
        ):

            if chunk:
                yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )