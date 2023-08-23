<div align="center">
    <img src="./images/logo.png" width="500"/>
</div>

<br/><br/><br/>

Autobuild is a CI/CD automation for Flymya Mobile App (Android/IOS).

## About

In Flymya, the process of generating archives or APKs involves utilizing Xcode for iOS and Android Studio for APKs. This manual procedure necessitates the opening of these platforms each time. To facilitate this, frontend developers are provided with a dedicated machine for conducting these builds.

The implementation of Autobuild has been designed to streamline this process. Similar to Jenkins, Autobuild is configured to automatically generate archives and APKs whenever new code is pushed to a monitored branch. Upon detecting new code, the Autobuild program retrieves the latest commit, performs the installation of node packages, and adjusts the contents of the .env file according to the specific app variant.

To keep developers informed, the Autobuild program initiates communication. It sends a notification via Google Chat containing comprehensive build information to indicate the commencement of the build process for the respective commit. Upon the successful completion of the build, another Google Chat message is dispatched, presenting a concise overview of the build outcome.

Upon completion, the build artifacts are managed accordingly. The iOS archive file is uploaded to TestFlight, while the Android APK is transferred to Google Drive. Inclusion of the Google Drive APK sharing URL in the build summary message facilitates easy distribution to Product Owners for testing purposes.

Furthermore, Autobuild generates a detailed log file for each build, ensuring transparency in the event of a build failure. Developers gain insights into the specific reasons behind any failed build by referring to these logs.

Distinguishing itself from Jenkins, Autobuild is designed to handle one build process at a time. Should a new code push occur while a build process is already underway, the program intelligently stores the incoming commit information in a queue. This enables subsequent builds to be initiated once the ongoing one concludes.

A CLI is also added to interact with the program.<br/>
![cli-gif](images/cli.gif)

## Install

To install the program follow these steps. You need to add configrations in the **settings.py** file, according to your project structure, git branch, google chat and google drive.

**NOTE** : This project is created to automate only Flymya mobile app build process. It may not work with other projects, but if you still want to do setup for your own project then follow the below instructions.

After cloning the repository, create a virtual environment for python.

```
$ pipenv shell
```

Install all the packages

```
$ pipenv install
```

Download your google-service-key.json from google api console, and start the builder

```
$ python main.py
```

To open the CLI program

```
$ python cli.py
```

## Screenshots

![log](images/log.png)
![build-started-msg](images/build-started-msg.png)
![build-summary-msg](images/build-summary-msg.png)
![running](images/running.png)
