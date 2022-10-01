import os
import pathlib

framework = int(input("What is your desired framework? Enter: \n1 for Static Site\n2 for React\n3 for Django\n>>>"))

while True:
    if framework <= 3:
        proj_name = input("What would you like to name this project?\n>>>")
        proj_dir = input("Where will this project live? Enter entire path:\n>>>")
        break
    else:
        framework = int(input("Incorrect value. What is your desired framework? Enter: \n1 for Static Site\n2 for React\n3 for Django\n>>>"))
static = "static"
react = "react"
django = "django"

if framework == 1:
    framework = static
elif framework == 2:
    framework = react 
elif framework == 3:
    framework = django

folder = pathlib.Path(proj_dir, proj_name)
folder.mkdir(parents=True, exist_ok=True)
vs_open = "code " + str(folder)
cmdl = str(folder)

# Creates a static website project
def create_static():
    index_html = folder / 'index.html'
    styles_css = folder / 'styles.css'

    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    '''

    index_html.write_text(template)
    styles_css.write_text("/* Website styles */")

    os.system(vs_open)

# Creates a React project
def create_react():
    os.chdir(cmdl)
    create ="npx create-react-app ."
    print("Your project will open once it's created. Please wait.")
    print("Creating project...")
    os.system(create)
    print("Done!")

    # Create components folder + home component
    comp_template = ''' 
    import React from 'react';

    const Home = () => {
        return(
            <div>
                <h1>Hello World</h1>
            </div>
        )
    }

    export default Home
    '''

    app_template = '''
    import'./App.css';
    import Home from '././components/home'

    function App() {
        return (
            <div>
                <Home />
            </div
        )
    }
    '''

    src_folder = str(folder) + "/src/"
    components = pathlib.Path(src_folder, 'components')
    components.mkdir(parents=True, exist_ok=True)
    home = components / 'home.jsx'
    home.write_text(comp_template)
    print("Creating component...")

    with open(home, 'r') as f:
        js_script = f.read()

    js_script = js_script.replace(js_script, comp_template)

    with open('home', 'w') as f:
        f.write(js_script)

    print("Done!")
    os.system(vs_open)

# Create a Django project
def create_django():
    app = "django-admin startproject " + proj_name + "_website"
    os.chdir(cmdl)
    print("Creating python virtual environment...")
    os.system("python -m venv virt")
    print("Activating virtual environment...")
    os.system("source virt/Scripts/activate")
    ins_django = "pip install django"
    print("Your project will open once it's created. Please wait.")
    print("Creating project...")
    os.system(ins_django)
    i = input("Press Enter to continue:\n>>>")
    os.system(app)
    print("Done!")
    os.system(vs_open)

if framework == static:
    create_static()
elif framework == react:
    create_react()
elif framework == django:
    create_django()