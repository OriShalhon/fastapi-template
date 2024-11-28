FROM python:3.12

# Set the working directory
WORKDIR /usr/src/app

# for docker optimization purposs - install dependencies first, 
# if the file has not changed, the cache will be used skipping the installation
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Run the application - can use either uvicorn or explicitly run the main.py file as it calls uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]