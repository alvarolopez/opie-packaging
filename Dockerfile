FROM centos:7

RUN useradd -m -u 1000 builder

RUN yum install -y epel-release \ 
                   rpm-build \
                   git \
                   python-setuptools \
                   epel-rpm-macros 
RUN yum install -y python-sphinx
RUN yum install -y python-pbr

COPY rpmbuild.sh /home/builder/
RUN  chmod 755 /home/builder/rpmbuild.sh

RUN mkdir -p /home/builder/rpmbuild/RPMS \
             /home/builder/rpmbuild/SOURCES \
             /home/builder/rpmbuild/SPECS \
             /home/builder/rpmbuild/SRPMS \
             /home/builder/rpmbuild/BUILD \
             /home/builder/rpmbuild/BUILDROOT
RUN chown -R builder:builder /home/builder/rpmbuild/ 
VOLUME ["/home/builder/rpmbuild/RPMS"]
VOLUME ["/home/builder/rpmbuild/SPECS"]

USER builder

ENV HOME /home/builder
CMD ["/home/builder/rpmbuild.sh"]
