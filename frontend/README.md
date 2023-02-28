# Frontend

To run this, please use the `docker-compose` script in the root README file.

## Installing Packages

To install a package, ensure that the app is running in docker (you should be able to visit localhost:3000 in your browser and see the page running).

Then, `cd` into the frontend (this) directory, and run the following script `./install_package.sh package1 package2 ...`. This will alias the npm install and use Docker to install the correct versions