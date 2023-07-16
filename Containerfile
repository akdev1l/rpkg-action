FROM fedora:latest

RUN dnf install -y rpkg 'dnf-command(builddep)'

COPY entrypoint /app/entrypoint

ENTRYPOINT ["/app/entrypoint"]
