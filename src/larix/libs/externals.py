from git import Repo
import appdirs
import yaml
import logging
from pathlib import Path
import larix.config as config

def repository_list():
    repositories = []

    if config.app.external_package_repository:
        repositories = repositories + [config.app.external_package_repository]

    if config.app.additional_package_repositories:
        repositories = repositories + list( filter(lambda x: bool(x),
            config.app.additional_package_repositories.split("\n")) )

    repositories = [record.split() for record in repositories]
    repositories = [
        ExternalPackageRepository(r[0], r[1], r[2]) for r in repositories]

    return repositories

class ExternalPackageRepository(object):
    def __init__(self, repo_url, repo_type, repo_name):
        self.repo_url = repo_url
        self.repo_type = repo_type
        self.repo_name = repo_name

        if self.repo_type == 'git':
            pass
        else:
            raise ValueError('unknown repository type')

        self.repos_dir = Path(appdirs.user_data_dir('larix'))/'external_repos'
        self.repo_dir = self.repos_dir/self.repo_name
        self.packages_yaml = self.repo_dir/'packages.yaml'
        self.packages_dir = self.repo_dir/'packages'


    def setup(self):
        if self.repo_type == 'git':
            self.repos_dir.mkdir(parents=True, exist_ok=True)

            repo = None
            
            try:
                repo = Repo(str(self.repo_dir))
            except:
                logging.debug("remote external repo_url: "+self.repo_url)
                logging.debug("remote external repo_type: "+self.repo_type)
                logging.debug("remote external repo_name: "+self.repo_name)

                logging.debug("clone remote repo")
                repo = Repo.clone_from(self.repo_url, str(self.repo_dir))

            if repo:
                packages_yaml = self.packages_yaml.open('w')

                for f in (self.repo_dir/'packages').glob('*.yaml'):
                    packages_yaml.write(f.open().read())
        else:
            raise ValueError('unknown repository type')


    def update(self):
        if self.repo_type == 'git':
            Repo(str(self.repo_dir)).remotes.origin.pull()

            packages_yaml = self.packages_yaml.open('w')

            for f in (self.packages_dir).glob('*.yaml'):
                packages_yaml.write(f.open().read())
        else:
            raise ValueError('unknown repository type')

    
    def is_setup(self):
        return self.packages_yaml.exists()

    def packages(self):
        package_files = yaml.load_all(self.packages_yaml.open().read())

        packages = {}

        for package_file in package_files:
            if 'packages' not in package_file:
                continue

            for package in package_file['packages']:
                packages[package['name']] = package

        return packages


