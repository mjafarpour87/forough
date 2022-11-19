# Changelog
All notable changes to this project will be documented in this file.

## v0.0.2-dev - Unreleased - 2022-11-02

### Improvements
- Add CHANGELOG
- Improve OrganizationUnit Model
- Change path of static file
- Add user profile page
- Add getallperm command


### Bug Fixes
- Fix permission_required in view generator
- Fix package Setup 
- Fix Error Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'django_cuser.CustomUser.groups'.
- Fix path of locale directory
- Fix model_verbose_name bug in lowcode

## v0.0.1 - 2022-08-26

### Improvements


### Bug Fixes





# Semantic Versioning 2.0.0
Given a version number MAJOR.MINOR.PATCH, increment the[:](https://semver.org/)

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backwards compatible manner
3. PATCH version when you make backwards compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

SemVer uses a sequence of three digits, MAJOR.MINOR.PATCH, and also allows for an optional pre-release tag and build metadata tag. Altogether, a version looks like:
```
MAJOR.MINOR.PATCH-[pre-release-tag]+[build-meta-tag]
```

The MAJOR, MINOR, and PATCH digits are sorted numerically (1.1.11 > 1.1.10), the pre-release tag is sorted alphanumerically (rc > beta > alpha), and the build-meta-tag is ignored completely when determining sort order or equality (1.1.1+abcd == 1.1.1+efgh)[.](https://interrupt.memfault.com/blog/release-versioning)

The most common pre-release tags are ‘alpha’, ‘beta’, and ‘rc’, which should satisfy most of your versioning requirements.

- Use ‘alpha’ when the release branch is first cut from master or another release branch. It’s pretty much assumed that ‘alpha’ builds are unstable and should be treated as broken-by-default.
- Use ‘beta’ when the API is stable, there are no longer any breaking changes and features being pushed into the release, and the stabilization phase has begun.
- Use ‘rc’ (release-candidate) when you think everything is stable and QA should start doing rigorous testing because it might turn out that this build could be “the one”.


In all of my scripts that parse SemVer and when I need to quickly test version comparisons, I turn to the python-semver package.
```
$ pip install semver
$ python
>>> semver.parse_version_info('1.1.1-alpha.1') \
    < semver.parse_version_info('1.1.1-alpha.11')
True
```