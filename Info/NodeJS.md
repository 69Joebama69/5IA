# Text Web-Server
```js
const http = require('http');
const server = http.createServer(function(request, response) {  
	response.writeHead(200, { 'content-type': 'text/plain; charset=utf8' });  
	response.write('Hello ');  
	response.end('World');  
});

server.listen(8080, function() {  
	console.log('Server is listening to http://localhost:8080');  
});
```

# HTML Web-Server
```js
const http = require('http');
const server = http.createServer(function(request, response) {
	response.writeHead(200, { 'content-type': 'text/html; charset=utf8' });
	const body = `
		<DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8">
			<title>Node.js HTML</title>
		</head>
		<body>
			<h1 style="color:green">Hello World</h1>
		</body>
		</html>
		`;
	response.end(body);
});
```

# Dynamische Antwort
```js
const http = require('http');
const url = require('url');
const server = http.createServer(function(request, response) {
	response.writeHead(200, { 'content-type': 'text/html; charset=utf8' });  
	const parsedUrl = url.parse(request.url, true);
	const body = `
		<DOCTYPE html>  
		<html>
		<head>
			<meta charset="utf-8">
			<title>Node.js HTML</title>
		</head>
		<body>
			<h1 style="color:green">Hello ${parsedUrl.query.name}</h1>
		</body>
		</html>
		`;
	response.end(body);
});
```
Bsp: localhost:8080/?name=Joe
```html
<h1>Hello Joe</h1>
```


# Module
**Vorteile:**
- _Wiederverwendbarkeit_
- Bessere _Testbarkeit_
- _Parallelisierbarkeit_
- _Austauschbarkeit_

## Globale Objekte/Variablen/Funktionen, Laden von Modulen
```js
console.log(`${__filename} ${__dirname}`);
const filename = 'output.txt';
const fs = require('fs');
```

CommonJS-Module | ECMAScript-Module
-|-
require() liefert Objekt für öffentliche Schnittstelle der Datei | Neuer Standart, experimentell

## CommonJS-Module
```js
const a = 3;  
function add(a, b) {  
	return `${a} + ${b} = ${a + b}`;  
}  

class User {  
	constructor(name, password) {  
		this.name = name;  
		this.password = password;  
	}  
	doSomething() {  
		console.log(`${this.name} doesSomething`);  
	}  
}  

const user = {  
	name: 'Sepp',  
	password: 'seppentinen'  
}  

module.exports = { a, add, user, User };
```
```js
const commonJS = require('./module-commonJS');  
console.log(commonJS.a);  
console.log(commonJS.add(commonJS.a, 4));  
console.log(commonJS.user);  
const user = new commonJS.User('Elfriede', 'rike');  
console.log(user.name);  
user.doSomething();
```
**Output:**
```
3
3 + 4 = 7
{ name: 'Sepp', password: 'seppentinen' }
Elfriede
Elfriede doesSomething
```

### Destructuring
Extrahiert Elemente aus Objekten und Arrays
```js
const { a, add } = require('./module-commonJS');
console.log(a);
console.log(add(a, 4));
```

### Export einer Funktion
```js
module.exports = function (a, b) {
	return `${a} + ${b} = ${a + b}`;
};
```
```js
const add = require('./module-commonJSFunction');
console.log(add(3, 4));
```


## ECMAScript-Module
**Vorraussetzungen:**
- package.json:
```json
{ "type": "module" }
```
- bei import angabe von extension

```js
export const a = 3;  
export function add(a, b) {  
	return `${a} + ${b} = ${a + b}`;  
}
export class User {  
	constructor(name, password) {  
		this.name = name;  
		this.password = password;  
	}  
	doSomething() {  
		console.log(`${this.name} doesSomething`);  
	}  
}
export const user = {  
	name: 'Sepp',  
	password: 'seppentinen'  
}  
```
```js
import { a, add, user as pureUser, User } from './module-ECMAScript.js';  
console.log(a);  
console.log(add(a, 4));  
console.log(pureUser);  
const user = new User('Elfriede', 'rike');  
console.log(user.name);  
user.doSomething();
```

```js
function mul(a, b) {  
	return `${a} * ${b} = ${a * b}`;  
}  
function div(a, b) {  
	return `${a} / ${b} = ${a / b}`;  
}  
export * from './module-ECMAScript.js';  
export { mul as default, mul, div };
```
```js
import { add, a, user as pureUser, User, mul } from './module-ECMAScriptExpanded.js';  
import x from './module-ECMAScriptExpanded.js';  
import * as y from './module-ECMAScriptExpanded.js';

console.log(x(1, 2));  
console.log(y.add(5, 6));  
console.log(y.mul(5, 6));  
console.log(y.div(5, 6));  
console.log(a);  
console.log(add(a, 4));  
console.log(mul(a, 4));  
console.log(div(a, 4)); // Fehler  
console.log(pureUser);  
const user = new User('Elfriede', 'rike');  
console.log(user.name);  
user.doSomething();
```

# Express
- Umgang mit Requests
- Auflösen von URLs
- Session-Management
- Authentifizierung
- Dateiuploads

