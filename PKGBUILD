# Maintainer: Your Name <youremail@domain.com>
pkgname=python-pbfetch-git
pkgver=r4.21b383c
pkgrel=1
pkgdesc="An unbelievably customizable hardware/software fetch"
arch=('x86_64' 'aarch64')
url="https://github.com/pennybelle/pbfetch"
license=('Apache-2.0')
depends=("python-psutil")
makedepends=(python-build python-installer python-wheel git)
provides=("${pkgname}")
conflicts=("${pkgname}")
source=("git+https://github.com/pennybelle/pbfetch.git")
sha256sums=('SKIP')
# dist=("${pkgname}")
# groups=()omg

pkgver() {
    # cd "$srcdir/.."
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    # cd "$srcdir/.."
    build --wheel --no-isolation
    # rye publish
    # build --wheel --no-isolation
}

package() {
    # cd "$srcdir/.."
    installer --destdir="$srcdir" dist/*.whl
}
