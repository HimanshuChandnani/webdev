import os

def generate_index_file(output_file='index.html'):
    with open(output_file, 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Project Index</title>
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

        def write_directory(path, f):
            f.write('<ul>')
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    f.write(f'<li class="folder" onclick="toggleFolder(this)">{item}')
                    write_directory(item_path, f)
                    f.write('</li>')
                else:
                    file_path = os.path.join(path, item).replace("\\", "/")
                    f.write(f'<li class="file"><a href="{file_path}">{item}</a></li>')
            f.write('</ul>')

        write_directory('.', f)

        f.write('''
</ul>
<script>
    function toggleFolder(folder) {
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
