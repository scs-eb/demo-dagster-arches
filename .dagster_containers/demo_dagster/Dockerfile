FROM python:3.13-slim as prod

## Build Args
ARG PROJ_NAME=demo_dagster
ARG PROJ_REPO_NAME=demo-dagster

## Setting default environment variables
ENV DAGSTER_PROJECT=$PROJ_NAME
ENV APP_ROOT=/app

# Copy the project source from the build context (workspace root)
COPY ${PROJ_REPO_NAME}/${DAGSTER_PROJECT}/ ${APP_ROOT}/${DAGSTER_PROJECT}/

# Install from APP_ROOT to allow debug and development of Dagster.
WORKDIR ${APP_ROOT}/${DAGSTER_PROJECT}

RUN pip install -e '.[dev]'

# Set $DAGSTER_HOME and copy dagster.yaml and workspace.yaml there
ENV DAGSTER_HOME=/opt/dagster/dagster_home/

RUN mkdir -p $DAGSTER_HOME

COPY ${PROJ_REPO_NAME}/dagster.yaml ${PROJ_REPO_NAME}/workspace.yaml $DAGSTER_HOME

FROM prod AS dev

RUN pip install debugpy

# Remote debugging port
EXPOSE 5679

ENTRYPOINT ["python", "-m", "debugpy", "--listen", "0.0.0.0:5679", "-m"]
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000", "-w", "/opt/dagster/dagster_home/workspace.yaml"]