# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu bot al contenedor
COPY . /app

# Instala las dependencias del bot
RUN pip install --no-cache-dir -r requirements.txt

# Configura las variables de entorno
ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV TOKEN=your_bot_token
ENV OWNER_ID=your_owner_id
ENV SUDO_IDS=comma_separated_sudo_ids

# Comando para ejecutar el bot
CMD [ "python", "main.py" ]