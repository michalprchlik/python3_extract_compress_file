FROM python:3.8.12-slim

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash  appuser
USER appuser
WORKDIR /home/appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV TEST_IN_CONTAINER=True

COPY --chown=appuser:appuser . .

CMD ["-m", "unittest"]
ENTRYPOINT ["python3"] 