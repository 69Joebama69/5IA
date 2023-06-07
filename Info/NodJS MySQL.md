## Variante 1
```js
const mysql = require('mysql');  
const connectionProperties = {  
	host: 'localhost',  
	user: 'root',  
	password: 'masterkey',  
	database: 'movie-db'  
};  

function getAll() {  
	const connection = mysql.createConnection(connectionProperties);  
	const sql = `  
		SELECT movies.id, title, year, published, users.username AS owner, CONCAT(users.firstname, ' ', users.secondname) AS fullname  
			FROM movies, users  
			WHERE movies.owner = users.id  
			ORDER BY title;  
	`;  
	
	connection.query(sql, (error, result) => {  
		connection.end(); 
		if (error) { throw error; }  
		console.log(result);  
	});  
}
```

- Verbindung mit query() geöffnet und end() geschlossen
- query() callback asynchron wenn Ergebnis / Fehler vorliegt


## Variante 2
movie.model.js
```js
const mysql = require('mysql');  
const connectionProperties = { ... };  

function getAll(processResultCallback) {  
	const connection = mysql.createConnection(connectionProperties);  
	const sql = ` ... `;  
	connection.query(sql, (error, result) => {  
		connection.end();  
		processResultCallback(error, result);  
	});
}
```
movie.controller.js
```js
function listAction(request, response) {  
	movieModel.getAll((error, result) =>  
		response.send(
			error ? 
				movieView.renderError(error) :  
				movieView.renderList(result))  
	);  
}
```

## Variante 3
movie.model.js
```js
const mysql = require('mysql');  
const connectionProperties = { ... };  

function getAllPromise() {  
	return new Promise((resolve, reject) => {  
		const connection = mysql.createConnection(...);  
		const sql = ` ... `;  
		connection.query(sql, (error, result) => {  
			connection.end();  
			if (error) { reject(error); }  
			resolve(result);  
		});  
	});  
}
```
movie.controller.js
```js
function listAction(request, response) {  
	movieModel.getAllPromise()  
		.then(result => response.send(movieView.renderList(result)))  
		.catch(error => response.send(movieView.renderError(error)));  
}
```