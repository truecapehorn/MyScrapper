from jinja2 import Environment, FileSystemLoader

def make_template(content):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about.html')

    output = template.render(content=content)
    print(output)
    return output
