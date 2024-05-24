## About

Collection of extensions and further tips for [VS Code](https://code.visualstudio.com/).

## VS Code: Extensions

#### Extensions that must to be installed for better development experience

* Python, Pylance, IntelliCode, autoDocstring, Python Type Hint
* Remote Development, Dev Containers, Docker, Remote - SSH
* Better Comments, isort, Black Formatter, Code Spell Checker
* CodeSnap, DotENV, Rainbow CSV, indent-rainbow
* Jupyter, Jupyter Cell Tags, Jupyter Keymap, Jupyter Notebook Renderers, Jupyter Slide Show
* LaTeX Workshop
* **Markdown**: Markdown PDF, Markdown PDF, Markdown Preview Mermaid Support****
* YAML

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


