import setuptools

setuptools.setup(name="AutoML2015",
                 description="Code to participate in the AutoML 2015 challenge.",
                 version="0.1dev",
                 packages=setuptools.find_packages(),
                 install_requires=["numpy",
                                   "pyyaml",
                                   "scipy",
                                   "scikit-learn==0.15.2",
                                   "nose",
                                   "lockfile"
                                   "HPOlibConfigSpace",
                                   "AutoSklearn",
                                   "cma"],
                 test_suite="nose.collector",
                 package_data={'': ['*.txt', '*.md', 'metadata']},
                 author="Matthias Feurer",
                 author_email="feurerm@informatik.uni-freiburg.de",
                 license="BSD",
                 platforms=['Linux'],
                 classifiers=[],
                 url='')
