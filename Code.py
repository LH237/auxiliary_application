from rich.progress import track
from rich.console import Console
import subprocess
import time
import os

console = Console()

class functions:
	def create_project():
		console.print("[light_green]Bitte erstellen sie einen Projektordner auf dem Desktop und geben sie dessen Namen an:[/light_green]")
		folder_name = input(">")
		folder_dir = "C:/Users/satte/OneDrive/Desktop/"
		if folder_name == "":
			console.print("[light_red]Bitte geben sie einen Namen ein![/light_red]")
			time.sleep(1.5)
			subprocess.call("cls", shell=True)
			functions.create_project()
		else:
			for i in track(range(1), "checking for folder..."):
				time.sleep(1.5)
			subprocess.call("cls", shell=True)
			if os.path.exists(folder_dir+folder_name+"/"):
				console.print("[light_green]Bitte geben sie den Namen des Projekts ein:[/light_green]")
				file_name = input(">")
				subprocess.call("cls", shell=True)
				if file_name == "":
					console.print("[light_red]Bitte geben sie einen Projektnamen an![light_red]")
					time.sleep(1.5)
					subprocess.call("cls", shell=True)
					functions.create_project()
				else:
					console.print("[light_green]Bitte geben sie die Programmiersprache an:[/light_green]")
					coding_ln = input(">")
					if coding_ln == "python" or "Python":
						for i in track(range(12), "creating project..."):
							time.sleep(0.1)
						file_one = open(folder_dir+folder_name+"/"+file_name+".py", 'w')
						file_one.close()
						subprocess.call("cls", shell=True)
						start()
					elif coding_ln == "java" or "Java":
						for i in track(range(12), "creating project..."):
							time.sleep(0.1)
						file_two = open(folder_dir+folder_name+"/"+file_name+".jar", 'w')
						file_two.close()
						subprocess.call("cls", shell=True)
						start()
					elif coding_ln == "c#" or "C#":
						for i in track(range(12), "creating project..."):
							time.sleep(0.1) 
						file_three = open(folder_dir+folder_name+"/"+file_name+".cs", 'w')
						file_three.close()
						subprocess.call("cls", shell=True)
						start()
					else:
						console.print("[light_red]Bitte geben sie eine Unterstützte Programmiersprache an! (Python, Java, C#) [/light_red]")
						time.sleep(1.25)
						subprocess.call("cls", shell=True)
						functions.create_project()
			else:
				console.print("[light_red]Dieser Ordner ist nicht auf dem Desktop vorhanden![/light_red]")
				time.sleep(1.5)
				subprocess.call("cls", shell=True)
				functions.create_project()


	def create_basic_project(ex):
		if ex == "y":
			console.print("[light_green]Bitte geben sie den namen des Projekts an:[/light_green]")
			ex_file_name = input(">")
			subprocess.call("cls", shell=True)
			if ex_file_name == "":
				console.print("[light_red]Bitte geben sie einen Projektnamen an![/light_red]")
			else:
				console.print("[light_green]Wie möchten sie die main-funktion nennen?[/light_green]")
				main_inp = input(">")
				for i in track(range(2), "[light_green]gathering input...[/light_green]"):
					time.sleep(1)
		elif ex == "n":
			start()
		else:
			console.print("[light_red]ERROR, something went wrong! restarting...")
			time.sleep(1)
			subprocess.call("cls", shell=True)
			functions.create_basic_project()


def start():
	console.print("[light_green]Bitte geben sie einen Befehl ein:[/light_green]")
	command = input(">")
	if command == "projekt erstellen":
		functions.create_project()
		subprocess.call()
	elif command == "basis projekt erstellen":
		console.print("[light_green]Möchten sie ein Projekt erstellen oder ein bestehendes Projekt mit dem Basis-Code überschreiben?[/light_green]")
		existing = input("Erstellen/Überschreiben>")
		if existing == "erstellen" or "Erstellen":
			functions.create_basic_project("n")
		elif existing == "überschreiben" or "Überschreiben":
			functions.create_basic_project("y")
	else:
		console.print(f"[light_red]der Befehl {command} ist nicht gültig, bitte überprüfen sie die Rechtschreibung! Mit 'help' erhalten sie eine vollständige Liste der Befehle.[/light_red]")
		time.sleep(1.75)
		subprocess.call("cls", shell=True)
		start()

subprocess.call("@echo off", shell=True)
subprocess.call("cls", shell=True)
start()
