#!/bin/bash

# Construir la imagen Docker
docker compose build

# Iniciar los contenedores
docker compose up -d
