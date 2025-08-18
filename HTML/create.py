import os

POSTS_DIR = "Posts"
OUTPUT_DIR = "Site"       # generated blog posts go here
BLOG_TEMPLATE_FILE = os.path.join(POSTS_DIR, "blog-template.html")
BLOG_INDEX_FILE = "blogs.html"   # your hub page with {{posts}}

# Load templates
with open(BLOG_TEMPLATE_FILE, encoding="utf-8") as f:
    blog_template = f.read()
with open(BLOG_INDEX_FILE, encoding="utf-8") as f:
    blog_index_template = f.read()

posts_html = []

# Loop through all text posts
for filename in sorted(os.listdir(POSTS_DIR), reverse=True):
    if filename.endswith(".txt"):
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()

        # Extract metadata
        title = lines[0].replace("Title: ", "").strip()
        date = lines[1].replace("Date: ", "").strip()
        content = "".join(lines[3:]).strip().replace("\n", "<br>")

        # Make a safe filename for the post
        slug = filename.replace(".txt", ".html")
        post_output = os.path.join(OUTPUT_DIR, slug)

        # Generate individual post page
        post_page = blog_template.replace("{{title}}", title)\
                                 .replace("{{date}}", date)\
                                 .replace("{{content}}", content)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(post_output, "w", encoding="utf-8") as out:
            out.write(post_page)

        # Generate preview for blog hub
        preview = content[:120] + "..." if len(content) > 120 else content
        posts_html.append(
            f'<li><a href="{OUTPUT_DIR}/{slug}">{date} – {title}</a><br>{preview}</li>'
        )

# Generate blog index (hub page)
blog_index_filled = blog_index_template.replace("{{posts}}", "\n".join(posts_html))
with open(BLOG_INDEX_FILE, "w", encoding="utf-8") as out:
    out.write(blog_index_filled)

print("✅ Blog generated successfully!")
print(f"   - {len(posts_html)} posts processed")
print(f"   - Individual posts saved in: {OUTPUT_DIR}/")
print(f"   - Blog hub updated: {BLOG_INDEX_FILE}")