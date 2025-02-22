FROM hemanhp/djbase:5.0


COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR src

EXPOSE 8000

USER root

RUN /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --upgrade pip setuptools && \
    /py/bin/pip install -r /requirements/base.txt && \
    chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home jwt && \
    chown -R jwt:jwt /vol && \
    chmod -R 755 /vol


ENV PATH="/scripts:/py/bin:$PATH"

USER jwt

CMD ["run.sh"]