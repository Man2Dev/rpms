%bcond_with    tests

%global         srcname     safetensors

Name:           python-%{srcname}
%global         pypi_version    0.5.2
Version:        v%{pypi_version}
Release:        %autorelease
Summary:        Simple, safe way to store and distribute tensors
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        %{pypi_source %{srcname} %{pypi_version}}
# LICENSE is not included in the source
# PR for fix https://github.com/huggingface/safetensors/pull/416
Source1: https://github.com/huggingface/%{srcname}/raw/%{version}/LICENSE

BuildArch:      noarch

Epoch:          1

BuildRequires:  python%{python3_pkgversion}-devel

BuildRequires:  python%{python3_pkgversion}dist(pip)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-rust)
BuildRequires:  python%{python3_pkgversion}dist(maturin)
BuildRequires:  python%{python3_pkgversion}dist(torch)
BuildRequires:  python%{python3_pkgversion}dist(torchaudio)
BuildRequires:  python%{python3_pkgversion}dist(torchtext)
BuildRequires:  python%{python3_pkgversion}dist(torchvision)
BuildRequires:  python%{python3_pkgversion}dist(numpy)
BuildRequires:  python%{python3_pkgversion}dist(absl-py)
BuildRequires:  python%{python3_pkgversion}dist(elasticsearch)
BuildRequires:  python%{python3_pkgversion}dist(fastprogress)
BuildRequires:  python%{python3_pkgversion}dist(h5py)
BuildRequires:  python%{python3_pkgversion}dist(matplotlib)
BuildRequires:  python%{python3_pkgversion}dist(nltk)
BuildRequires:  python%{python3_pkgversion}dist(packaging)
BuildRequires:  python%{python3_pkgversion}dist(pandas)
BuildRequires:  python%{python3_pkgversion}dist(pandas-datareader)
BuildRequires:  python%{python3_pkgversion}dist(pandas-flavor)
BuildRequires:  python%{python3_pkgversion}dist(psutil)
BuildRequires:  python%{python3_pkgversion}dist(pytest)
BuildRequires:  python%{python3_pkgversion}dist(pytest-benchmark)
BuildRequires:  python%{python3_pkgversion}dist(timeout-decorator)
BuildRequires:  python%{python3_pkgversion}dist(tqdm)
BuildRequires:  python%{python3_pkgversion}dist(huggingface-hub)
BuildRequires:  python%{python3_pkgversion}dist(hypothesis)
BuildRequires:  python%{python3_pkgversion}dist(flake8)
BuildRequires:  python%{python3_pkgversion}dist(isort)
BuildRequires:  python%{python3_pkgversion}dist(click)
BuildRequires:  python%{python3_pkgversion}dist(black)
# https://pypi.org/project/conllu/
# https://pypi.org/project/datasets/
# https://pypi.org/project/fairseq/
# https://pypi.org/project/faiss-cpu/
# https://pypi.org/project/fire/
# https://pypi.org/project/fugashi/
# https://github.com/pi2p/pil
# https://pypi.org/project/pytorch-lightning/
# https://pypi.org/project/rouge-score/
# https://pypi.org/project/sacrebleu/
# https://pypi.org/project/seqeval/
# https://pypi.org/project/sklearn/
# https://pypi.org/project/scikit-learn/
# https://pypi.org/project/streamlit/
# https://pypi.org/project/tensorboardX/
# https://pypi.org/project/tensorflow/
# https://pypi.org/project/tensorflow-datasets/
# https://pypi.org/project/torch-xla/
# https://pypi.org/project/paddlepaddle/
# https://pypi.org/project/jax/
# https://pypi.org/project/flax/
# https://pypi.org/project/jaxlib/
# https://pypi.org/project/mlx/

