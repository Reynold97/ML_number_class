FROM python:3.10

WORKDIR /ml_number_class

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]