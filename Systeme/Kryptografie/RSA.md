Ronald **R**ivest, Adi **S**hamir, Leonard **A**dleman

- asymmetrisch
- Primzahlen:
	- Primzahlen multiplizieren = einfach
	- durch Primfaktorenzerlegung Faktoren finden = schwierig
- public Key (e, N)
- private Key (d, N)
- N = RSA-Modul
- e = Verschlüsselungsexponenten
- d = Entschlüsselungsexponenten

# Verfahren
- 2 Random Primzahlen mit großem Abstand (p, q)
- p != q
- N = p * q
- φ(N) = (p-1) ∗ (q-1)
- 1 < e < φ(N)
- e ∗ d ≡ 1 (mod φ(N))
- Verschlüsselung: c = m^e (mod N)
- Entschlüsselung: m = c^d (mod N)