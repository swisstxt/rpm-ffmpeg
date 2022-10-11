FROM centos:7

ARG package
ARG dependencies=

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install make rpm-build ${dependencies}

RUN mkdir -p /build/${package}
WORKDIR /build/${package}
CMD make
