#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R2jags
Version  : 0.7.1
Release  : 28
URL      : https://cran.r-project.org/src/contrib/R2jags_0.7-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R2jags_0.7-1.tar.gz
Summary  : Using R to Run 'JAGS'
Group    : Development/Tools
License  : GPL-3.0+
Requires: R-R2WinBUGS
Requires: R-abind
Requires: R-coda
Requires: R-rjags
BuildRequires : R-R2WinBUGS
BuildRequires : R-abind
BuildRequires : R-coda
BuildRequires : R-rjags
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n R2jags
cd %{_builddir}/R2jags

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641085039

%install
export SOURCE_DATE_EPOCH=1641085039
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2jags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2jags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2jags
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc R2jags || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R2jags/DESCRIPTION
/usr/lib64/R/library/R2jags/INDEX
/usr/lib64/R/library/R2jags/Meta/Rd.rds
/usr/lib64/R/library/R2jags/Meta/features.rds
/usr/lib64/R/library/R2jags/Meta/hsearch.rds
/usr/lib64/R/library/R2jags/Meta/links.rds
/usr/lib64/R/library/R2jags/Meta/nsInfo.rds
/usr/lib64/R/library/R2jags/Meta/package.rds
/usr/lib64/R/library/R2jags/NAMESPACE
/usr/lib64/R/library/R2jags/R/R2jags
/usr/lib64/R/library/R2jags/R/R2jags.rdb
/usr/lib64/R/library/R2jags/R/R2jags.rdx
/usr/lib64/R/library/R2jags/help/AnIndex
/usr/lib64/R/library/R2jags/help/R2jags.rdb
/usr/lib64/R/library/R2jags/help/R2jags.rdx
/usr/lib64/R/library/R2jags/help/aliases.rds
/usr/lib64/R/library/R2jags/help/paths.rds
/usr/lib64/R/library/R2jags/html/00Index.html
/usr/lib64/R/library/R2jags/html/R.css
/usr/lib64/R/library/R2jags/model/schools.txt
/usr/lib64/R/library/R2jags/tests/testthat.R
/usr/lib64/R/library/R2jags/tests/testthat/test-jags.R
/usr/lib64/R/library/R2jags/tests/testthat/test-jags.parallel.R
