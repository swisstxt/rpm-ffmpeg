FROM almalinux:9

ARG package
ARG dependencies=

RUN dnf -y update
RUN dnf -y install epel-release dnf-plugins-core
RUN dnf config-manager --set-enabled crb
RUN dnf -y install make rpm-build ${dependencies}

RUN mkdir -p /build/${package}
WORKDIR /build/${package}
CMD make
