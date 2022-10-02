# PyAutoDev

Python Automated-Development is a tool that allows users to bypass installation and set-up for web development projects. By using your CLI of choice (PowerShell tested and recommended), developers can create static websites, React projects, and Django projects by answering three simple questions.

For static sites, PyAutoDev creates an index.html and styles.css file in the users determined directory.
For React projects, PyAutoDev creates a fresh React project, a component folder, and a "Home" component that's ready to be added to the app.js file.
For Django projects, PyAutoDev creates a fresh Django project ready for development.

### Requirements and Recommendations
* PowerShell
* Python
* VS Code

### How to use:
* Clone this repository and cd into the directory where it's housed.
* Run the command `python pad.py`
* Answer the three questions:
  * What is your desired framework?
  * What would you like to name your project?
  * Where will this project live? (Full path ending with "\")

After that, PyAutoDev will create and open your project in VS Code!

![](https://github.com/dacrews/PyAutoDev/blob/main/gif.gif)

### Future updates:
* Ability to utilize more frameworks
* GUI
* Mac compatibility 