![Pasted image 20230418170107](Pasted%20image%2020230418170107.png)
- über Request- und Response-Object Zugriff auf Anfragen des Clients
- Routing: welche Methode die Request bearbeitet
- Middleware: können integriert werden (Cookies, Zugriff auf POST-Parameter)

**Initialisierung**
```js
const express = require('express');  
const app = express();  

app.get('/a/:b', (request, response) => {  
	console.log(request.protocol);  
	console.log(request.method);  
	console.log(request.originalUrl);  
	console.log(request.path);  
	console.log(request.params);  
	console.log(request.params.b);  
	console.log(request.query);  
	console.log(request.query.x);  
	response.send('Meine erste express Anwendung');  
});  

app.listen(8080, () => console.log('Server listen on port 8080'));
```
http://localhost:8080/a/foo?x=3&y=4
- path: /a/b
- params: { b: 'foo' }
- query: { x: '3', y: '4' }

**params:**
in Route mit : gekennzeichnet

**query**
in URL mit ? eingeleitet, mit & getrennt, mit name=wert gesetzt

## MVC-Pattern

Name | Aufgabe 
-|-
**M**odel | <ul><li>Datenhaltung</li><li>Einfügen, Löschen, Ändern, Auflisten</li><li>Datenbankzugriffe</li></ul>
**V**iew | <ul><li>Darstellung</li><li>Mit Daten gefüllte HTML-Templates</li></ul>
**C**ontroller | <ul><li>Steuerungslogik</li><li>Verbindet Model und View</li></ul>

- Anwendung in fachliche / thematische Bereiche gegliedert (accont, user)
- Jeder Bereich = Modul
- eigenen Router
- .model / .view / .controller

index.js
```js 
const express = require('express');  
const app = express();  
const bodyParser = require('body-parser');  

app.use(bodyParser.urlencoded({ extended: false }));  

const movieRouter = require('./movie/movie.router.js');  
app.use('/movie', movieRouter);  

app.get('/', (request, response) => response.redirect('/movie'));  
app.use(express.static(__dirname));  

app.listen(8080, () => console.log('Server listen on port 8080'));
```
- bodyParser: Verarbeitung von Daten im JSON-Format
- npm intall body-parser
- routen die mit /movie beginnen über movieRouter verarbeitet
- Laden von statischen Inhalten (CSS, js)

movie.router.js
```js
const express = require('express');  
const router = express.Router();  
const { listAction, removeAction, editAction, saveAction } = require('./movie.controller.js');  

router.get('/', listAction);  
router.get('/remove/:id', removeAction);  
router.get('/edit/:id?', editAction);  
router.post('/save', saveAction);  

module.exports = router;
```
- funktionen werden request und response übergeben
- optionale Parameter ?

movie.controller.js
```js
const movieModel = require('./movie.model.js');  
const movieView = require('./movie.view.js'); 

function listAction(request, response) {  
	response.send(movieView.renderList(movieModel.getAll()));  
}  

function removeAction(request, response) {  
	movieModel.remove(request.params.id);  
	response.redirect(request.baseUrl);  
}  
function editAction(request, response) {  
	let movie = { id: '-1', title: '', year: '' };  
	if (request.params.id) {  
		movie = movieModel.get(request.params.id);  
	}  
	response.send(movieView.renderMovie(movie));  
}  

function saveAction(request, response) {  
	const movie = {  
		id: request.body.id,  
		title: request.body.title,  
		year: request.body.year  
	};  
	movieModel.save(movie);  
	response.redirect(request.baseUrl);  
}  
module.exports = { listAction, removeAction, editAction, saveAction };
```

movie.model.js
```js
const { v4: uuid } = require('uuid');  

let data = [  
	{ id: uuid(), title: 'Iron Man', year: '2008' },  
	{ id: uuid(), title: 'Thor', year: '2011' },  
	{ id: uuid(), title: 'Capitain America', year: '2001' }  
]; 

function getAll() {  
	return data;  
}  

function remove(id) {  
	data = data.filter(movie => movie.id !== id);  
}  

function get(id) {  
	return data.find(movie => movie.id === id);  
}  

function save(movie) {  
	if (movie.id === '-1') {  
		movie.id = uuid();  
		data.push(movie);  
	} else {  
		data = data.map(item => item.id === movie.id ? movie : item);  
	}  
}  

module.exports = { getAll, remove, get, save };
```

movie.view.js
```js
function renderList(movies) {  
	return `  
		<!DOCTYPE html>  
		<html lang="en">  
		<head>  
			<meta charset="UTF-8">  
			<title>Filmliste</title>  
			<link rel="stylesheet" href="/style.css">  
		</head>  
		<body>  
			<table>  
				<tr><th>Id</th><th>Titel</th><th>Jahr</th><th></th><th></th></tr>  
				${movies.map(movie => `
					<tr>
						<td>${movie.id}</td>  
						<td>${movie.title}</td>
						<td>${movie.year}</td>  
						<td><a href="/movie/remove/${movie.id}">Löschen</a></td>
						<td><a href="/movie/edit/${movie.id}">Ändern</a></td>
					</tr>
				`).join('')}  
			</table>  
			<a href="/movie/edit">Neu</a>  
		</body>  
		</html>  
	`;  
}
// ...
```
