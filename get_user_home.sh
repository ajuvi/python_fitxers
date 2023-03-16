#!/bin/bash

read -p "Entra el nom: " nom

if ! grep ^$nom: /etc/passwd > /dev/null;then
  >&2 echo "No existeix l'usuari ${nom}"
  exit 1
fi

home=$(cat /etc/passwd | grep ^$nom: | cut -d: -f6)
echo "La carpeta home de $nom és $home"
