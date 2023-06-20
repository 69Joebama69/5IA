## Einfache Buchhaltung
- ein Buch
- betriebliche einnahmen und ausgaben chronologisch
- gegenüberstellung der einnahmen und ausgaben an Jahresende ([#Einnahmen-Überschuss-Rechnung](#Einnahmen-%C3%9Cberschuss-Rechnung))

## Doppelte Buchhaltung
- mehrere Bücher
- Gliederung nach Soll und Haben
- Gewinnermittlung aus Bilanz und Gewinn - und Verlust - Rechnung

### Einnahmen-Überschuss-Rechnung
- Einnahmen und Ausgaben werden gegenübergestellt
- Am Ende bleibt Gewinn oder Verlust
- Gewinn / Verlust = Betriebseinnahmen - Betriebsausgaben

### Anlagevermögen (AV)
- längerer Zeitraum (über 1 Jahr) im Unternehmen
- z.B. Grundstücke, Maschinen, Wertpapiere

**Arten:**
1. **Sachanlage**
	- materiell
	- langfristig im Unternehmen (mindestens 12 Monate)
	- Maschinen, Büroeinrichtung

2. **Immaterielle Anlagen**
	- ungreifbar
	- Lizenzen, Patente

3. **Finanzanlagen**
	- monetär
	- langfristig
	- Wertpapiere, Finanzanlagen

### Umlaufvermögen (UV)
- kurze Zeit (unter 1 Jahr)

**Bestandteile:**
1. Vorräte
2. Forderungen
3. Liquide Mittel
4. Wertpapiere

### Fremdkapital (FK)
- Schulden des Unternehmens in Bilanz
- gehört fremden Kapitalgebern
- Schulden des Unternehmens

**Bestandteile:**
1. **Rückstellungen:**
	- ungewisse Verbindlichkeiten
	- Höhe und Bestehen nicht konkret
	  
1. **Verbindlichkeiten:**
	- finanzielle Verpflichtungen des Unternehmens (Schuldner) gegenüber Dritten (Gläubiger)
	- **Verbindlichkeiten**
	- **Erhaltene Anzahlungen**
	- **Verbindlichkeiten gegenüber Kreditinstituten**
	- **Verbindlichkeiten aus Lieferungen**
	- **Verbindlichkeiten aus Wechseln**
	- **Sonstige Verbindlichkeiten**

### Eigenkapital (EK)
- eigenem Kapitalanteil
- steht unbefristet zur Verfügung
- keine Rückzahlungspflicht

**Bestandteile:**
1. **Gezeichnetes Kapital**
	- verpflichtet bei Gründung Kapitaleinlage zu Hinterlegen (Stammeinlage / Grundkapital)
	- diese Einlage + spätere Kapitalerhöhungen
1. **Kapitalrücklagen**
	- finanzielle Reserven gewährleisten


### Inventar
```mermaid
graph TD
id1(Inventar)

id2.1(Vermögen)
id2.2(Schulden)

id3.1(Anlagevermögen)
id3.2(Umlaufvermögen)
id3.3(Langfristige Schulden)
id3.4(Kurzfristige Schulden)

id1 --> id2.1 & id2.2

id2.1 --> id3.1 & id3.2
id2.2 --> id3.3 & id3.4
```
Eigenkapital = Vermögen - Schulden