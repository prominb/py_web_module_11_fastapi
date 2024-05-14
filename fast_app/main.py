from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/note/new")
async def read_new_notes():
    return {"message": "Return new notes"}

# @app.get("/notes/{note_id}")
# async def read_note(note_id: int):
#     return {"note": note_id}
@app.get("/notes/{note_id}")
async def read_note(note_id: int = Path(description="The ID of the note to get", gt=0, le=10)):
    return {"note": note_id}

# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = 10):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}
# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = 10, q: str | None = None):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}
@app.get("/notes")
async def read_notes(skip: int = 0, limit: int = Query(default=10, le=100, ge=10)):
    return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}
