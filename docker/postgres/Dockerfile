FROM postgres:17

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    postgresql-server-dev-17

RUN git clone https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install

RUN echo "CREATE EXTENSION IF NOT EXISTS vector;" > /docker-entrypoint-initdb.d/init.sql 