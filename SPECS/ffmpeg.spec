%global service_name %{name}

Name:           %{name}
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder for RHEL/CENTOS %{os_rel}
BuildArch:      %{arch}
Group:          System Environment/Libraries
License:        commercial
URL:            http://ffmpeg.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  opus-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel >= 1.3.0
BuildRequires:  yasm
BuildRequires:  lame-devel
BuildRequires:  fdk-aac-devel
BuildRequires:  x264-devel
Requires:      %{name}-libs = %{version}-%{release}

Source:         http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2

%package libs
Summary:        Library for ffmpeg
Group:          System Environment/Libraries

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

%description devel
FFmpeg is a complete and free Internet live audio and video broadcasting
solution for Linux/Unix. It also includes a digital VCR. It can encode in real
time in many formats including MPEG1 audio and video, MPEG4, h263, ac3, asf,
avi, real, mjpeg, and flash.
This package contains development files for ffmpeg

%description libs
FFmpeg is a complete and free Internet live audio and video broadcasting
solution for Linux/Unix. It also includes a digital VCR. It can encode in real
time in many formats including MPEG1 audio and video, MPEG4, h263, ac3, asf,
avi, real, mjpeg, and flash.
This package contains the libraries for ffmpeg

%prep
%setup -q
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
LDFLAGS=-lstdc++ ./configure --prefix=%{_prefix} --libdir=%{_libdir} \
            --shlibdir=%{_libdir} --mandir=%{_mandir} \
    --enable-shared \
    --disable-static \
    --enable-runtime-cpudetect \
	--enable-gpl \
	--enable-nonfree \
	--enable-libfdk_aac \
	--enable-libmp3lame \
	--enable-libopus \
	--enable-libvorbis \
	--enable-libvpx \
	--enable-libx264 \
%ifarch %ix86
   --extra-cflags="%{optflags}" \
%else
   --extra-cflags="%{optflags} -fPIC" \
%endif
   --disable-stripping
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} incdir=%{buildroot}%{_includedir}/ffmpeg
# Remove from the included docs
rm -f doc/Makefile
rm -f %{buildroot}/usr/share/doc/ffmpeg/*.html

%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_bindir}/*
%{_datadir}/ffmpeg
%{_mandir}/man1/*

%files libs
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_libdir}/*.so.*
%{_mandir}/man3/*

%files devel
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%changelog
* Fri Jan 16 2015 Daniel Menet <daniel.menet@swisstxt.ch> -%{version}-%{release}
- Initial release based on https://github.com/lkiesow/matterhorn-rpms/blob/master/specs/ffmpeg.spec