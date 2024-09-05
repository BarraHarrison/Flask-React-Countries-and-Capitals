## Setting up an "almost" Full Stack file structure
1. Create a new folder with the name of your "app".
2. Open inside VS Code.

## Creating the React App
3. Open a terminal inside VSCode and create our client side frontend.

- "npm run vite" will create a new project and you will
    see this as the output-> ```? Project name: > vite-project```

-   **Enter a name for your React Project**, if you don't enter a new name here you will end up with the default name *vite-project*
        -   I have named mine *client*, see below
    -   Use the arrow keys to scroll down and select *React* for our framework
    -   Use the arrow keys to scroll down and select *Javascript* for our variant
    -   ```cd {vite-project-name}```
    -   ```npm install```
    -   ```npm run dev``` -> This command will run the server, and you should see the default React and Vite logos and example page if you have done the install properly

#### Creating the Flask App

4. Open a new terminal (do **not** close the previous terminal) and navigate to the root folder of your project
   -    For example if the new terminal is inside ```root/client``` then enter ```cd ..``` to go up a directory to the root

5. Make a new folder for your backend/Flask application
    -   I have named mine *server* see below
6. Create a Virtual Environment for our Python code
    -   ```python -m venv {virtual_env_name}``` will create a virtual environment
        -   I have named mine *.venv*
        -   Confirm that the new directory created has files inside of it after being created, then close the directory
    - Activate the virtual environment via the activate script
        - Mac/Linux -> ```source {virtual_env_name}/bin/activate```
        - Windows -> ```{virtual_env_name}\Scripts\activate```
7. Install Flask
    -   ```pip install flask```

#### Example Folder Structure

```
project_root/
├── .venv/
│   ├── bin
│   ├── include
│   └── lib
│
├── client/
│   ├── node_modules/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── App.css
│       ├── App.jsx
│       ├── index.css
│       └── main.jsx
│
└── server/
    └── main.py
```
