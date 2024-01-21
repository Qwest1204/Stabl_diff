FROM pytorch/pytorch:latest
COPY . /workspace

RUN pip install flask
RUN pip install datetime
RUN pip install diffusers transformers accelerate --upgrade

CMD python server.py