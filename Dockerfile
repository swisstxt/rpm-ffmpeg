FROM almalinux:9

ARG username=builduser
ARG userid
ARG groupname=${username}
ARG groupid=${userid}
ARG package
ARG dependencies=

RUN dnf -y update
RUN dnf -y install epel-release dnf-plugins-core
RUN dnf config-manager --set-enabled crb
RUN dnf -y install make rpm-build ${dependencies}

RUN groupadd -g ${groupid} ${groupname}
RUN useradd -d /home/${username} -m -u ${userid} -g ${groupid} ${username}

USER ${username}
CMD cd /home/${username}/${package} && make
