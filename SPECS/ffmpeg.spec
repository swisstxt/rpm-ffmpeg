%global service_name %{name}

Name:           %{name}
Version:        2.5.2
Release:        %{rel}%{?dist}
Summary:        Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder for RHEL/CENTOS %{os_rel}
BuildArch:      %{arch}
Group:          System Environment/Libraries
License:        commercial
URL:            http://ffmpeg.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source:         http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2

%description
Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder for RHEL/CENTOS %{os_rel}

%prep
%setup -q
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build

%install

%clean

%files

%changelog
