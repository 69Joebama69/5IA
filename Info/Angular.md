
## Projekt erstellen
	$ ng new (Projekt name) --prefix=(prefix)


# Klassen
	$ ng generate class shared/(klassen name)

```ts
export class Test {
	constructor (idk?: number, idk2: number = 1) {} // idk? -> optional, idk2 -> default wert = 1
}
```


# Komponenten

	$ ng generate component (Component name)
- Teile der Anwendung
- **COmponent Decorator** enthält Konfiguration
- **Selektor** name in html
- **templateUrl** path zu html
- **styleUrls** path zu css / scss
```ts
@Component({
	selector: 'test',
	templateUrl: './test.component.html',
	styleUrls: ['./test.component.scss']
})
```

**ngOnInit**: ausgeführt wenn Komponente initialisiert ist
```ts
export class Test implements OnInit {
	ngOnInit() {}
}
```


## Binding
### Property:
\[property\]
```html
<a [href]="person.homepage">{{ person.homepage }}</a><br>
```

### Event:
\(event\)
```html
<button (click)= "myClickHandler(id.value)">Drück mich</button>
```

### Two-Way:
\[\(\)\]
```html
<input type="text" [(ngModel)]="registrationyear">
```

## Strukturdirektiven
- \*ngIf
```html
<div *ngIf="person.height > 1.85">Die Person ist groß</div>
```
- \*ngFor(let ... of ...)
```html
<li *ngFor="let emailaddress of person.emailaddresses">  
	{{ emailaddress }}  
</li>
```
- \[ngSwitch\]
```html
<div [ngSwitch]="person.address.postcodetown">  
	<span *ngSwitchCase="'39100 Bozen'">Kommt von Bozen</span>  
	<span *ngSwitchCase="'39012 Meran'">Kommt von Meran</span>  
	<span *ngSwitchDefault>Kommt von anderswo</span>  
</div>
```

## Formularverarbeitung
```html
<input type="text" [(ngModel)]="registrationyear">
```
- ngModel bindet variable an input


## Werteübergabe
datei | Komponente
-|-
test.component.html | TestComponent \[...\]="..."
email-list.component.ts | EmailListComponent @Input()

test.component.html:
```html
<ta-email-list [emailaddresse]="person.emailaddresse"></ta-email-list>
```
email-list.component.ts:
```ts
export class EmailListComponent implements OnInit {  
	@Input() emailaddresse!: string;
	ngOnInit() {}
}
```

## Werterückgabe
```ts
export class SearchTermComponent implements OnInit {  
	@Output('searchTerm') changeEvent: EventEmitter<string>;  
	constructor() {  
		this.changeEvent = new EventEmitter<string>();  
	}  
	emitSearchTermChange(searchTerm: string) {  
		this.changeEvent.emit(searchTerm);  
	}  
}
```

```html
<input #searchTerm type="text" (keyup)="emitSearchTermChange(searchTerm.value)"
```


# Flex-Layout + Material

Material:
	$ ng add @angular/material
flex-layout:
	$ npm install @angular/flex-layout@12.0.0-beta.35


# Service
```ts
@Injectable()  
export class WeatherService { }
```

```ts
import { WeatherService } from './shared/weather-service';
@NgModule({
	imports: [ ],
	providers: [ WeatherService* ]
})
export class AppModule { }
```

-> Service kann in gesamter Anwendung verwendet werden:
```ts
export class StationListComponent implements OnInit {
	constructor(private ws: WeatherService) { }
	ngOnInit() { 
		this.ws.getAll(); 
	}
}
```

## Konfiguration
```ts
providers: [  
	{ provide: 'config', useValue: { showErrors: true, url: '...' } }  
]
```
```ts
constructor(@Inject('config') private conf: any) {  
	console.log(`${conf.showErrors} ${conf.url}`);  
}
```


# Routing
- Angular Single Page Applikation
	-> bei klicken auf link Seite nicht neu von Server laden
- soll von Suchmaschinen angezeigt werden
- Browser Verlauf + Lesezeichen korrekt gesetzt
- HTML5 History API

app.component.html: \<router-outlet\>
	-> station-detail.component.html \<router-outlet\>
		-> temperature-detail.component.html

app-routing.module.ts:
```ts
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
	{ path: '', component: HomeComponent, pathMatch: 'full'1 },
	{ path: 'home', component: HomeComponent },
	{ path: 'stations', component: StationListComponent },
	{ path: 'station', component: StationDetailComponent,
		children: [
		{ path: 'all/:code', component: AllDetailComponent },
		{ path: 'temperature/:code', component: TemperatureDetailComponent },
		]
	}
];

@NgModule({
imports: [ RouterModule.forRoot(routes) ],
exports: [ RouterModule ],
})
export class AppRoutingModule { }
```
routes verwenden:
```html
<a routerLink="/home">Home</a>
<a routerLink="/stations">Stations</a>
```

### Parameterübergabe zu Route
```html
<a routerLink="/station/all/{{ station.code }}">  
	{{ station.name }}  
</a>
```

### Parameter lesen
```ts
import { ActivatedRoute } from '@angular/router';  
export class AllDetailComponent implements OnInit {  

	constructor(private route: ActivatedRoute, private ws: WeatherService) { }  
	ngOnInit() {  
		console.log(this.route.snapshot.params.code); 
	}  
}
```