# bindings/python/Cargo.toml
# safetensors/Cargo.toml
# BuildRequires:  rust-pyo3_0.23*
# https://crates.io/crates/pyo3
BuildRequires:  rust-pythonize+default-devel
BuildRequires:  rust-pythonize-devel
BuildRequires:  rust-pyo3_0.22+default-devel
BuildRequires:  rust-pyo3+default-devel
BuildRequires:  rust-pyo3-macros-devel
BuildRequires:  rust-pyo3-macros0.22+default-devel
BuildRequires:  rust-pyo3-macros-backend0.22+default-devel
BuildRequires:  rust-pyo3-macros-backend-devel
BuildRequires:  rust-pyo3-macros-backend+default-devel
BuildRequires:  rust-pyo3-macros+multiple-pymethods-devel
BuildRequires:  rust-pyo3-macros+default-devel
BuildRequires:  rust-pyo3-log-devel
BuildRequires:  rust-pyo3-log+default-devel
BuildRequires:  rust-pyo3-devel
BuildRequires:  rust-pyo3-build-config-devel
BuildRequires:  rust-pyo3-build-config+resolve-config-devel
BuildRequires:  rust-pyo3-build-config+extension-module-devel
BuildRequires:  rust-pyo3-build-config+default-devel
BuildRequires:  rust-pyo3-build-config0.22+default-devel
BuildRequires:  rust-pyo3-build-config+abi3-py38-devel
BuildRequires:  rust-pyo3-build-config+abi3-devel
BuildRequires:  rust-pyo3+abi3-py38-devel
BuildRequires:  rust-pyo3_0.22-devel
BuildRequires:  rust-pyo3_0.22+abi3-devel
BuildRequires:  rust-pyo3_0.22+abi3-py38-devel
BuildRequires:  rust-pyo3_0.22+serde-devel
BuildRequires:  rust-pyo3_0.22+full-devel
BuildRequires:  rust-serde-devel
BuildRequires:  rust-serde+alloc-devel
BuildRequires:  rust-serde+default-devel
BuildRequires:  rust-serde+std-devel
BuildRequires:  rust-serde_default+default-devel
BuildRequires:  rust-serde_default-devel
BuildRequires:	rust-serde_json-devel
BuildRequires:	rust-serde_json+std-devel
BuildRequires:	rust-serde_json+alloc-devel
BuildRequires:  rust-serde_json+arbitrary_precision-devel
BuildRequires:  rust-serde_json+default-devel
BuildRequires:  rust-serde_json+float_roundtrip-devel
BuildRequires:  rust-serde_json+indexmap-devel
BuildRequires:  rust-serde_json+preserve_order-devel
BuildRequires:  rust-serde_json+raw_value-devel
BuildRequires:  rust-serde_json+unbounded_depth-devel
BuildRequires:  rust-maxminddb+memmap2-devel
BuildRequires:  rust-memmap2+default-devel
BuildRequires:  rust-memmap2+stable_deref_trait-devel
BuildRequires:  rust-memmap2-devel
# https://crates.io/crates/safetensors
BuildRequires:  rust-safetensors-devel
BuildRequires:  rust-safetensors+default-devel
BuildRequires:  rust-proptest-devel
BuildRequires:  rust-proptest+std-devel
BuildRequires:  rust-proptest+alloc-devel
BuildRequires:  rust-proptest+default-devel
BuildRequires:  rust-proptest-macro+default-devel
BuildRequires:  rust-proptest+proptest-macro-devel
BuildRequires:  rust-proptest-macro-devel
BuildRequires:  rust-proptest+attr-macro-devel
BuildRequires:  rust-hashbrown-devel
BuildRequires:  rust-hashbrown+allocator-api2-devel
BuildRequires:  rust-hashbrown+default-devel
BuildRequires:  rust-hashbrown+default-hasher-devel
BuildRequires:  rust-hashbrown+equivalent-devel
BuildRequires:  rust-hashbrown+inline-more-devel
BuildRequires:  rust-hashbrown+raw-entry-devel
BuildRequires:  rust-hashbrown+rayon-devel
BuildRequires:  rust-hashbrown+serde-devel
BuildRequires:  rust-pyo3_0.22+hashbrown-devel

BuildRequires:  git-core
BuildRequires:  pyproject-rpm-macros
BuildRequires:	cargo-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-cargo-devel
BuildRequires:  clippy
BuildRequires:  clippy-sarif
BuildRequires:  csmock-plugin-clippy
BuildRequires:  rustfmt
BuildRequires:  rust-bindgen+which-rustfmt-devel
BuildRequires:  rust-bindgen0.63+which-rustfmt-devel
BuildRequires:  rust-bindgen0.68+which-rustfmt-devel

%if %{with tests}
%endif

%global _description %{expand:
Simple, safe way to store and distribute tensors}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{pypi_version}
%cargo_prep
cp -p %{SOURCE1} %{buildroot}

%generate_buildrequires
# %%pyproject_buildrequires -r
%pyproject_buildrequires -x pip,setuptools,setuptools-rust,maturin,torch,torchaudio,torchtext,torchvision,numpy,absl-py,elasticsearch,fastprogress,h5py,matplotlib,nltk,packaging,pandas,pandas-datareader,pandas-flavor,psutil,pytest,pytest-benchmark,timeout-decorator,tqdm,huggingface-hub,hypothesis,flake8,isort,click,black
%cargo_generate_buildrequires -f rust-pyo3_0.22+abi3-py38-devel,rust-pyo3_0.22-devel,rust-pyo3_0.22+abi3-devel,rust-pyo3+abi3-py38-devel,rust-memmap2-devel,rust-memmap2+default-devel,rust-pyo3_0.22+abi3-py38-devel,rust-pyo3_0.22-devel,rust-pyo3_0.22+abi3-devel,rust-pyo3_0.22+default-devel,rust-pyo3+default-devel,rust-serde_json+default-devel

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license %{buildroot}/LICENSE


%changelog
%autochangelog
