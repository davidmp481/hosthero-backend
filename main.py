
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, tasks, inventory, bookings

app = FastAPI()

origins = ["*"]  # Replace with your frontend domain in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(inventory.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {"message": "Welcome to HostHero API"}
