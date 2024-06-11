import os

def generate_index_file():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    output_file = os.path.join(script_dir, 'index.html')
    
    with open(output_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>File Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        ul {
            list-style-type: none;
        }
        .folder {
            cursor: pointer;
            margin: 5px 0;
        }
        .file {
            margin-left: 20px;
        }
    </style>
</head>
<body>
<h1>Project Index</h1>
<ul>
''')

        def write_directory(path, base_path, f):
            f.write('<ul>')
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path).replace("\\", "/")
                if os.path.isdir(item_path):
                    f.write(f'<li class="folder" onclick="toggleFolder(event, this)">{item}')
                    write_directory(item_path, base_path, f)
                    f.write('</li>')
                else:
                    f.write(f'<li class="file"><a href="{relative_path}">{item}</a></li>')
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
        } else {
            sublist.style.display = 'none';
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
