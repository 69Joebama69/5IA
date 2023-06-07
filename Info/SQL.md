```sql 
-- INSERT
INSERT INTO artikel(hnummer, rbezeichnung, repreis, rvpreis, rbestand, rsollbestand)  
	VALUES (10, "NXJ-2389-9", 230.60, 349.90, 150, 150);

-- UPDATE
UPDATE artikel  
	SET rbestand = 0  
	ORDER BY rvpreis DESC  
	LIMIT 10;

-- DELETE
DELETE positionen, auftraege  
	FROM positionen, auftraege, kunden  
	WHERE kfname = "Ahnert" AND kname = "Lisa"  
		AND kunden.knummer = auftraege.knummer  
		AND auftraege.anummer = positionen.anummer;

-- SELECT
SELECT rnummer, rvpreis * rbestand AS gesamt  
	FROM artikel  
	ORDER BY gesamt DESC;

SELECT IF(CHARACTER_LENGTH(rbezeichnung) <= 13, 
		  rbezeichnung, 
		  CONCAT(SUBSTRING(rbezeichnung, 1, 5), "...", 
		  SUBSTRING(rbezeichnung, 
			  CHARACTER_LENGTH(rbezeichnung) - 4, 5)))  
	FROM artikel;

-- NULL
SELECT *  
	FROM artikel  
	WHERE rbeschreibung = NULL;

-- BETWEEN
SELECT rnummer, rbezeichnung  
	FROM artikel  
	WHERE rvpreis BETWEEN 200 AND 500;

-- IN
SELECT *  
	FROM artikel  
	WHERE rnummer NOT IN (11, 22, 44);

-- LIKE (% = *)
SELECT knummer, kfname, kname  
	FROM kunden  
	WHERE kfname LIKE "K%";
	WHERE kfname LIKE "K____";
	WHERE kname NOT LIKE "%er";
	WHERE rbezeichnung LIKE "%\%%";

-- Einfache Unterabfragen
SELECT kfname, kname  
	FROM kunden  
	WHERE knummer =  
		(SELECT knummer  
			FROM auftraege  
			WHERE anummer = 20);
			
-- Unterabfragen mit IN
SELECT knummer  
	FROM auftraege  
	WHERE anummer IN  
		(SELECT anummer  
			FROM positionen  
			WHERE rnummer = 33);

-- ANY / ALL
-- ANY: Unterabfrage mindestens 1 Ergebnis
-- Nummern und Namen aller Kunden, deren Kundennummer nicht die größte ist.
SELECT knummer, kfname, kname  
	FROM kunden  
	WHERE knummer < ANY  
		(SELECT knummer  
			FROM kunden);
-- ALL: Unterabfrage alle Ergebnisse
-- Postleitzahl des Wohnortes des Kunden mit der kleinsten Kundennummer.
SELECT kplz  
	FROM kunden  
	WHERE knummer <= ALL  
		(SELECT knummer  
			FROM kunden);

-- EXISTS
SELECT kfname, kname  
	FROM kunden  
	WHERE EXISTS  
		(SELECT *  
			FROM auftraege  
			WHERE knummer = kunden.knummer  
			AND MONTH(adatum) = 1);

-- Aggregatfunktionen
SELECT COUNT(*)  
	FROM kunden;
SELECT MIN(knummer)  
	FROM kunden;
SELECT MAX(kfname)  
	FROM kunden;
SELECT SUM(pmenge)  
	FROM positionen;
SELECT AVG(DISTINCT rsollbestand)  
	FROM artikel;

-- GROUP BY
SELECT kort  
	FROM kunden  
	GROUP BY kort {WITH ROLLUP};

-- HAVING
SELECT kort
	FROM kunden
	GROUP BY kort
	HAVING COUNT(*) = 2;

-- ORDER BY
SELECT *  
	FROM artikel  
	ORDER BY rnummer DESC {/ ASC};

-- LIMIT
SELECT *
	FROM kunden
	ORDER BY kfname
	LIMIT 15;

-- RAND
SELECT *
	FROM artikel
	ORDER BY RAND()
	LIMIT 1;

-- UNION
SELECT kort
	FROM kunden
UNION
SELECT hort
	FROM hersteller
ORDER BY 1;

-- Verbund
-- Kartesisches Produkt
SELECT *
	FROM auftraege, positionen;
-- Gleichverbund (Equijoin)
SELECT *
	FROM artikel, hersteller
	WHERE artikel.hnummer = hersteller.hnummer;
-- Natürlicher Verbund (Natural Join)
SELECT auftraege.*, rnummer, pmenge  
	FROM auftraege, positionen  
	WHERE auftraege.anummer = positionen.anummer;
-- Theta-Verbund (Theta-Join)
SELECT knummer, kfname, kname, kort, hnummer, hname, hort
	FROM kunden, hersteller
	WHERE kort <> hort;
-- Selbstverbund (Selfjoin)
SELECT DISTINCT k1.knummer, k1.kfname, k1.kname, k1.kort,
	FROM kunden k1, kunden k2
	WHERE k1.kort = k2.kort AND k1.knummer <> k2.knummer;
```
