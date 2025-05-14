## FD Project

By: 
[v.ii.n.i](https://github.com/gitviini/),
[Juliana Comparoto](https://github.com/comparoto),
[Marcos Fraga](https://github.com/MarcTony0),
[Matheus](https://github.com/matheusprojects).

## Architecture (in Layers)

``` python
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
        └── json-parser.py
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
