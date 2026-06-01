---
title: "OpenProject 12.2.0 released with Nextcloud integration"
date: "2022-09-02 01:27:12"
lastmod: "2022-09-02 01:27:48"
slug: "openproject-released-with-nextcloud-integration"
draft: false
author: "Moult"
description: "OpenProject now integrates with Nextcloud to allow documentation, schedules, and specifications to be linked to work packages."
tags: ["OpenProject", "Construction"]
wordpress_id: 2907
wordpress_guid: "https://osarch.org/?p=2907"
cover:
  image: "/uploads/2022/09/openproject-released-with-nextcloud-integration-4.png"
  alt: "OpenProject 12.2.0 released with Nextcloud integration"
  hiddenInSingle: false
  hiddenInList: false
---
OpenProject 12.2.0 has just been released, with the biggest feature being a new integration with Nextcloud. OpenProject is an open source GPLv3 licensed web-based project management platform, with over 2 million downloads and 190 contributors. OpenProject has a BIM module, which allows basic navigation of OpenBIM models, and is one of the few open source options to use as a Common Data Environment (CDE) for AEC professionals.

!

Prior to this release, OpenProject focused primarily on issue management. Although there was an OpenBIM viewer (based on the open source Xeokit project), there was no way to see a central filesystem of project documents, such as drawings, schedules, and specifications. This major omission did not make it feasible for larger companies to adopt OpenProject as a model platform, and it had to be used together with other filesharing software.

This release combines the issue management capabilities of OpenProject with the filesharing capabilities of the well-established open source Nextcloud project. Nextcloud is a mature, enterprise-ready project that offers an alternative to the proprietary Microsoft cloud offerings. When combined with OpenProject, this allows you to store project documents, along with all the features of Nextcloud Files, such as filesharing access controls, integration with FTP, Windows Network Drives, SharePoint, NFS, web, desktop, and mobile apps, locked files, and GDPR compliance.

Documents on Nextcloud Files may be linked to issues on OpenProject, and vice versa. Clicking a document will show all relevant issues. Permissions are linked between OpenProject and Nextcloud, so a user who does not have the permission to access the file in Nextcloud will also not be able to open, download, modify or unlink the file in OpenProject.

!

Issue related notifications (such as issue status changes) will also then be available as a widget in your Nextcloud dashboard.

!

Note that Nextcloud does not yet have features tailored to the AEC industry, such as document revisioning, and custom metadata fields. However, this integration is still a huge step forward for firms concerned about data sovereignty.

Other features include improvements to the date picker, the ability to log time for other users for administrators, and numerous bug fixes and improvements.

- [Visit the OpenProject homepage](https://www.openproject.org/)
- [Help develop OpenProject on Github](https://github.com/opf/openproject)
- [Read the official release notes](https://www.openproject.org/docs/release-notes/12-2-0/)
- [Read the documentation on Nextcloud integration](https://www.openproject.org/docs/user-guide/nextcloud-integration/)
- [Learn more about Nextcloud](https://nextcloud.com/)
