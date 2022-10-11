HOME=$(shell pwd)
PACKAGE=ffmpeg
DEPENDENCIES=redhat-rpm-config epel-rpm-macros alsa-lib-devel bzip2-devel fontconfig-devel freetype-devel fribidi-devel gnutls-devel gsm-devel lame-devel jack-audio-connection-kit-devel ladspa-devel libass-devel libbluray-devel libcdio-paranoia-devel libdrm-devel libgcrypt-devel libGL-devel libmodplug-devel librsvg2-devel libssh-devel libtheora-devel libv4l-devel libva-devel libvdpau-devel libvorbis-devel nasm nv-codec-headers libxcb-devel openal-soft-devel opencl-headers ocl-icd-devel openjpeg2-devel pulseaudio-libs-devel SDL2-devel soxr-devel speex-devel texinfo vid.stab-devel zimg-devel zlib-devel zvbi-devel libxml2-devel \
AMF-devel ilbc-devel libaom-devel libbs2b-devel libchromaprint-devel libdav1d-devel libmysofa-devel libopenmpt-devel libsmbclient-devel rubberband-devel snappy-devel tesseract-devel twolame-devel wavpack-devel
DISTRIBUTION=.el7.swisstxt
VERSION=$(shell awk '/^Version:/{print $$2}' < SPECS/${PACKAGE}.spec)
COMMIT=$(shell git rev-parse HEAD)

all: build

clean:
	rm -rf ./rpmbuild
	mkdir -p ./rpmbuild/SPECS/ ./rpmbuild/SOURCES/

download-upstream:
	wget https://ffmpeg.org/releases/${PACKAGE}-${VERSION}.tar.xz -P ./SOURCES/ -q

build: clean
	cp -r ./SPECS/* ./rpmbuild/SPECS/
	cp -r ./SOURCES/* ./rpmbuild/SOURCES/
	rpmbuild -ba SPECS/${PACKAGE}.spec \
	--define "commit ${COMMIT}" \
	--define "dist ${DISTRIBUTION}" \
	--define "_topdir %(pwd)/rpmbuild" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define "_without_amr 1" \
	--define "_without_x264 1" \
	--define "_without_x265 1" \
	--define "_without_xvid 1" \
	--define "_without_rtmp 1" \
	--define "_without_vpx 1" \
	--define "_without_opus 1" \
	--define "_without_srt 1" \
	--define "flavor -nofusion" \
	--define "progs_suffix -nofusion" \
	--define "build_suffix -nofusion"

docker-build:
	podman build -t ${PACKAGE} $(shell pwd) --build-arg package=${PACKAGE} --build-arg dependencies="${DEPENDENCIES}"
	podman run -t --rm -v $(shell pwd):/build/${PACKAGE} ${PACKAGE} make DISTRIBUTION=${DISTRIBUTION} COMMIT=${COMMIT} build
	sha256sum rpmbuild/*.rpm rpmbuild/*/*.rpm
