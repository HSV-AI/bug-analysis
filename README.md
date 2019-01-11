# Bug Analysis

The purpose of this project is to attempt to find a way to recommend similar bugs when assigning a bug or creating a new bug.
At the time of this writing, the Eclipse Foundation [Bugzilla Database](https://bugs.eclipse.org/bugs/) contains 543131 bugs. Below is an excerpt from the [Eclipse Foundation 2018 annual report](https://www.eclipse.org/org/foundation/reports/annual_report.php):

> ## Photon Simultaneous Release

> In June 2017 the Eclipse community shipped Eclipse Oxygen, its twelfth annual simultaneous release. Including previous releases of the Eclipse Platform, this was the fourteenth release that was shipped on time, to the day. A total of 83 projects participated in the Oxygen simultaneous release. The release comprises 71 million lines of code produced by 283 committers from 46 member companies, with contributions from 417 non-committer contributors.

> ![Image of Release Metrics](https://www.eclipse.org/images/reports/2018_simultaneous-release-metrics.png "Release Metrics")

> ## Committer and Project Community

> Our number of committers grew past 1,500 in early 2018.

> ![Image of Committer Numbers](https://www.eclipse.org/images/reports/2018_community.png "Community Metrics")

# Problem

With the amount of source code being maintained by such a small community, we need a better way to identify overlaps where the same work may apply to multiple places. The simple goal of this project is to reccomend additional bugs could be addressed when working to correct another.
