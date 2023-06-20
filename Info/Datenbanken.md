# Einführung
```sql
CREATE DATABASE ...
```
---
```sql
CREATE TABLE ... (
	... varchar(n) / int / decimal(n, m) / bool
	NOT NULL / PRIMARY KEY / FOREIGN KEY (...) REFERENCES ...(...)
);
```
---
```sql
INSERT INTO ... (..., ...)
	VALUES (..., ...);
```
---
```sql
UPDATE ... SET ... = ...
	WHERE ... = ...;
```
---
```sql
DELETE FROM ...
	WHERE ... = ...;
```
---
```sql
SELECT ..., ...
	FROM ...
	WHERE ... = ...
	ORDER BY ...;
```


# Grundlagen des Datenbankdesigns

## Datentypen

### Integerzahlen
![Pasted image 20221004143859](bilder/Pasted%20image%2020221004143859.png)
- xxxINT(m) m: maximal ausgegebene zahlen (display width) z.B. INT(3) = 4: 004
- xxxINT UNSIGNED: nur positiv
- BOOL = TINYINT
- AUTO_INCREMENT: nur wenn NOT NULL und PRIMARY KEY oder UNIQUE

### Dezimalzahlen

| Name             | Eigenschaften                         |
| ---------------- | ------------------------------------- |
| FLOAT(m, d)      | 4 Bytes, 8 Stellen Genauigkeit        |
| DOUBLE(m, d)     | 8 Bytes, 16 Stellen Genauigkeit       |
| DECIMAL(m [, d]) | Festkommadarstellung m <= 65, d <= 30 | 

m = Gesamtstellenanzahl
d = Anzahl der Stellen nach Dezimalpunkt
z.B. FLOAT(5, 3) 0.1235 = 0.124, 1000 = 99.999

### Datum und Uhrzeit

Name      | Eigenschaften
          -|-
DATE      | 3 Bytes, YYYY-MM-dd, 1000-01-01 bis 9999-12-31
TIME      | 3 Bytes, HH:mm:ss, +- 838:59:59
DATETIME  | 5 Bytes, YYYY-MM-dd HH:mm:ss, 1000-01-01 00:00:00 bis 9999-12-31 23:59:59
TIMESTAMP | 4 Bytes, 1970 bis 2038
YEAR      | 1 Byte, 1900 bis 2155
TIMESTAMP bei jeder Änderung des Datensatzes automatisch aktualisiert, bei neuem Datensatz automatisch gesetzt

### Zeichenketten

Name | Eigenschaften
-|-
CHAR(n) | fixe Länge n, max 255
VARCHAR(n) | variable Länge n, max 65.535
TINYTEXT | variable Länge, max 255
TEXT | variable Länge, max 65.535
MEDIUMTEXT | variable Länge, max 16.777.215
LONGTEXT | variable Länge, max 4.294.967.295

### BLOBs

Name | Eigenschaften
-----|--------------
TINYBLOB | max 255 Bytes
BLOB | max 65.535 Bytes
MEDIUMBLOB | max 16.777.215
LONGBLOB | max 4.294.967.295


### ENUM
``` SQL
name ENUM ("a", "b", "c");
			0,   1,   2
```

## Deadlocks
Zwei Prozesse wollen auf eine resource zugreifen die der andere prozess bereits glockt hat.
![Pasted image 20220907091336](bilder/Pasted%20image%2020220907091336.png)

## Transaktionen
- Transaktion wird gestartet (START TRANSACTION)
- befehle werden ausgeführt
- Transaktion wird beendet (COMMIT)

wird COMMIT nicht ausgeführt (z.b. datenbank abgestürzt) werden alle befehle bis START TRANSACTION rückgängig gemacht
