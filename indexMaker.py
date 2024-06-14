import os
import subprocess
import time

def generate_index_file():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    output_file = os.path.join(script_dir, 'index.html')

    # Define the time frame for considering files/folders as recent (in seconds)
    recent_time_frame = 1 * 24 * 60 * 60  # 1 day
    current_time = time.time()

    print(f"Current time: {current_time}")

    def get_git_last_commit_time(path):
        try:
            # Get the last commit timestamp for the given path
            timestamp = subprocess.check_output(['git', 'log', '-1', '--format=%ct', path], cwd=script_dir)
            return int(timestamp.strip())
        except subprocess.CalledProcessError:
            print(f"Failed to get last commit time for {path}")
            return 0

    def is_recent(path):
        last_commit_time = get_git_last_commit_time(path)
        print(f"Path: {path}, Last commit time: {last_commit_time}, Recent: {(current_time - last_commit_time) < recent_time_frame}")
        return (current_time - last_commit_time) < recent_time_frame

    def write_indented_line(file, line, indent_level=0):
        indent = ' ' * 4 * indent_level
        file.write(f"{indent}{line}\n")

    with open(output_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>File Explorer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="HTML/bootstrap.4.6.2.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
        }
        header {
            background-color: black;
            color: white;
            div {
                display: flex;
                justify-content: space-between;
            }
            h1 {
                margin: 0;
                padding: 30px 0;
            }
            nav {
                padding: 35px 0;
            }
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        a {
            text-decoration: none !important;
            font-weight: bold;
            color: lightgrey;
        }
        a:hover {
            color: #9f9f9f;
        }
        .folder, .file {
            position: relative;
        }
        .folder {
            cursor: pointer;
            box-shadow: 0 0 6px #cb9400;
            padding: 15px 25px;
            border-radius: 20px;
            margin: 20px 0;
            font-weight: bold;
            color: #f3b100;
        }
        .folder::before {
            content: ">";
            position: absolute;
            left: 10px;
            transition: transform 0.2s;
        }
        .folder.open::before {
            transform: rotate(90deg);
        }
        .file {
            padding: 15px 25px;
            margin: 10px 0;
        }
        .html-file {
            color: #0042f3;
        }
        .html-file:hover {
            color: #002486;
        }
        .recent::after {
            content: "";
            display: inline-block;
            width: 10px;
            height: 10px;
            background-color: red;
            border-radius: 50%;
            position: absolute;
            left: -15px;
            top: 27px;
            transform: translateY(-50%);
            cursor: default;
        }
    </style>
</head>
<body>
<header class="mb-5">
    <div class="container">
    <h1>Project Index</h1>
    <nav><a href="https://github.com/HimanshuChandnani/webdev" target="_blank" class="btn btn-outline-light">Himanshu Github Page</a></nav>
    </div>
</header>
<section class="container"><ul class ="col-12">
''')

        def write_directory(path, base_path, f, indent_level=1):
            items = sorted(os.listdir(path))
            directories = [item for item in items if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
            files = [item for item in items if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]
            
            for item in directories:
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path).replace("\\", "/")
                recent_class = ' recent' if is_recent(item_path) else ''
                write_indented_line(f, f'<li class="folder{recent_class}" onclick="toggleFolder(event, this)">{item}', indent_level)
                write_indented_line(f, '<ul>', indent_level + 1)
                write_directory(item_path, base_path, f, indent_level + 2)
                write_indented_line(f, '</ul>', indent_level + 1)
                write_indented_line(f, '</li>', indent_level)

            for item in files:
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path).replace("\\", "/")
                recent_class = ' recent' if is_recent(item_path) else ''
                class_attr = 'html-file' if item.lower().endswith('.html') else ''
                write_indented_line(f, f'<li class="file{recent_class}"><a class="{class_attr}" target="_blank" href="{relative_path}">{item}</a></li>', indent_level)

        write_directory(script_dir, script_dir, f, 1)

        f.write('''
</ul></section>
<script>
    function toggleFolder(event, folder) {
        event.stopPropagation();
        var sublist = folder.querySelector('ul');
        if (sublist.style.display === 'none') {
            sublist.style.display = 'block';
            folder.classList.add('open');
        } else {
            sublist.style.display = 'none';
            folder.classList.remove('open');
        }
    }
    document.querySelectorAll('.folder ul').forEach(function(ul) {
        ul.style.display = 'none';
    });
    document.querySelectorAll('.file a').forEach(function(anchor) {
        anchor.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    });
</script>
</body>
</html>
''')

if __name__ == "__main__":
    generate_index_file()
