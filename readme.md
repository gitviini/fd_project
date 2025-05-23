## FD Project

By: 
[Vinicius Gabriel](https://github.com/gitviini/),
[Juliana Comparoto](https://github.com/comparoto),
[Marcos Fraga](https://github.com/MarcTony0),
[Matheus de Freitas](https://github.com/matheusprojects),
[Joanna Farias](https://github.com/Joanna-Farias),
[Malu](https://github.com/alumiria).

## Architecture (in Layers)

```shell
├── jsons #Fouder of .jsons
│   ├── animals.json
│   ├── support_points.json
│   └── users.json
├── readme.md
├── run.py #Run project (python run.py)
└── src 
    ├── animals #Animals show and manager
    │   ├── display.py
    │   └── manager.py
    ├── support_points #Points show and manager
    │   ├── display.py
    │   └── manager.py
    ├── users #Users show and manager
    │   ├── display.py
    │   └── manager.py
    └── utils #Utils files functions\libraries
        ├── constants.py #Constants (COLORS and STYLES)
        ├── json_parser.py #Json Parser (JSON -> DICT and DICT -> JSON)
        └── util.py # Tools (clear terminal, receive inputs, colors ...)
```

## Architecture pattern

* Comments: begin for verbs;
* Variables and Constants: use snack_case;
* Functions: use snack_case, try-except and returns one type:

```python
def function(*args) -> int:
	try:
		...
	except Exception as error:
		...
	return 0
```
* Modules: part layers of aplication by files, Example: `run.py`, `json.py`, `users.py` e etc.
