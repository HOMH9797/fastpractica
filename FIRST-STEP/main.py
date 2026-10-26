from fastapi import FastAPI,Query

app = FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")

BLOG_POST = [
    {
        "id": 1,
        "title": "First Blog Post",
        "content": "This is the content of the first blog post.",
        "author": "John Doe"
    },
    {
        "id": 2,
        "title": "Second Blog Post",
        "content": "This is the content of the second blog post.",
        "author": "Jane Smith"
    },
    {
        "id": 3,
        "title": "Third Blog Post",
        "content": "This is the content of the third blog post.",
        "author": "Alice Johnson"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to the My FastAPI Application!"}

# @app.get("/posts")
# def get_blog_posts():
#     return {"blog_posts": BLOG_POST}

@app.get("/posts")
def list_posts(query: str | None = Query(default=None, description="Search query for blog posts")):
    if query:
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
        return {"search_results": results}

    return {"blog_posts": BLOG_POST}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in BLOG_POST:
        if post["id"] == post_id:
            return {"post": post}
    return {"error": "Post not found"}