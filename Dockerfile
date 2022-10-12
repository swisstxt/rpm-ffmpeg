FROM centos:7

ARG username=builduser
ARG userid
ARG groupname=${username}
ARG groupid=${userid}
ARG package
ARG dependencies=

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install make rpm-build ${dependencies}

RUN groupadd -g ${groupid} ${groupname}
RUN useradd -d /home/${username} -m -u ${userid} -g ${groupid} ${username}

USER ${username}
CMD cd /home/${username}/${package} && make
