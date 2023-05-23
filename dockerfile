FROM python

WORKDIR /app

COPY requirements.txt /app/

RUN pip install requirements.txt

COPY . . /app/

CMD [ "streamlit run inventory.py" ]
