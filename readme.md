## FD Project

By: [v.ii.n.i](https://github.com/gitviini/)

## Architecture pattern

* Comments: begin for verbs;
* Variables and Constants: use snack_case;
* Functions: use snack_case and try-except to returns dict: 
`
response = {
	data: {
		message: "...",
		content: dict
	},
	error: {
		message: "...",
		content: dict
	}
}
`
* Modules: part layers of aplication by files, Example: `run.py`, `json.py`, `users.py` e etc.
