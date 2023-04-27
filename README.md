[![Downloads](https://pepy.tech/badge/scrappo)](https://pepy.tech/project/scrappo)

# Scrappo - Video Downloader Tool
## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [License](#license)
- [Status](#status)

<a name="description"></a>

## Description

Scrappo downloads any video from a given URL or a file containing a list of URLs. These URLs must be the actual video.

It's possible to also distinguish between a series or movies. The difference between these two options is that a series expects to have at least 1 season, therefore each season will be  separate into its own folder containing each related episode.

<a name="features"></a>

## Features

| Feature                                                                          |
|:---------------------------------------------------------------------------------|
| can be input a .txt file containing a list of URLs                               |
| download movies, series or related content                                       |
| series will be separate into season folders                                      |
| movies can also be separated in their own folder                                 |
| videos already downloaded will be skipped                                        |
| any errors regarding the videos will not stop program and will appear in the end |
| progress bar while downloading                                                   |


Any new features are **_very_** welcomed.

### Future features

Nothing at the moment.

<a name="prerequisites"></a>

## Prerequisites

[Python 3](https://www.python.org/downloads/) must be installed.

<a name="installation"></a>

## Installation

```
pip --no-cache-dir install scrappo
```

or,

```
pip3 --no-cache-dir install scrappo
```
<a name="usage"></a>
## Usage

| Command (shortcut)        | Command (full) | Required       | Description                                                                       |
|:--------------------------|----------------|----------------|:----------------------------------------------------------------------------------|
| -u                        | --urls         | **REQUIRED**   | a list of URLs or a path to a .txt file containing a list of URLs.                |
| -o                        | --output       | **REQUIRED**   | the path to the folder in which the videos will be downloaded.                    |
| -t                        | --type         | **REQUIRED**   | the type of the videos to download. Choices are "movies" or "series".             |
| --separate/--no-separate  | ---            | **OPTIONAL**   | if enabled, it will separate every movie into his own folder.                     |
| --shutdown/--no-shutdown  | ---            | **OPTIONAL**   | enable or disable shutting down computer when program is done                     |

---
### Important

#### URLs .txt file
The file containing a list of URLs must obey to certain requirements.

```text
nameOfVideo1:::https://someurl.withavideo.org//video1
nameOfVideo2:::https://someurl.withavideo.org//video2
https://someurl.withavideo.org//video3
https://someurl.withavideo.org//video4
nameOfVideo5:::https://someurl.withavideo.org//video5

https://someurl.withavideo.org//video6
nameOfVideo7:::https://someurl.withavideo.org//video7
```

- It could be added the name the file should have by inserting ':::' between the name and the URL.
- If a URL does not have ':::', its assumed the name of the file will be 'movie#' or 'episode#' (# being the number according to the position (line) the URL has in the file), depending on if the type is 'movies' or 'series', respectively.
- If type is 'series', the seasons should be separated by blank lines. This means, for instance in the example above, the season 1 has 5 episodes and the season 2 has 2 episodes. These episodes will be separated by folders with the name of corresponding season.
- If type is 'movies', any blank lines will be ignored.

---

The following command will download all given URLs with the type 'movies'. These videos will be downloaded in the 'C:\Users\<username>\Desktop\movies' folder:
```bash
scrappo --type movies --output "C:\Users\<username>\Desktop\movies" --urls "nameOfVideo1:::https://someurl.withavideo.org//video1" "nameOfVideo2:::https://someurl.withavideo.org//video2"
```
The same naming option is also available when not using a file.
The command above will download 2 videos from two different sources which the names of those video files will be 'nameOfVideo1' and 'nameOfVideo2', respectively.

The command below will do the same thing but separating each movie into its own folder. The folder name will be the same name as the video file name.
```bash
scrappo --type movies --output "C:\Users\<username>\Desktop\movies" --urls "nameOfVideo1:::https://someurl.withavideo.org//video1" "nameOfVideo2:::https://someurl.withavideo.org//video2" --separate
```

The following command will download all URLs contained in the 'C:\Users\<username>\Desktop\moviesToDownload.txt' file. Can also be used the '--separate' argument.
```bash
scrappo --type movies --output "C:\Users\<username>\Desktop\movies" --urls "C:\Users\<username>\Desktop\moviesToDownload.txt"
```

The command below will download all URLs contained in the 'C:\Users\<username>\Desktop\seriesToDownload.txt'. Inside 'C:\Users\<username>\Desktop\series' folder there will be at least a folder named 'season1' containing all related episodes. Keep in mind that the file needs to contain a blank line to indicate separation of seasons.
```bash
scrappo --type series --output "C:\Users\<username>\Desktop\series" --urls "C:\Users\<username>\Desktop\seriesToDownload.txt"
```

If '--shutdown' argument is used, when all videos are downloaded, the device will be shut down.
```bash
scrappo --type series --output "C:\Users\<username>\Desktop\series" --urls "C:\Users\<username>\Desktop\seriesToDownload.txt" --shutdown
```

<a name="support"></a>
## Support
 If any problems occurs, feel free to open an issue.

<a name="license"></a>
## License

[MIT](https://choosealicense.com/licenses/mit/)

<a name="status"></a>

## Status

Currently maintaining it.