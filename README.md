# Custom FFmpeg RPM build

This repository contains a custom RPM build that doesn't require RPMFusion packages.

It also contains bug fixes that are not available upstream.

## Bug fixes

* A patch for [#8522](https://trac.ffmpeg.org/ticket/8522) - fixes MPEG-DASH segment number calculation for certain edge cases

## Legal

This project is Copyright © 2015-2022 SWISS TXT AG. All rights reserved.

The custom build scripts (Makefiles, spec files, build automation, etc.) are released under the MIT license.
See the [LICENSE](LICENSE) file for details.

The full FFmpeg source code is licensed under the GNU General Public License (GPL) version 2 or later.
See [ffmpeg.org/legal.html](https://ffmpeg.org/legal.html) for more information.

The RPM spec file is based on [RPMFusion/ffmpeg](https://github.com/rpmfusion/ffmpeg).
Licensed under the "Current Default License", which is the MIT license, as specified in the
[RPM Fusion Wiki](https://rpmfusion.org/wiki/Legal:RPM%20Fusion_Project_Contributor_Agreement).