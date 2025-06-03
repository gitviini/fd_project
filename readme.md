## FD Project

By: 
[Vinicius Gabriel](https://github.com/gitviini/),
[Juliana Comparoto](https://github.com/comparoto),
[Marcos Fraga](https://github.com/MarcTony0),
[Matheus de Freitas](https://github.com/matheusprojects),
[Joanna Farias](https://github.com/Joanna-Farias),
[Malu](https://github.com/alumiria).

## Running project
```shell
git clone https://github.com/gitviini/fd_project/ &&
cd fd_project &&
python ./run.py
```

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
        └── util.py # Tools (clear terminal)
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
* Modules: part layers of aplication by files, Example: `run.py`, `users.py` e etc.
