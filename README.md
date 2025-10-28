AGAthon Frankfurt 2025

Team Members
	•	Mark Merkouchev
	•	Mohamed Eltantawy
	•	Leon Demare

Overview

Welcome to our official repository for AGAthon Frankfurt 2025! This repository contains all code, documentation, and resources related to our project submission for this year’s hackathon. We are excited to participate and showcase our work as a team.

Project Description

Patienten Aufenthaltsvorhersage

Die Belegung von Betten sowie die präzise Einschätzung ihrer Wiederverfügbarkeit erfordern ein hohes Maß an Erfahrung – eine Kompetenz, die erfahrenem Pflegepersonal oder ärztlichem Fachpersonal zu zuordnen ist. Aktuell basieren Prognosen zu Entlasszeitpunkten häufig auf Erfahrungswerten, was nicht selten zu Engpässen, Verlegungen, Verzögerungen und führt. Die Challenge besteht darin, auf Basis weniger bei der Aufnahme verfügbarer Merkmale – wie Alter, Fachabteilung oder Hauptdiagnose – eine patientenindividuelle Verweildauer zuverlässig vorherzusagen. Zu diesem Zweck stellen wir echte, anonymisierte Routinedaten bereit, um Kapazitäten frühzeitig sichtbar zu machen, Entlassmanagement gezielt zu automatisieren und zukünftige Kapazitäten vorhersagen zu können. 

English verson

The occupation of beds and the precise estimation of their re-availability require a high degree of experience – a competence that is typically attributed to experienced nursing or medical specialists. Currently, prognoses regarding discharge times are often based on empirical values, which not infrequently leads to bottlenecks, transfers, and delays. The challenge is to reliably predict a patient-specific length of stay based on a few characteristics available at admission – such as age, specialist department, or primary diagnosis. To this end, we provide real, anonymized routine data to make capacities visible early on, specifically automate discharge management, and predict future capacities.

Inspo

https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii/data

Steps
	- Try to run and understand whats done in the two examples
	- Try to improve the examples and compare the scores
	- Create a web framework for UI where the params could be submitted
	- Cleanup the GitHub and legal data formalization
	- Create a presentation and description of results

Tech Stack
	•	Frontend: Add your technologies
	•	Backend: Jupyter Notebook
	•	Database: Add your technologies
	•	Other Tools/Services: Add your tools

Repository Structure

## 🛠️ Setup & Installation

Follow these steps to set up the project environment on your local machine. We recommend using Conda and the provided `environment.yml` file for the most reliable setup.

### Option 1: Using Conda (Recommended)

This method uses the `environment.yml` file to recreate the exact development environment, including specific package versions and non-Python dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MarkMerk/AGAthon.git](https://github.com/MarkMerk/AGAthon.git)
    cd AGAthon
    ```
2.  **Ensure you have Conda installed.** If not, we recommend installing [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).
3.  **Create the Conda environment** from the `environment.yml` file. This command reads the file and installs all specified dependencies:
    ```bash
    conda env create -f environment.yml
    ```
    *(This might take a few minutes as it downloads and installs all packages)*
4.  **Activate the environment:**
    ```bash
    conda activate agathon
    ```
    Your terminal prompt should now show `(agathon)` at the beginning.

### Option 2: Using pip (Alternative)

This method uses the `requirements.txt` file with `pip`. Note that this might not capture non-Python dependencies and relies on `pip`'s dependency resolution, which could lead to minor differences from the original Conda environment.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MarkMerk/AGAthon.git](https://github.com/MarkMerk/AGAthon.git)
    cd AGAthon
    ```
2.  **Ensure you have Python installed** (version 3.10 or higher recommended).
	Check the default python command (might be Python 2 or 3 depending on your system)
	```bash
	python --version
	```

	Check the specific Python 3 version (recommended)
	```bash
	python3 --version
	```
3.  **Install dependencies** using `pip` and the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

Goals & Milestones
	•	Define problem statement
	•	Design architecture & workflow
	•	Implement core features
	•	Test & refine
	•	Final presentation prep

Contribution Guidelines
	•	Use feature branches when working on tasks
	•	Commit with clear messages
	•	Open Pull Requests for review before merging

License

Specify your project license here

Acknowledgements

A big thank you to the organizers of AGAthon Frankfurt 2025 and everyone supporting hackathon innovation and collaboration!