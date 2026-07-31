## Building the libchewing library for Sailfish OS.

Since version 0.9, libchewing has been reimplemented in Rust, but Rust support for libchewing is not yet satisfied on Sailfish OS.
Consequently, the package will remain at version 0.8.5 until Rust support is ready for newer versions.

## How to build by yourself

### Pre-requisites

Install the [Sailfish SDK](https://docs.sailfishos.org/Tools/Sailfish_SDK/) on your system.

### Clone and Patch

```bash
git clone --recurse-submodules https://github.com/hanhsuan/SailfishOS-libchewing.git

cd SailfishOS-libchewing

cp -r rpm libchewing

patch libchewing/doc/CMakeLists.txt libchewing/rpm/0001-skip-chewing-cli-doc.patch
```

### Build

for static library

```bash
cd libchewing

# Build static library only
sfdk build
```

for shared library

```bash
cd libchewing

# Build shared library only
sfdk build -- --with dynamic
```

## **TOOD** Github action
There are some issues to use the [action](https://github.com/CODeRUS/github-sfos-build) made by [CODeRUS](https://github.com/CODeRUS) for this project.
