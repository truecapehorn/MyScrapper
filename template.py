from jinja2 import Environment, FileSystemLoader


def make_template(content):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True
    template = env.get_template('about.html')
    output = template.render(content=content)
    #print(output)
    return output

if __name__ == '__main__':

    out=make_template({"price": 1223.45, "url": "www.test.pl"},)
    print(out)

