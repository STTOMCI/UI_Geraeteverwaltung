# Mockup der UI der Geräteverwaltung

Dieses Projekt stellt ein Mockup für eine Sotware zur Geräteverwaltung an einer Hochschule da.

Mit dieser Software sollen Geräte wie z.B. (z.B. Laser-Cutter, 3D-Drucker, etc.) verwaltet werden können.
Zu dieser Verwaltung gehören unter anderm Funktionen wie die Wartungsplanung und die Reservierung von Geráten für Forschungsprojekte.

## Beschreibung

Das Endgültige Programm soll folgende Umstände berücksichtigen:
* In der Hochschule gibt es diverse Geräte, die von den Studierenden und Forschenden verwendet werden können
* Viele der Geräte müssen in regelmäßigen Abständen gewartet werden
* In dieser Zeit sind die Geräte nicht verfügbar, ebenso werden die Geräte für bestimmte Zeiträume reserviert (dringende Forschungsprojekte, Lehrlabore etc.)
* Das nächste Wartungsdatum wird durch die Software geplant, kann aber vom Administrator geändert werden
* Für jedes Gerät gibt es eine verantwortliche Person, welche sich jedoch über die Zeit ändern kann
* Alleiniger Nutzer der Software ist der Administrator, welcher die Geräte-Verwaltung durchführt
* Es kann für jedes Gerät eine Warteschlange angelegt werden, in der zukünftige Reservierungsbedarfe eingetragen werden können. Es gilt first-come-first-serve
* Die Kosten für die Wartung der Geräte werden pro Quartal abgerechnet

## Erste Schritte

### Abhängigkeiten

#### Programmiersprache

&emsp;[![Python 3.12.0][Python]][Python-url] 

#### Wichtigste Bibliotheken

&emsp;n/a

*(für genauere Informationen siehe* [requirements.txt](requirements.txt) *)*

#### Betriebssysteme

&emsp;[![Windows 10][Windows_10]][Windows_10-url]
&emsp;[![Windows 11][Windows_11]][Windows_11-url]

#### Programmierumgebung

&emsp;[![Visual Studio Code][VS_Code]][VS_Code-url]

### Initialisierung

Da es sich bei diesem Programm nur um ein Mockup handelt, die Entsprechende Programmierumgebung erst herunterlgeladen werden.
* Herunterladen und Instalieren von [Python 3.12.0](https://www.python.org/downloads/windows/)
* Herunterladen und Instalieren von [Visual Studio Code](https://code.visualstudio.com)
* Herunterladen der aktuellen Version des Projekts von [GitHub](https://github.com/STTOMCI/UI_Geraeteverwaltung)


### Programm Ausführen

Da es sich bei diesem Programm nur um ein Mockup handelt, muss der Sourcecode noch Compiled werden.
* Einrichten einer Virtuellen Pythen-Umgebung in VS Code mit  
```python -m venv .venv```
* Aktivieren der Virtuellen Pythen-Umgebung mit  
```.venv\Scripts\activate```
* Instalieren aller benötigten Biblioteken mit  
```pip install -r requirements.txt```
* Compelieren und ausführen des Sourc-Codes mit Visual Studio Code

### Programm Schließen

* Nach dem Ausführen kann die virtuelle Pythen-Umgebung beendet werden mit    
```deactivate ```

## Authors

Contributors names and contact info

* Tobias Stummer    
&emsp;Email: <t.stummer@mci4me.at>

## Version History

* 0.1
    * Setup
    * See [commit change]() or See [release history]()

## License

This project is licensed under the Educational Community License, Version 2.0 - see the [LICENSE.md](LICENSE.md) file for details

[![Educational Community License, Version 2.0][ECL_V2]][ECL_V2-url]

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/python_3.12.0-FFD43B?style=for-the-badge&logo=python&logoColor=306998
[Python-url]: https://www.python.org
[Windows_10]: https://img.shields.io/badge/Windows%2010-357EC7?style=for-the-badge&logo=windows10
[Windows_10-url]: https://www.microsoft.com/de-de/software-download/windows10%20
[Windows_11]: https://img.shields.io/badge/Windows%2011-357EC7?style=for-the-badge&logo=windows11
[Windows_11-url]: https://www.microsoft.com/de-de/software-download/windows11
[VS_Code]: https://img.shields.io/badge/Visual%20Studio%20Code-444444?style=for-the-badge&logo=visualstudiocode&logoColor=007ACC
[VS_Code-url]: https://code.visualstudio.com
[ECL_V2]: https://img.shields.io/badge/Educational%20Community%20License,%20Version%202.0-414042?style=for-the-badge&logo=opensourceinitiative&logoColor=3DA639
[ECL_V2-url]: https://opensource.org/license/ecl-2-0/
