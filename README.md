# Creazione e Attivazione di un Virtual Environment su Linux

Questa guida spiega come creare ed attivare un **virtual environment** in Python utilizzando il comando `python3 -m venv`, esclusivamente in ambiente Linux.

---

## Creare il virtual environment

1. Apri il terminale.
2. Spostati nella cartella venvs:
    
    ```bash
    cd venvs
    ```
3. Crea il virtual environment (qui chiamato `lezione1`):
    
    ```bash
    python3 -m venv lezione1
    ```

Questo comando genera una cartella `lezione1` contenente gli script e i file necessari.

---

## Attivare il virtual environment

1. Entra nella cartella `lezione1`:
    
    ```bash
    cd lezione1
    ```
2. Attiva il virtual environment:
    
    ```bash
    source bin/activate
    ```
3. Se l’attivazione ha avuto successo, vedrai comparire il nome del tuo ambiente a sinistra del prompt, per esempio:

    ```
    (lezione1) fabio@DESKTOP-TCN1R7V:~/PIN
    ```

---

## Disattivare il virtual environment

Per disattivare l’ambiente virtuale, ti basta eseguire:

```bash
deactivate
```