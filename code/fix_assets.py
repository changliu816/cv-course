import os
import subprocess

# Set your folder path here
folder_path = "/Users/chang/Workplace/machine_learning/cs231n.github.io-master"  # ← Change this

# for filename in os.listdir(folder_path):
#     if filename.endswith(".md"):
#         file_path = os.path.join(folder_path, filename)
#         with open(file_path, "r", encoding="utf-8") as f:
#             content = f.read()
#
#         # Replace all occurrences of "/assets/" with "assets/"
#         updated_content = content.replace("/assets/", "assets/")
#
#         # Write back only if changes were made
#         if updated_content != content:
#             with open(file_path, "w", encoding="utf-8") as f:
#                 f.write(updated_content)
#             print(f"✅ Fixed: {filename}")
#         else:
#             print(f"— Skipped (no change): {filename}")
#

for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        md_path = os.path.join(folder_path, filename)

        # Step 1: Replace "/assets/" with "assets/"
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        updated_content = content.replace("/assets/", "assets/")
        if updated_content != content:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"✅ Fixed: {filename}")
        else:
            print(f"— Skipped fix: {filename}")

        # Step 2: Convert to .html using Pandoc
        html_filename = filename.replace(".md", ".html")
        html_path = os.path.join(folder_path, html_filename)

        try:
            subprocess.run(
                ["pandoc", md_path, "-o", html_path, "--mathjax", "--standalone"],
                check=True
            )
            print(f"✅ Converted to HTML: {html_filename}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Pandoc failed for {filename}: {e}")
