import os

root_dir = "content"

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(subdir, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            fm = ""
            body = ""

            # Front Matter رو جدا کن
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) == 3:
                    fm = parts[1]
                    body = parts[2]

                    # Body رو wrap کن
                    if '{{< rawhtml >}}' not in body:
                        body = "\n{{< rawhtml >}}\n" + body.strip() + "\n{{< /rawhtml >}}\n"

                    content = f'---\n{fm}---{body}'
                else:
                    continue
            else:
                # فایل بدون Front Matter
                body = content
                if '{{< rawhtml >}}' not in body:
                    body = "\n{{< rawhtml >}}\n" + body.strip() + "\n{{< /rawhtml >}}\n"
                content = body

            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Wrapped rawhtml in: {file_path}")