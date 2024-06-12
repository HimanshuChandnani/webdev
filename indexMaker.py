import os

def generate_index_file():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    output_file = os.path.join(script_dir, 'index.html')
    
    with open(output_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>File Index</title>
    <link rel="stylesheet" href="HTML/bootstrap.4.6.2.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
        }
        header {
            background-color: black;
            color: white;
        }
        header h1 {
            margin: 0;
            padding: 30px 80px;
        }
        ul {
            list-style-type: none;
        }
        a {
            text-decoration: none !important;
            font-weight: bold;
            color: lightgrey;
        }
        a:hover {
            color: #9f9f9f;
        }
        .folder {
            cursor: pointer;
            box-shadow: 0 0 6px #cb9400;
            padding: 15px 25px;
            border-radius: 20px;
            margin: 20px 0;
            display: table;
            font-weight: bold;
            color: #f3b100;
            position: relative;
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
            padding: 9px 25px;
            margin: 10px 0;
        }
        .html-file {
            color: #0042f3;
        }
        .html-file:hover {
            color: #002486;
        }
    </style>
</head>
<body>
<header class="mb-5"><h1>Project Index</h1></header>
<ul>
''')

        def write_directory(path, base_path, f):
            f.write('<ul>')
            items = sorted(os.listdir(path))
            # Separate directories and files
            directories = [item for item in items if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
            files = [item for item in items if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]
            
            # Write directories first
            for item in directories:
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path).replace("\\", "/")
                f.write(f'<li class="folder" onclick="toggleFolder(event, this)">{item}')
                write_directory(item_path, base_path, f)
                f.write('</li>')

            # Write files afterwards
            for item in files:
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path).replace("\\", "/")
                class_attr = 'html-file' if item.lower().endswith('.html') else ''
                f.write(f'<li class="file"><a class="{class_attr}" href="{relative_path}">{item}</a></li>')
            
            f.write('</ul>')

        write_directory(script_dir, script_dir, f)

        f.write('''
</ul>
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
</script>
</body>
</html>
''')

if __name__ == "__main__":
    generate_index_file()
