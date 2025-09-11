## About

Collection of extensions and further tips for [VS Code](https://code.visualstudio.com/).

To directly edit ```settings.json``` use in search panel ```Preferences: Open User Settings (JSON)```. Details are in [VS Code: How to Add Custom Keybindings](#vs-code-how-to-add-custom-keybindings)

## VS Code: Extensions

#### Extensions that must to be installed for better development experience

* IntelliCode
* Python, Pylance, isort, Black Formatter, pylint, Python Type Hint
* Better Comments, autoDocstring, Code Spell Checker
* Remote Development, Dev Containers, Docker, Remote - SSH
* CodeSnap, DotENV, Rainbow CSV
* Jupyter, Jupyter Cell Tags, Jupyter Keymap, Jupyter Notebook Renderers, Jupyter Slide Show
* LaTeX Workshop
* **Markdown**
    + Markdown PDF
    + Markdown Preview Mermaid Support
* YAML, Task
* **Todo Tree**
* Themes
    + GitHub Theme
    + Monokai Pro
* Go
    + templ-vscode

#### Docs/Options for the VS Code extensions

* [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
* [vscode-pdf](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf)
* [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
* [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
* [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
* Jupyter Notebook Renderers
* CodeSnap
    - Crtl+Shift + P -> Preferences: Open Settings (UI) -> codesnap -> *edit settings here*
        - (to copy directly in clipboard): Shutter Action -> Copy
* REST Client
* [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
* [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
* [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
    - [Best way to work with TODOs in VSCode](https://thomasventurini.com/articles/the-best-way-to-work-with-todos-in-vscode/)
* [LaTeX in VS Code](https://paulwintz.com/latex-in-vscode/)


## VS Code: Keyboard Shortcuts / Keybindings

* Toggle sidebar visibility / hide explorer:
    - **Ctrl+B**
* Switch focus between editor and terminal:
    - **Ctrl + \`** -> focuces on terminal (*\`* -> backtick key)
    - **Ctrl + 1** -> focuces on editor
* Switch between opened terminal in VS Code
   - **Ctrl + Shift + a** -> requires custom key bindings
* Got to file:
* 	- **Ctrl + P**

## VS Code: How to debug a Python module

Example of the ```launch.json``` to debug module (see sections: ```args```, ```msconsconverter```)
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Module",
            "type": "debugpy",
            "request": "launch",
            "module": "msconsconverter",
            "args": ["convert", "--debug", "--input-directory", "tests/data", "--output-directory", "tests/data/output"],
        }
    ]
}
```

## VS Code: How to Add Custom Keybindings

Open and edit ```Preferences: Open Keyboard Shortcuts (JSON)``` by addding
```json
// Place your key bindings in this file to override the defaults
[
  // Terminal
  {
    "key": "ctrl+shift+a",
    "command": "workbench.action.terminal.focusNext",
    "when": "terminalFocus"
  },
  {
    "key": "ctrl+shift+b",
    "command": "workbench.action.terminal.focusPrevious",
    "when": "terminalFocus"
  }
]
```

## VS Code: templ (golang)
```
{
    "[templ]": {
        "editor.defaultFormatter": "a-h.templ",
		"editor.formatOnSave": true
    },
}
```

## VS Code: Theme

Switch between themes as follows:
* Open `Command Palette`
* Type `theme`
* Select the one you want to write out
