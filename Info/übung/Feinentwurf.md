benutzer (<u>bid</u>, bvorname, bnachname, bemail, btelefon)
fahrer (<u>bid</u>, ffsnummer, ffsverfalldatum, ffoto, fkennzeichen, fautotyp)
mitfahrer (<u>bid</u>, mausweisnummer)
fahrten (<u>fid</u>, bid, fastartzeitdatum, fastartstadt, fastartadresse, fazielstadt, fazieladresse, fadauer, fapreis, faanmerkungen, fageschlossen)
reservierungen (<u>faid, bid</u>, rakzeptiert)
bewertungen (<u>fid, bid</u>, bwfuerfahrer, bwbewertung, bwtext)
a)
```sql
SELECT b.bvorname, b.bnachname, fa.fastadt, fa.fapreis, f.fkennzeichen, f.fautotyp
	FROM benutzer b, fahrer f, fahrten fa
	WHERE b.bid = f.bid
		AND f.bid = fa.bid
		AND fa.fastartadresse LIKE ?
		AND fa.fazieladresse LIKE ?
		AND fa.fastartzeitdatum LIKE ?
		AND fa.fageschlossen = FALSE
	ORDER BY 3;
```

c)
```sql
SELECT b.bvorname, b.bnachname, AVG(bw.bwbewertung)
	FROM benutzer b, bewertungen bw, reservierungen r,
	WHERE bw.bwfuerfahrer = TRUE
		AND bw.fid = ?
		
```