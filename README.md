# Custom FFmpeg RPM build

This repository contains a custom RPM build that doesn't require RPMFusion packages.

It also contains bug fixes that are not available upstream.

## Bug fixes

* A patch for [#8522](https://trac.ffmpeg.org/ticket/8522) - fixes MPEG-DASH segment number calculation for certain edge cases

## Releases

Releases are built by a GitHub action that triggers on tag creation.

Important: Make sure to update the VERSION variable in the Makefile to the FFmpeg release you
want to build, and the RELEASE variable to a patch level. When you update the FFmpeg version,
you can start with RELEASE 1. If you only make modifications to the build script, dependencies
or patches, increment the RELEASE. Do not forget this, or the built package won't have a
newer version than the previous one.

Each commit or pull request starts a test build that can be used to verify the resulting package.
The build artifacts can be found under the Actions job corresponding to the commit. 

Once you are satisfied, create a tag for the full package version (this should be `${VERSION}-${RELEASE}`),
and another workflow will automatically launch a release build and create a GitHub release with the built packages.

## Legal

This project is Copyright © 2015-2022 SWISS TXT AG. All rights reserved.

The custom build scripts (Makefiles, spec files, build automation, etc.) are released under the MIT license.
See the [LICENSE](LICENSE) file for details.

The full FFmpeg source code is licensed under the GNU General Public License (GPL) version 2 or later.
See [ffmpeg.org/legal.html](https://ffmpeg.org/legal.html) for more information.

The RPM spec file is based on [RPMFusion/ffmpeg](https://github.com/rpmfusion/ffmpeg).
Licensed under the "Current Default License", which is the MIT license, as specified in the
[RPM Fusion Wiki](https://rpmfusion.org/wiki/Legal:RPM%20Fusion_Project_Contributor_Agreement).
